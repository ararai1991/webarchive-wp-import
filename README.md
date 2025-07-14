# webarchive-wp-import
Automate fetching Wayback Machine snapshots and generating a WordPress WXR import for your wordpress blog.

# README

## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. (Optional) Create and activate a virtual environment:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install required libraries:  
   ```bash
   pip install -r requirements.txt
   ```

## Required Libraries

- `requests`  
- `beautifulsoup4`  
- `lxml`  
- `python-dateutil` (optional, for advanced date parsing)  
- Standard libraries: `datetime`, `urllib`, `time`, `sys`, `re`, `random`

Or install individually:  
```bash
pip install requests beautifulsoup4 lxml python-dateutil
```

## Configuration

### `export.py`

Edit the `params` dictionary and replace the placeholder with your WordPress blog URL:

```python
params = {
    "url": "ENTER-YOUR-WEB-SITE-URL-HERE/*",
    # …
}
```

### `request.py`

In the WXR template section, replace the placeholders with your site title and URL:

```xml
<title>ENTER-YOUR-TITLE</title>
<link>ENTER-YOUR-WEBSITE-URL-HERE</link>
```

## How It Works

1. **export.py**  
   - Queries the Internet Archive CDX API for snapshots of your blog posts.  
   - Saves each post URL and timestamp into `export-urls.txt`.

2. **request.py**  
   - Reads `export-urls.txt` and downloads each archived HTML snapshot.  
   - Uses BeautifulSoup to parse title, content, author, and timestamp.  
   - Generates a WordPress WXR XML file (`final_wp_import.xml`) ready for import.
