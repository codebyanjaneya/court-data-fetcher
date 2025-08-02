print("✅ app.py is being executed...")

from flask import Flask, render_template, request, redirect
from court_scraper import fetch_case_details
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
print("Flask app started...")


# Ensure the database exists
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            case_year TEXT,
            timestamp TEXT,
            raw_html TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        case_year = request.form['case_year']

        print("📥 Received input:")
        print("Case Type:", case_type)
        print("Case Number:", case_number)
        print("Case Year:", case_year)
  
        details, raw_html = fetch_case_details(case_type, case_number, case_year)
        

        # Save log
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO logs (case_type, case_number, case_year, timestamp, raw_html)
            VALUES (?, ?, ?, ?, ?)
        """, (case_type, case_number, case_year, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), raw_html))
        conn.commit()
        conn.close()

        if details:
            return render_template('result.html', details=details)
        else:
            return render_template('index.html', error="Case not found or website error.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
