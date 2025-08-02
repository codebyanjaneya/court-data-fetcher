from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def fetch_case_details(case_type, case_number, case_year):
    try:
        # Set up headless Chrome
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

        # Open the Ghaziabad eCourts search page directly
        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index")

        # Select State: Uttar Pradesh
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sess_state_code"))).send_keys("Uttar Pradesh")
        time.sleep(2)

        # Select District: Ghaziabad
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sess_dist_code"))).send_keys("Ghaziabad")
        time.sleep(2)

        # Click on Case Number tab
        driver.find_element(By.ID, "case_no_tab").click()

        # Fill in the form
        driver.find_element(By.NAME, "case_type").send_keys(case_type)
        driver.find_element(By.NAME, "case_number").send_keys(case_number)
        driver.find_element(By.NAME, "case_year").send_keys(case_year)

        # Submit
        driver.find_element(By.ID, "submitBtn").click()

        # Wait for results to load
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "caseStatusDetails")))

        html = driver.page_source
        driver.quit()

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Find petitioner and respondent from result (basic example)
        case_info = soup.find("div", {"id": "caseStatusDetails"})
        parties = case_info.text.split("Versus")
        petitioner = parties[0].strip() if len(parties) > 0 else "Not found"
        respondent = parties[1].strip() if len(parties) > 1 else "Not found"

        result = {
            "case_type": case_type,
            "case_number": case_number,
            "case_year": case_year,
            "petitioner": petitioner,
            "respondent": respondent,
            "filing_date": "Not available",
            "next_hearing": "Not available",
            "pdf_link": None
        }

        return result, html

    except Exception as e:
        print("❌ Error during Selenium fetch:", e)
        return None, None
