WebArchive WP Import

Video Demo: https://cdn.imgurl.ir/uploads/n861381_cs50xFINAL-output.mp4

Description:

Overview WebArchive WP Import is a tool designed to import archived web pages from the Internet Archive’s Wayback Machine into WordPress. It assists website administrators in restoring lost or deleted content by transforming archived HTML data into WordPress‐compatible posts.

Technical Details

Language: Python 3
Key Libraries: requests, BeautifulSoup4, xml.etree.ElementTree, argparse
Input: list of URLs (via file or command‐line)
Output: WordPress import file (XML)
Sample command: python webarchive_importer.py --input urls.txt --output output.xml
Features

Fetches archived pages automatically via Wayback Machine
Parses HTML, extracts content (images/links), and rebuilds internal structure
Converts content to WordPress import format (WXR)
Supports batch processing of multiple URLs/domains
Project Structure webarchive-wp-import/ │ ├── webarchive_importer.py # Main script
├── parser/ │ ├── html_parser.py # Module to parse HTML content
│ └── utils.py # General utility functions
├── samples/ │ ├── urls.txt # Example input file
│ └── output.xml # Example WP import file
├── requirements.txt # Python dependencies
└── README.txt # This file

How It Works

Prepare a text file (e.g., urls.txt) containing the list of archived URLs you want to restore.
Run the script to fetch and process each URL.
The script extracts content, cleans up markup, rebuilds links/images, and packages everything into a WordPress import file.
In WordPress, go to Tools → Import → WordPress, and upload the resulting XML to restore posts.
Design Choices

Used BeautifulSoup instead of regex for HTML parsing to handle messy markup robustly.
Chose plain XML output (rather than a database) for compatibility with WordPress’s native importer.
Modular structure to allow future extensions (GUI, REST API, etc.).
Challenges

Handling inconsistencies in archived HTML (broken links, missing images) required heuristic fixes.
Converting arbitrary HTML into structured WordPress post format with metadata (title/date) was non-trivial.
Ensuring batch processing scales and avoids redundant downloads.
Lessons Learned

Gained experience working with web APIs, HTTP requests and parsing XML/HTML.
Developed scripting proficiency for command‐line utilities with arguments and flags.
Improved modular design and separation of concerns in a real‐world tool.
Future Improvements

Add a graphical user interface (GUI) for easier use by non-technical users.
Support translation of content and automatic metadata enrichment.
Integrate a direct WordPress plugin version instead of external script.
Acknowledgements Thank you to the CS50x 2025 instructors and staff for providing the curriculum and inspiration. Portions of this project were developed with help from ChatGPT and GitHub Copilot (limited assistance).

How to run git clone https://github.com/ararai1991/webarchive-wp-import
cd webarchive-wp-import
pip install -r requirements.txt
python webarchive_importer.py --input samples/urls.txt --output samples/output.xml


---

## 💬 Additional Notes

This project was designed and implemented entirely by **Alireza Rezaei** as part of the **CS50x 2025 Final Project**.  
It represents an exploration into web automation, HTML parsing, and data migration between platforms.  

The core motivation behind this project was to simplify the process of restoring lost web content from the Internet Archive and make it accessible again through WordPress.  
While developing the tool, I focused heavily on clean code organization, modularity, and error handling.  

By completing this project, I have not only learned more about Python scripting and API usage,  
but also about how to design real-world tools that address practical problems in digital archiving and web restoration.

---

## 🧩 Reflection

CS50x has been an incredible journey that strengthened my understanding of programming fundamentals and project design.  
Creating this final project helped me consolidate everything I learned throughout the course — from loops and conditionals to file I/O, APIs, and software design.  
It was both challenging and rewarding to turn an idea into a fully functional piece of software.

Thank you to the CS50 team for providing the structure, guidance, and inspiration to bring this project to life.

---
