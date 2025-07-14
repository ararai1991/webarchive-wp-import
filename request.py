import requests  # HTTP requests to fetch pages
from bs4 import BeautifulSoup  # HTML parsing
from datetime import datetime, timezone  # timestamp handling
from urllib.parse import urlparse  # URL parsing (not used currently)
from time import sleep  # introduce delays between requests
from sys import stdout  # progress output
import re  # regex operations for parsing
import random  # random delay generation


def fetch_snapshot_html(url, ts=None):
    """
    Fetch HTML snapshot from the Internet Archive for the given URL.
    If a timestamp (ts) is not provided, query the CDX API for the closest snapshot.

    Args:
        url (str): The target URL to snapshot.
        ts (str, optional): Specific archive timestamp in YYYYMMDDhhmmss format.

    Returns:
        tuple: (html_text, timestamp) or (None, None) on failure.
    """
    if not ts:
        # Query CDX API for the closest valid snapshot
        cdx_url = "https://web.archive.org/cdx/search/cdx"
        params = {
            "url": url,
            "output": "json",
            "limit": "1",
            "filter": "statuscode:200",
            "sort": "closest"
        }
        res = requests.get(cdx_url, params=params)
        if res.status_code != 200 or len(res.json()) <= 1:
            return None, None
        ts = res.json()[1][1]

    # Construct the archive URL and fetch the page
    snapshot_url = f"https://web.archive.org/web/{ts}id_/{url}"
    page = requests.get(snapshot_url)
    if page.status_code == 200:
        return page.text, ts
    return None, None


def extract_post_data(html, url):
    """
    Parse the fetched HTML to extract title, content, and author info.

    Args:
        html (str): Raw HTML text of the page.
        url (str): Original URL for reference.

    Returns:
        tuple: (title, content_text, url, author_display, author_login)
    """
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "No Title"

    # Try to find the main content container: <article>, <main>, or fallback to <body>
    content_div = soup.find("article") or soup.find("main") or soup.find("body")
    content = content_div.get_text(separator="\n", strip=True) if content_div else "No content found"

    # Locate the author element by common class patterns
    author_tag = soup.select_one('span[class*="author"] a, span[class*="arz-post__info-author-name"] a')
    author_display = author_tag.get_text(strip=True) if author_tag else "admin"
    author_login = "admin"

    # Extract the login slug from the href if possible
    if author_tag and "href" in author_tag.attrs:
        href = author_tag["href"]
        match = re.search(r'/author/([^/]+)/?', href)
        if match:
            author_login = match.group(1)
        else:
            author_login = slugify(author_display)
    else:
        author_login = slugify(author_display)

    return title, content, url, author_display, author_login


def escape_xml(text):
    """
    Escape XML special characters to ensure valid output.
    """
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&apos;"))


def slugify(text):
    """
    Convert text to a URL-friendly slug (lowercase, hyphens).
    """
    return text.strip().lower().replace(" ", "-").replace("/", "-").replace(".", "-")


# -------------------- MAIN SCRIPT --------------------

# Define the random delay interval (in seconds)
MIN_DELAY = 1.0  # minimum delay between requests
MAX_DELAY = 5.0  # maximum delay between requests

# Read URLs (and optional timestamps) from file
with open("export-urls.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# Parse lines into tuples: (url, ts) or (url, None)
urls_with_ts = [tuple(line.split("|")) if "|" in line else (line, None) for line in lines]

# Initialize collectors and counters
items_xml = ""
authors = {}
success_count = 0
fail_count = 0
failed_urls = []
snapshot_lines = []
total = len(urls_with_ts)

for idx, (url, ts) in enumerate(urls_with_ts, start=1):
    try:
        html, final_ts = fetch_snapshot_html(url, ts)
        if html and final_ts:
            title, content, link, author_display, author_login = extract_post_data(html, url)
            authors[author_login] = author_display

            # Format post timestamp and slug
            post_date = datetime.strptime(final_ts[:8], "%Y%m%d").strftime("%Y-%m-%d 00:00:00")
            slug = slugify(url)
            archive_url = f"https://web.archive.org/web/{final_ts}id_/{url}"
            snapshot_lines.append(archive_url)

            # Build XML item block
            items_xml += f"""
    <item>
        <title>{escape_xml(title)}</title>
        <link>{link}</link>
        <pubDate>{datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>
        <dc:creator><![CDATA[{author_login}]]></dc:creator>
        <guid isPermaLink="false">{link}</guid>
        <description></description>
        <content:encoded><![CDATA[{content}]]></content:encoded>
        <excerpt:encoded><![CDATA[]]></excerpt:encoded>
        <wp:post_id>{idx}</wp:post_id>
        <wp:post_date>{post_date}</wp:post_date>
        <wp:post_date_gmt>{post_date}</wp:post_date_gmt>
        <wp:comment_status>closed</wp:comment_status>
        <wp:ping_status>closed</wp:ping_status>
        <wp:post_name>{slug}</wp:post_name>
        <wp:status>publish</wp:status>
        <wp:post_parent>0</wp:post_parent>
        <wp:menu_order>0</wp:menu_order>
        <wp:post_type>post</wp:post_type>
        <wp:post_password></wp:post_password>
        <wp:is_sticky>0</wp:is_sticky>
    </item>
            """
            success_count += 1
        else:
            raise Exception("No snapshot data")
    except Exception:
        failed_urls.append(url)
        fail_count += 1

    # Introduce a random delay before next request
    delay = random.uniform(MIN_DELAY, MAX_DELAY)
    stdout.write(f"\r[{idx}/{total}] Processing... | {success_count} | {fail_count} | Delay: {delay:.2f}s")
    stdout.flush()
    sleep(delay)

print()  # newline after progress

# Save list of failed URLs if any
if failed_urls:
    with open("failed_urls.txt", "w", encoding="utf-8") as f:
        for u in failed_urls:
            f.write(u + "\n")
    print("failed_urls.txt saved")

# Save all snapshot URLs
if snapshot_lines:
    with open("snapshot_urls.txt", "w", encoding="utf-8") as f:
        for u in snapshot_lines:
            f.write(u + "\n")
    print("snapshot_urls.txt saved")

# Build author blocks for WordPress export
author_blocks = ""
for idx, (login, display) in enumerate(sorted(authors.items()), start=1):
    author_blocks += f"""
    <wp:author>
        <wp:author_id>{idx}</wp:author_id>
        <wp:author_login><![CDATA[{login}]]></wp:author_login>
        <wp:author_display_name><![CDATA[{display}]]></wp:author_display_name>
        <wp:author_email>{login}@example.com</wp:author_email>
    </wp:author>
    """

# Final RSS/WXR assembly
rss_template = f"""<?xml version=\"1.0\" encoding=\"UTF-8\" ?>
<rss version=\"2.0\" xmlns:excerpt=\"http://wordpress.org/export/1.2/excerpt/\" xmlns:content=\"http://purl.org/rss/1.0/modules/content/\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:wp=\"http://wordpress.org/export/1.2/\">
<channel>
    <title>ENTER-YOUR-TITLE</title>
    <link>EBTER-YOUR-WEBSITE-URL-HERE</link>
    <description>Imported posts from Wayback Archive</description>
    <pubDate>{datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>
    <language>en</language>
    <wp:wxr_version>1.2</wp:wxr_version>
    {author_blocks}
    {items_xml}
</channel>
</rss>"""

with open("final_wp_import.xml", "w", encoding="utf-8") as f:
    f.write(rss_template)

print("📦 WordPress WXR file saved as final_wp_import.xml")
