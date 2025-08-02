🏛️ Court-Data Fetcher
A simple Flask-based dashboard that fetches and displays Indian court case details by scraping real or sample HTML data from the eCourts portal. Built as part of a Python Development Internship Task.

🚀 Features
🔍 Search by Case Type, Case Number, and Year

🧾 Displays:

Petitioner & Respondent
Filing Date
Next Hearing Date
Order PDF (if available)

💻 Clean Bootstrap-styled UI

🧪 Sample cases included for testing without network

📦 Neatly organized project structure

⚠️ Why Sample HTML Was Used
Due to the following limitations on the official eCourts site, this app uses saved sample HTML files for testing:

🔐 eCourts uses dynamic dropdowns (state/district/court) via JavaScript, which cannot be auto-filled through backend requests.

⚙️ No reliable public API or URL-based form submission.

🔄 The final results page loads inside protected JS frames or via internal session handling.

🧪 Although Selenium automation was tested, it wasn’t consistent across different case types and courts.

✅ Therefore, two sample cases were created using real page structures:

Civil Suit / 233 / 2024
Warrant Case / 50 / 2024

This ensures recruiters can reliably test and evaluate the application.

📁 Folder Structure
sql
Copy
Edit
courtdata_gzb/
├── app.py                  ← Flask app
├── court_scraper.py        ← HTML parser / scraper logic
├── sample_case.html        ← Sample test case 1
├── sample_case2.html       ← Sample test case 2
├── templates/
│   ├── index.html          ← Search form page
│   └── result.html         ← Result display page
├── static/
│   └── style.css           ← Custom CSS styling
├── requirements.txt
└── README.md

🧪 Sample Test Cases
Case Type	Case Number	Filing Year
Civil Suit	233	2024
Warrant Case	50	2024

Enter these values on the homepage to test.

🛠️ Tech Stack
Python 3.13+

Flask
Jinja2 templates

BeautifulSoup (for HTML parsing)
Bootstrap 5 (for frontend)
Selenium (tested, but fallback used)

⚙️ Setup Instructions
Clone this repo:
git clone https://github.com/YOUR_USERNAME/court-data-fetcher.git
cd court-data-fetcher

Install dependencies
pip install -r requirements.txt

Run the app:
python3 app.py

Visit in browser:
http://127.0.0.1:5000

📄 requirements.txt
flask
beautifulsoup4
(Selenium not required unless you're trying full automation)

✍️ Author
Built as part of a Python Development Internship assignment.
Crafted with Anjaneya and clean code.










