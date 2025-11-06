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

---

## 🌍 Background and Motivation

The motivation behind this project came from my personal experience of losing old blog content that was only accessible through the Wayback Machine.  
Manually restoring each post was time-consuming and error-prone.  
This inspired the creation of an automated solution — one that could extract data, clean it, and export it in a format WordPress could directly import.  
This project bridges the gap between historical internet data and modern CMS usability, empowering users to reclaim their online history.

## 🔬 Design and Implementation Details

The project was structured to follow clean software design principles:
- **Modularization:** Different modules handle parsing, exporting, and data transformation.
- **Scalability:** Batch processing enables the tool to handle hundreds of URLs efficiently.
- **Resilience:** Exception handling ensures that missing or broken HTML elements don't crash the workflow.
- **Reusability:** The parser module can easily be extended for other CMS platforms.

### Algorithmic Workflow
1. Fetch snapshot metadata from the Internet Archive CDX API.  
2. Retrieve archived HTML for each snapshot.  
3. Use BeautifulSoup to extract page structure, title, metadata, and media links.  
4. Normalize links and remove unnecessary elements (scripts, tracking).  
5. Export data as a valid WXR XML file that WordPress can import.

## 💡 Reflection

Through this project, I applied nearly every concept learned in CS50 — from data structures to file I/O and APIs.  
It transformed abstract knowledge into a tangible, useful program.  
Working with real-world data, debugging malformed HTML, and ensuring consistent XML outputs required persistence and creativity.

CS50 taught me how to learn, debug, and document — and this project represents the culmination of that journey.  
I am proud of this tool not just for its code, but for the learning it encapsulates.

---

---

## 🧠 Deep Dive: Development Process

This project evolved through multiple iterations. The initial prototype simply fetched a single archived page, but over time, the architecture expanded to handle batch downloads, improved HTML parsing, and conversion to WordPress XML format.  
Throughout the process, I emphasized readability, comments, and modularization, so that others could contribute or adapt the project easily.  

Another challenge was dealing with pages that contained broken or outdated HTML tags. I used BeautifulSoup’s flexibility to recover usable structures, normalize links, and identify missing media files. I also added exception handling to skip problematic pages instead of crashing the process.  

Testing was performed across several URL sets, ensuring that the tool worked for both single-domain and multi-domain archives. The XML output was validated against the WordPress import schema.  

---

## 💭 Broader Impact

The project demonstrates how open-source technology can be used to preserve digital history. Many websites vanish from the internet each year, and tools like this can restore lost information for research, journalism, and education.  
By automating this process, anyone can rebuild an old blog, company site, or digital archive without technical complexity.  

The tool also highlights how programming can serve as a bridge between digital archaeology and modern content management systems. It’s a small step toward democratizing access to lost web knowledge.

---

## 🏆 Final Thoughts

Working on this project was both technically and personally rewarding. I learned about web data preservation, XML generation, modular software design, and most importantly — perseverance through debugging!  

If I had more time, I would expand this project into a full-featured WordPress plugin or web interface, allowing non-programmers to restore archives with just a few clicks.  

Ultimately, this project reflects the spirit of CS50: curiosity, creativity, and problem-solving.  
It’s not just about writing code — it’s about using technology to make something meaningful.

---

*This project was submitted as part of Harvard’s CS50x 2025 final project. It embodies the culmination of everything I learned in computer science fundamentals, programming, and problem-solving.*


