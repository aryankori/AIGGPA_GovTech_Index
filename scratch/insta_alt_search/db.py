import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "cache.db")
CACHE_TTL_DAYS = 7


def _get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    """Create tables and FTS5 index if they don't exist."""
    conn = _get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS posts (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            username        TEXT NOT NULL,
            post_url        TEXT,
            image_url       TEXT NOT NULL,
            alt_text        TEXT DEFAULT '',
            phash           TEXT DEFAULT '',
            is_profile_pic  INTEGER DEFAULT 0,
            scraped_at      TEXT DEFAULT (datetime('now')),
            UNIQUE(username, image_url)
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS posts_fts
            USING fts5(alt_text, content=posts, content_rowid=id);

        CREATE TRIGGER IF NOT EXISTS posts_ai AFTER INSERT ON posts BEGIN
            INSERT INTO posts_fts(rowid, alt_text) VALUES (new.id, new.alt_text);
        END;

        CREATE TRIGGER IF NOT EXISTS posts_ad AFTER DELETE ON posts BEGIN
            INSERT INTO posts_fts(posts_fts, rowid, alt_text)
                VALUES ('delete', old.id, old.alt_text);
        END;

        CREATE TRIGGER IF NOT EXISTS posts_au AFTER UPDATE ON posts BEGIN
            INSERT INTO posts_fts(posts_fts, rowid, alt_text)
                VALUES ('delete', old.id, old.alt_text);
            INSERT INTO posts_fts(rowid, alt_text) VALUES (new.id, new.alt_text);
        END;
    """)
    conn.commit()
    conn.close()


def upsert_post(username: str, post_url: str, image_url: str,
                alt_text: str = "", phash: str = "", is_profile_pic: bool = False):
    """Insert or update a post record."""
    conn = _get_conn()
    conn.execute("""
        INSERT INTO posts (username, post_url, image_url, alt_text, phash, is_profile_pic)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(username, image_url) DO UPDATE SET
            alt_text = excluded.alt_text,
            phash = excluded.phash,
            scraped_at = datetime('now')
    """, (username, post_url, image_url, alt_text, phash, int(is_profile_pic)))
    conn.commit()
    conn.close()


def search_keyword(keyword: str, usernames: list[str] | None = None) -> list[dict]:
    """Full-text search on alt_text. Optionally filter by usernames."""
    conn = _get_conn()
    if usernames:
        placeholders = ",".join("?" for _ in usernames)
        rows = conn.execute(f"""
            SELECT p.* FROM posts p
            JOIN posts_fts f ON f.rowid = p.id
            WHERE posts_fts MATCH ?
            AND p.username IN ({placeholders})
            ORDER BY rank
        """, [keyword] + usernames).fetchall()
    else:
        rows = conn.execute("""
            SELECT p.* FROM posts p
            JOIN posts_fts f ON f.rowid = p.id
            WHERE posts_fts MATCH ?
            ORDER BY rank
        """, (keyword,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def search_by_phash(target_hash: str, threshold: int = 10,
                    usernames: list[str] | None = None) -> list[dict]:
    """Find images with perceptual hash within Hamming distance threshold.
    
    Scans all stored hashes (fast enough for thousands of images).
    """
    from hasher import hamming_distance

    conn = _get_conn()
    if usernames:
        placeholders = ",".join("?" for _ in usernames)
        rows = conn.execute(f"""
            SELECT * FROM posts
            WHERE phash != '' AND username IN ({placeholders})
        """, usernames).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM posts WHERE phash != ''"
        ).fetchall()
    conn.close()

    results = []
    for row in rows:
        dist = hamming_distance(target_hash, row["phash"])
        if dist <= threshold:
            entry = dict(row)
            entry["hamming_distance"] = dist
            results.append(entry)

    results.sort(key=lambda x: x["hamming_distance"])
    return results


def get_cached_usernames() -> list[str]:
    """Return list of usernames that have been scraped."""
    conn = _get_conn()
    rows = conn.execute("SELECT DISTINCT username FROM posts").fetchall()
    conn.close()
    return [r["username"] for r in rows]


def is_stale(username: str) -> bool:
    """Check if cached data for a username is older than CACHE_TTL_DAYS."""
    conn = _get_conn()
    row = conn.execute(
        "SELECT MAX(scraped_at) as latest FROM posts WHERE username = ?",
        (username,)
    ).fetchone()
    conn.close()
    if not row or not row["latest"]:
        return True
    latest = datetime.fromisoformat(row["latest"])
    return datetime.utcnow() - latest > timedelta(days=CACHE_TTL_DAYS)


# Initialize on import
init_db()
