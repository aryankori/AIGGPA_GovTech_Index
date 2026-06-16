"""Flask web server for Instagram alt-text + reverse image search."""

import os
import json
import threading
import queue
from flask import Flask, render_template, request, jsonify, Response

import db
import scraper
from hasher import compute_phash

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max upload

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# --- SSE progress stream ---
progress_queues: list[queue.Queue] = []


def broadcast_progress(msg: str):
    for q in progress_queues:
        q.put(msg)


scraper.set_progress_callback(broadcast_progress)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/login", methods=["POST"])
def api_login():
    """Trigger manual login in a visible browser window."""
    def do_login():
        try:
            result = scraper.login_interactive()
            broadcast_progress(f"Login {'successful' if result else 'failed'}.")
            broadcast_progress("__DONE__")
        except Exception as e:
            broadcast_progress(f"Login error: {e}")
            broadcast_progress("__DONE__")

    t = threading.Thread(target=do_login, daemon=True)
    t.start()
    return jsonify({"status": "ok", "message": "Browser window opening. Log in manually."})


@app.route("/api/login/status")
def api_login_status():
    """Fast login status check (file-based, no browser launch)."""
    logged_in = scraper.is_logged_in()
    return jsonify({"logged_in": logged_in})


@app.route("/api/login/verify", methods=["POST"])
def api_login_verify():
    """Full session verification (launches headless browser — slower)."""
    def do_verify():
        result = scraper.verify_session()
        broadcast_progress(f"Session {'valid' if result else 'expired'}.")
        broadcast_progress("__DONE__")

    t = threading.Thread(target=do_verify, daemon=True)
    t.start()
    return jsonify({"status": "ok", "message": "Verifying session..."})


@app.route("/api/search", methods=["POST"])
def api_search():
    """Keyword search against cached alt texts."""
    data = request.json or {}
    keyword = data.get("keyword", "").strip()
    target = data.get("target", "")
    if not keyword:
        return jsonify({"error": "keyword required"}), 400

    usernames = None
    if target and target != "mutuals":
        usernames = [target.lstrip("@")]
    elif target == "mutuals":
        usernames = db.get_cached_usernames()

    results = db.search_keyword(keyword, usernames)
    return jsonify({"results": results, "count": len(results)})


@app.route("/api/reverse", methods=["POST"])
def api_reverse():
    """Reverse image search: upload an image, find matching posts by pHash."""
    if "image" not in request.files:
        return jsonify({"error": "no image uploaded"}), 400

    file = request.files["image"]
    if not file.filename:
        return jsonify({"error": "empty filename"}), 400

    filepath = os.path.join(UPLOAD_DIR, file.filename)
    file.save(filepath)

    try:
        target_hash = compute_phash(filepath)
    except Exception as e:
        return jsonify({"error": f"Failed to hash image: {e}"}), 400
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

    threshold = int(request.form.get("threshold", 10))
    target = request.form.get("target", "")
    usernames = None
    if target and target != "mutuals":
        usernames = [target.lstrip("@")]
    elif target == "mutuals":
        usernames = db.get_cached_usernames()

    results = db.search_by_phash(target_hash, threshold, usernames)
    return jsonify({
        "query_hash": target_hash,
        "threshold": threshold,
        "results": results,
        "count": len(results),
    })


@app.route("/api/scrape", methods=["POST"])
def api_scrape():
    """Trigger a scrape of target usernames in a background thread."""
    data = request.json or {}
    target = data.get("target", "")
    max_posts = data.get("max_posts", 12)

    if not scraper.is_logged_in():
        return jsonify({
            "status": "error",
            "message": "Not logged in. Click Login first."
        }), 401

    def do_scrape():
        try:
            if target == "mutuals":
                broadcast_progress("Fetching mutuals list...")
                mutuals = scraper.get_mutuals()
                if not mutuals:
                    broadcast_progress("No mutuals found. Check if you're logged in.")
                    broadcast_progress("__DONE__")
                    return
                broadcast_progress(f"Found {len(mutuals)} mutuals. Starting scrape...")
                scraper.scrape_profiles(mutuals, max_posts)
            elif target:
                username = target.lstrip("@")
                scraper.scrape_profile(username, max_posts)
            broadcast_progress("__DONE__")
        except Exception as e:
            broadcast_progress(f"Error: {e}")
            broadcast_progress("__DONE__")

    t = threading.Thread(target=do_scrape, daemon=True)
    t.start()
    return jsonify({"status": "ok", "message": f"Scraping started for: {target}"})


@app.route("/api/progress")
def api_progress():
    """SSE endpoint for live scrape progress."""
    q = queue.Queue()
    progress_queues.append(q)

    def stream():
        try:
            while True:
                msg = q.get(timeout=120)
                yield f"data: {json.dumps({'message': msg})}\n\n"
                if msg == "__DONE__":
                    break
        except queue.Empty:
            yield f"data: {json.dumps({'message': 'timeout'})}\n\n"
        finally:
            if q in progress_queues:
                progress_queues.remove(q)

    return Response(stream(), mimetype="text/event-stream")


@app.route("/api/cached")
def api_cached():
    """Return list of cached usernames."""
    return jsonify({"usernames": db.get_cached_usernames()})


if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)
