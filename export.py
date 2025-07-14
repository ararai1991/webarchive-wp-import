# Script to retrieve archived URLs and timestamps from the Internet Archive CDX API
# and save them to a local file for Website import

import requests  # to perform HTTP requests
from sys import stdout  # for progress output to console

# CDX API endpoint for Wayback Machine snapshots
url = "https://web.archive.org/cdx/search/cdx"
# Parameters for the API query:
#   url      : pattern to match archived pages (here, all blog posts)
#   output   : JSON format for easy parsing
#   fl       : fields to return (original URL and timestamp)
#   collapse : collapse entries by URL key to avoid duplicates
params = {
    "url": "ENTER-YOUR-WEB-SITE-URL-HERE/*",
    "output": "json",
    "fl": "original,timestamp",
    "collapse": "urlkey"
}

# Send the GET request to the CDX API
response = requests.get(url, params=params)

# Check for a successful API response
if response.status_code == 200:
    # Parse the JSON payload into a Python list
    data = response.json()
    # The first entry is header info, so subtract one for the total count
    total = len(data) - 1
    # Prepare a list to collect lines of the form: url|timestamp
    urls = []

    # Iterate over each record (skipping the header row at index 0)
    for idx, row in enumerate(data[1:], start=1):
        # Extract original URL from the first element
        original = row[0]
        # Extract timestamp if available (second element), else empty string
        timestamp = row[1] if len(row) > 1 else ""
        # Combine URL and timestamp with a '|' delimiter if timestamp exists
        line = f"{original}|{timestamp}" if timestamp else original
        urls.append(line)

        # Display progress: current record / total and percentage complete
        percent = (idx / total) * 100
        stdout.write(f"\r⏳ Processing {idx}/{total} ({percent:.1f}%)")
        stdout.flush()

    # After collecting all entries, write them to an output file
    output_file = "export-urls.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in urls:
            f.write(entry + "\n")

    # Feedback to the user about completion and file location
    print(f"\n {len(urls)} URLs with timestamps saved to {output_file}")

else:
    # Handle non-200 HTTP responses
    print(f" Error: Received status code {response.status_code} from CDX API")
