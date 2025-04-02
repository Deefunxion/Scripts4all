import requests
import json
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# **API URLs**
SEARCH_API_URL = "https://searchetv99.azurewebsites.net/api/simplesearch"
VIEW_PAGE_URL = "https://search.et.gr/el/fek?fekId="  # Σελίδα προβολής ΦΕΚ

# **Ρυθμίζουμε το Selenium WebDriver**
chrome_options = Options()
chrome_options.add_argument("--headless")  # Εκτέλεση χωρίς άνοιγμα παραθύρου
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# **Διορθώνουμε το path για το Chrome WebDriver**
webdriver_path = r"C:\Users\dee\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(webdriver_path)

# **Συνάρτηση για αναγνώριση της νέας μορφής εισαγωγής**
def parse_fek_input(user_input):
    fek_pattern = re.search(r"ΦΕΚ\s*(\d+)/Τ\.(Α|Β|Γ)΄?/(\d{4})", user_input, re.IGNORECASE)

    if fek_pattern:
        fek_number, fek_issue, fek_year = fek_pattern.groups()

        # Μετατροπή του τεύχους από Α, Β, Γ στο format του API (1, 2, 3)
        issue_mapping = {'Α': '1', 'Β': '2', 'Γ': '3'}
        fek_issue_code = issue_mapping.get(fek_issue.upper(), '1')

        print(f"📄 Αναγνωρίστηκε ΦΕΚ: {fek_number} {fek_issue} {fek_year}")
        return fek_number, fek_issue_code, fek_year

    print("❌ Δεν αναγνωρίζω το αίτημά σας. Δώστε κάτι σαν 'ΦΕΚ 745/Τ.Β΄/2013'.")
    return None

# **Συνάρτηση για αναζήτηση ΦΕΚ μέσω API**
def search_fek(year, issue, fek_number):
    payload = {
        "selectYear": [str(year)],
        "selectIssue": [issue],  # Χρησιμοποιούμε "1", "2", "3"
        "documentNumber": str(fek_number),
        "searchText": "",
        "categoryIds": [],
        "datePublished": "",
        "dateReleased": "",
        "entity": [],
        "tags": []
    }

    headers = {
        "Content-Type": "application/json",
        "Origin": "https://search.et.gr",
        "Referer": "https://search.et.gr/"
    }

    print(f"\n📡 [REQUEST] Αναζητούμε ΦΕΚ {fek_number}/Τ.{issue}΄/{year} στο API...")
    response = requests.post(SEARCH_API_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        try:
            json_response = response.json()
            fek_results = json.loads(json_response["data"])

            print(f"\n✅ [RESPONSE] Βρέθηκαν {len(fek_results)} αποτελέσματα.")

            # **Ελέγχουμε κάθε αποτέλεσμα**
            for fek in fek_results:
                fek_id = fek.get("search_ID")
                fek_doc_number = fek.get("search_DocumentNumber")
                fek_issue = fek.get("search_IssueGroupID")
                fek_date = fek.get("search_IssueDate")

                # **Παίρνουμε ΜΟΝΟ το έτος από το search_IssueDate**
                fek_year = fek_date.split("/")[2].split(" ")[0] if fek_date else "N/A"

                print(f"📄 [ΕΛΕΓΧΟΣ] ΦΕΚ {fek_doc_number}/Τ.{fek_issue}΄/{fek_year} (ID: {fek_id})")

                # **Ελέγχουμε αν ταιριάζει με αυτό που ζητήσαμε**
                if fek_doc_number == fek_number and fek_issue == issue and fek_year == year:
                    print(f"✅ Βρέθηκε ακριβές ταίριασμα: ΦΕΚ {fek_number}/Τ.{issue}΄/{year} (ID: {fek_id})")
                    return fek_id

            print("❌ Δεν βρέθηκε ακριβές ταίριασμα. Το API επέστρεψε λάθος αποτελέσματα.")
            return None

        except json.JSONDecodeError:
            print("❌ Σφάλμα αποκωδικοποίησης JSON από το API.")
            return None
    else:
        print(f"❌ Σφάλμα HTTP: {response.status_code}")
        return None

# **Συνάρτηση για εξαγωγή του PDF URL μέσω Selenium**
def get_pdf_url_from_view_page(fek_id):
    url = f"{VIEW_PAGE_URL}{fek_id}"
    print(f"🔍 Ανοίγουμε τη σελίδα προβολής: {url}")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    # Περιμένουμε λίγα δευτερόλεπτα για να φορτώσει η σελίδα
    time.sleep(5)

    try:
        # **Εντοπισμός του κουμπιού "Λήψη ΦΕΚ"**
        download_button = driver.find_element(By.LINK_TEXT, "Λήψη ΦΕΚ")
        pdf_url = download_button.get_attribute("href")

        if pdf_url and pdf_url.endswith(".pdf"):
            print(f"✅ Βρέθηκε PDF URL: {pdf_url}")
            return pdf_url
        else:
            print("❌ Δεν βρέθηκε έγκυρο PDF URL.")
            return None
    except Exception as e:
        print(f"❌ Σφάλμα εντοπισμού κουμπιού: {e}")
        return None
    finally:
        driver.quit()  # Κλείνουμε το browser

# **Συνάρτηση για λήψη ΦΕΚ με σωστή ονομασία**
def download_fek(fek_id, fek_number, fek_issue, fek_year, structure):
    url = f"{VIEW_PAGE_URL}{fek_id}"
    print(f"🔍 Ανοίγουμε τη σελίδα προβολής: {url}")

    response = requests.get(url)

    if response.status_code == 200:
        print("✅ Η σελίδα προβολής άνοιξε επιτυχώς. Αναζητούμε PDF URL...")

        pdf_url_match = re.search(r"https://ia[0-9a-z]+\.blob\.core\.windows\.net/fek/.+?\.pdf", response.text)

        if pdf_url_match:
            pdf_url = pdf_url_match.group(0)
            print(f"🔗 Βρέθηκε PDF URL: {pdf_url}")

            response = requests.get(pdf_url, stream=True)
            if response.status_code == 200:
                folder_path = f"ΦΕΚ_ΑΝΑ_ΔΟΜΗ/{structure}"
                os.makedirs(folder_path, exist_ok=True)

                # **Νέο Όνομα Αρχείου**
                filename = f"{folder_path}/ΦΕΚ_{fek_number}_Τ.{fek_issue}_{fek_year}.pdf"
                print(f"📂 Αποθηκεύουμε το αρχείο ως: {filename}")

                with open(filename, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)

                print(f"✅ Το ΦΕΚ αποθηκεύτηκε επιτυχώς!")
            else:
                print(f"❌ Σφάλμα HTTP κατά τη λήψη του PDF. Status: {response.status_code}")
        else:
            print("❌ Δεν βρέθηκε το PDF URL στη σελίδα προβολής.")
    else:
        print(f"❌ Σφάλμα HTTP κατά το άνοιγμα της σελίδας προβολής. Status Code: {response.status_code}")

# **Εκτέλεση**
user_input = input("Τι θέλεις να κατεβάσω; ")
parsed_fek = parse_fek_input(user_input)

if parsed_fek:
    fek_number, fek_issue, fek_year = parsed_fek
    fek_id = search_fek(fek_year, fek_issue, fek_number)

    if fek_id:
        structure = "Γενικά ΦΕΚ"  # Αν δεν έχουμε δομή, το αποθηκεύουμε σε έναν γενικό φάκελο
        download_fek(fek_id, fek_number, fek_issue, fek_year, structure)
    else:
        print("❌ Δεν βρέθηκε το ΦΕΚ που ζητήσατε.")
else:
    print("❌ Δεν καταλαβαίνω το αίτημά σας. Παρακαλώ δώστε κάτι σαν 'ΦΕΚ 745/Τ.Β΄/2013'.")
