"""Instagram scraper using Playwright browser automation.

Login strategy: opens a VISIBLE browser window for manual login (handles 2FA),
then takes over the authenticated session for automated scraping.
Uses playwright.sync_api to avoid asyncio.run() conflicts in threads.
"""

import os
import random
import time
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright, Page, BrowserContext

import db
from hasher import compute_phash

SESSION_DIR = os.path.join(os.path.dirname(__file__), ".session")
BASE_URL = "https://www.instagram.com"

# --- Progress callback (set by app.py for SSE updates) ---
_progress_callback = None


def set_progress_callback(fn):
    global _progress_callback
    _progress_callback = fn


def _emit(msg: str):
    if _progress_callback:
        _progress_callback(msg)
    print(f"[scraper] {msg}")


# --- Delays to mimic human behavior ---
def _human_delay(lo=2, hi=5):
    time.sleep(random.uniform(lo, hi))


def _long_delay():
    time.sleep(random.uniform(15, 30))


# --- Browser setup ---
def _get_context(playwright, headless=False) -> BrowserContext:
    """Return a persistent browser context (saves cookies/session across runs)."""
    os.makedirs(SESSION_DIR, exist_ok=True)
    context = playwright.chromium.launch_persistent_context(
        SESSION_DIR,
        headless=headless,
        viewport={"width": 1280, "height": 900},
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125.0.0.0 Safari/537.36"
        ),
    )
    return context


# --- Login ---
def login_interactive() -> bool:
    """Open a visible browser for the user to log in manually.
    
    Returns True once the user is logged in (detected by URL change).
    """
    _emit("Opening browser for manual Instagram login...")
    with sync_playwright() as pw:
        ctx = _get_context(pw, headless=False)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(f"{BASE_URL}/accounts/login/", wait_until="networkidle")

        # Check if already logged in
        if "/accounts/login" not in page.url:
            _emit("Already logged in from previous session.")
            ctx.close()
            return True

        _emit("Please log in manually in the browser window. Waiting up to 5 minutes...")

        # Wait for navigation away from login page (max 5 minutes)
        try:
            page.wait_for_url(
                lambda url: "/accounts/login" not in url,
                timeout=300_000
            )
            _emit("Login detected!")
            _human_delay(2, 4)

            # Dismiss popups
            for _ in range(2):
                try:
                    btn = page.locator("button:has-text('Not Now')").first
                    if btn.is_visible(timeout=3000):
                        btn.click()
                        _human_delay(1, 2)
                except Exception:
                    pass

            _emit("Login successful. Closing browser window.")
            ctx.close()
            return True
        except Exception as e:
            _emit(f"Login failed or timed out: {e}")
            ctx.close()
            return False


def is_logged_in() -> bool:
    """Check if we have a valid saved session by looking at session files.
    
    Fast check: just verifies session directory has cookie data.
    Does NOT launch a browser.
    """
    if not os.path.exists(SESSION_DIR):
        return False
    # Check if there are any files in the session dir (Chromium stores cookies, etc.)
    files = os.listdir(SESSION_DIR)
    # A logged-in session will have multiple files including cookies
    return len(files) > 5


def verify_session() -> bool:
    """Full verification: launches headless browser to check if session is still valid.
    
    Slower than is_logged_in() but more accurate.
    """
    if not is_logged_in():
        return False
    try:
        with sync_playwright() as pw:
            ctx = _get_context(pw, headless=True)
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
            page.goto(BASE_URL, wait_until="networkidle", timeout=15000)
            result = "/accounts/login" not in page.url
            ctx.close()
            return result
    except Exception:
        return False


# --- Followers / Following / Mutuals ---
def _scroll_user_list(page: Page, dialog_selector: str, max_users: int = 500) -> list[str]:
    """Scroll through a followers/following dialog and collect usernames."""
    usernames = set()
    dialog = page.locator(dialog_selector)

    prev_count = 0
    stale_rounds = 0
    while len(usernames) < max_users:
        links = dialog.locator("a[href^='/']").all()
        for link in links:
            href = link.get_attribute("href")
            if href and href.count("/") == 2:
                usernames.add(href.strip("/"))

        if len(usernames) == prev_count:
            stale_rounds += 1
            if stale_rounds >= 3:
                break
        else:
            stale_rounds = 0
        prev_count = len(usernames)

        dialog.evaluate("el => el.scrollTop = el.scrollHeight")
        _human_delay(1, 2)

    return list(usernames)


def get_mutuals() -> list[str]:
    """Get the intersection of following and followers (mutuals)."""
    _emit("Fetching mutuals (following ∩ followers)...")
    with sync_playwright() as pw:
        ctx = _get_context(pw, headless=True)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        # Go to Instagram home
        page.goto(BASE_URL, wait_until="networkidle")
        _human_delay()

        # Navigate to own profile via the profile icon/link
        # Try multiple selectors since Instagram's UI changes
        own_username = None
        try:
            # Method 1: Look for profile link in navigation
            nav_links = page.locator("nav a[href^='/']").all()
            for link in nav_links:
                href = link.get_attribute("href") or ""
                # Profile links have format /<username>/ with exactly 2 slashes
                if href.count("/") == 2 and href.strip("/") not in ("explore", "reels", "direct"):
                    own_username = href.strip("/")
                    break
        except Exception:
            pass

        if not own_username:
            try:
                # Method 2: Check the page source for the logged-in username
                content = page.content()
                import re
                match = re.search(r'"username":"([^"]+)"', content)
                if match:
                    own_username = match.group(1)
            except Exception:
                pass

        if not own_username:
            _emit("Could not determine your username. Are you logged in?")
            ctx.close()
            return []

        _emit(f"Your username: @{own_username}")

        # Get following
        _emit("Fetching following list...")
        page.goto(f"{BASE_URL}/{own_username}/following/", wait_until="networkidle")
        _human_delay()
        following = _scroll_user_list(page, "div[role='dialog'] div[style*='overflow']")
        _emit(f"Following: {len(following)} accounts")

        _long_delay()

        # Get followers
        _emit("Fetching followers list...")
        page.goto(f"{BASE_URL}/{own_username}/followers/", wait_until="networkidle")
        _human_delay()
        followers = _scroll_user_list(page, "div[role='dialog'] div[style*='overflow']")
        _emit(f"Followers: {len(followers)} accounts")

        ctx.close()

    mutuals = list(set(following) & set(followers))
    _emit(f"Mutuals: {len(mutuals)} accounts")
    return sorted(mutuals)


# --- Profile scraping ---
def scrape_profile(username: str, max_posts: int = 12):
    """Scrape a profile's posts and profile picture, store in DB."""
    _emit(f"Scraping @{username} (up to {max_posts} posts)...")

    with sync_playwright() as pw:
        ctx = _get_context(pw, headless=True)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        # Visit profile
        page.goto(f"{BASE_URL}/{username}/", wait_until="networkidle")
        _human_delay()

        # Check if profile exists and is accessible
        title = page.title()
        if "Page Not Found" in title or "Instagram" == title:
            sorry = page.locator("h2:has-text('Sorry')").first
            try:
                if sorry.is_visible(timeout=2000):
                    _emit(f"@{username}: profile not found or private. Skipping.")
                    ctx.close()
                    return
            except Exception:
                pass

        # --- Profile picture ---
        try:
            pfp_img = page.locator(f"header img").first
            pfp_url = pfp_img.get_attribute("src")
            if pfp_url:
                _emit(f"@{username}: downloading profile picture...")
                pfp_hash = compute_phash(pfp_url)
                pfp_alt = pfp_img.get_attribute("alt") or ""
                db.upsert_post(
                    username=username,
                    post_url=f"{BASE_URL}/{username}/",
                    image_url=pfp_url,
                    alt_text=pfp_alt,
                    phash=pfp_hash,
                    is_profile_pic=True,
                )
                _emit(f"@{username}: profile picture indexed (pHash: {pfp_hash})")
        except Exception as e:
            _emit(f"@{username}: could not get profile picture ({e})")

        # --- Collect post links from grid ---
        post_links = []
        try:
            grid_links = page.locator("main a[href*='/p/']").all()
            for link in grid_links[:max_posts]:
                href = link.get_attribute("href")
                if href:
                    post_links.append(urljoin(BASE_URL, href))
        except Exception:
            pass

        _emit(f"@{username}: found {len(post_links)} posts")

        # --- Visit each post and extract data ---
        for i, post_url in enumerate(post_links):
            try:
                page.goto(post_url, wait_until="networkidle")
                _human_delay(1, 3)

                # Find the main post image
                img = page.locator("article img[alt]").first
                img_url = img.get_attribute("src") or ""
                alt_text = img.get_attribute("alt") or ""

                # Compute perceptual hash
                phash = ""
                if img_url:
                    try:
                        phash = compute_phash(img_url)
                    except Exception:
                        pass

                db.upsert_post(
                    username=username,
                    post_url=post_url,
                    image_url=img_url,
                    alt_text=alt_text,
                    phash=phash,
                    is_profile_pic=False,
                )
                _emit(f"@{username}: post {i+1}/{len(post_links)} indexed")

            except Exception as e:
                _emit(f"@{username}: error on post {i+1} ({e})")

            _human_delay(2, 4)

        ctx.close()

    _emit(f"@{username}: done.")


def scrape_profiles(usernames: list[str], max_posts: int = 12):
    """Scrape multiple profiles sequentially with long delays between each."""
    for i, username in enumerate(usernames):
        _emit(f"--- Profile {i+1}/{len(usernames)}: @{username} ---")
        if not db.is_stale(username):
            _emit(f"@{username}: cached data still fresh, skipping.")
            continue
        scrape_profile(username, max_posts)
        if i < len(usernames) - 1:
            _emit("Waiting before next profile...")
            _long_delay()

    _emit("All profiles scraped.")
