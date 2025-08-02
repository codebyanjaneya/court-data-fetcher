from bs4 import BeautifulSoup

def fetch_case_details(case_type, case_number, case_year):
    try:
        # Expand common abbreviations
        case_type_map = {
            "CS": "Civil Suit",
            "WC": "Warrant Case",
            "CR": "Criminal Revision",
            "CC": "Civil Complaint"
        }

        # Normalize case type
        case_type_expanded = case_type_map.get(case_type.upper(), case_type)

        # Select appropriate HTML sample file
        if case_type_expanded == "Civil Suit" and case_number == "233" and case_year == "2024":
            html_file = "sample_case.html"
        elif case_type_expanded == "Warrant Case" and case_number == "50" and case_year == "2024":
            html_file = "sample_case2.html"
        else:
            html_file = "sample_case.html"  # fallback

        with open(html_file, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("tr")

        expected_string = f"{case_type_expanded}/{case_number}/{case_year}".lower().replace(" ", "")
        print("🔍 Looking for:", expected_string)

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                case_text = cols[1].text.strip().lower().replace(" ", "")
                print("🔎 Found:", case_text)
                if expected_string in case_text:
                    print("✅ Match found. Extracting parties.")

                    try:
                        parties = cols[2].text.strip().split("Versus")
                        petitioner = parties[0].strip() if len(parties) > 0 else "Not found"
                        respondent = parties[1].strip() if len(parties) > 1 else "Not found"
                    except Exception as e:
                        print("❌ Error parsing parties:", e)
                        petitioner = "Not found"
                        respondent = "Not found"

                    result = {
                        "case_type": case_type_expanded,
                        "case_number": case_number,
                        "case_year": case_year,
                        "petitioner": petitioner,
                        "respondent": respondent,
                        "filing_date": "Not available",
                        "next_hearing": "Not available",
                        "pdf_link": None
                    }

                    return result, html

        print("❌ No matching case row found.")
        return None, None

    except Exception as e:
        print("❌ Error during parsing:", e)
        return None, None
