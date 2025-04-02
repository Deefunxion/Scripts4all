import os
import requests
import json
from cryptography.fernet import Fernet
from datetime import datetime

# 🔒 Διαχείριση Credentials με Κρυπτογράφηση
CREDENTIALS_FILE = "credentials.enc"
KEY_FILE = "secret.key"

# Ελέγχουμε αν υπάρχει ήδη κλειδί, αλλιώς δημιουργούμε
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
else:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

# Αποθήκευση credentials με κρυπτογράφηση

def save_credentials(username, password):
    credentials = json.dumps({"username": username, "password": password})
    encrypted_credentials = cipher.encrypt(credentials.encode())
    with open(CREDENTIALS_FILE, "wb") as file:
        file.write(encrypted_credentials)

# Ανάγνωση credentials

def load_credentials():
    if not os.path.exists(CREDENTIALS_FILE):
        return None
    with open(CREDENTIALS_FILE, "rb") as file:
        decrypted_data = cipher.decrypt(file.read())
        return json.loads(decrypted_data.decode())

# 🔐 Λήψη Access Token από ΙΡΙΔΑ

def get_access_token():
    return "eyJhbGciOiJSUzI1NiIsImtpZCI6IjhDRTMwOUNDQkQ5NEUwQkU5M0FGRjhBNDcwMzMwNDgwIiwidHlwIjoiYXQrand0In0.eyJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJuYmYiOjE3NDAyMjg4MjMsImlhdCI6MTc0MDIyODgyMywiZXhwIjoxNzQwMjU3NjIzLCJhdWQiOlsiYXV0aC5hcGkiLCJkZHIuYXBpIiwiaXJpcy5hcGkiXSwic2NvcGUiOlsiYXV0aF9hcGkiLCJkZHJfYXBpIiwiaXJpc19hcGkiXSwiYW1yIjpbInB3ZCJdLCJjbGllbnRfaWQiOiJpcmlzLmNsaWVudCIsInN1YiI6IjVjNGYyYzcxMWZiYWUzMjhhYzA2ZGU4MSIsImF1dGhfdGltZSI6MTc0MDIyODgyMywiaWRwIjoibG9jYWwiLCJlbXBpZCI6Ijc4MDMiLCJlbXBjYXRlZ29yeSI6IjAiLCJ1c2VybmFtZSI6ImRwYXBhZG9wb3Vsb3NAcGF0dC5nb3YuZ3IiLCJ1bml0IjoiOTIyIiwiZnVsbG5hbWUiOiJcdTAzQTBcdTAzOTFcdTAzQTBcdTAzOTFcdTAzOTRcdTAzOUZcdTAzQTBcdTAzOUZcdTAzQTVcdTAzOUJcdTAzOUZcdTAzQTMgXHUwMzk0XHUwMzk3XHUwMzlDXHUwMzk3XHUwM0E0XHUwM0ExXHUwMzk5XHUwMzlGXHUwM0EzIiwidGl0bGUiOiJcdTAzQTBcdTAzOTFcdTAzQTBcdTAzOTFcdTAzOTRcdTAzOUZcdTAzQTBcdTAzOUZcdTAzQTVcdTAzOUJcdTAzOUZcdTAzQTMgXHUwMzk0XHUwMzk3XHUwMzlDXHUwMzk3XHUwM0E0XHUwM0ExXHUwMzk5XHUwMzlGXHUwM0EzIChcdTAzQTBcdTAzOTUgXHUwMzk0XHUwMzk5XHUwMzlGXHUwMzk5XHUwMzlBXHUwMzk3XHUwM0E0XHUwMzk5XHUwMzlBXHUwMzlGXHUwM0E1IC0gXHUwMzlGXHUwMzk5XHUwMzlBXHUwMzlGXHUwMzlEXHUwMzlGXHUwMzlDXHUwMzk5XHUwMzlBXHUwMzlGXHUwM0E1LCBcdTAzOTEpIiwicHJvZmlsZSI6WyIxMzE0LTkiLCIxMzE1LTI1Il0sImp0aSI6IjIxQjE3Mzg2NkFGMTc2N0Y5QzA5NjNFRDdFMzhDMDA2In0.Ykn2qclyganGocGxwAShDYHo4Q1-zT1-wWDPy1aa9NP59ZcKWDR5x4kQ_BaseCt4CHjMTYjpoWRdH2BD6ykN9GfZZ7oga_EAAN9U-WOAAs1Rf7q2uBuHA683RCXdREZjQLGGa-Jp9TEM0OxRUK9O3TzX7LGbHAPWFU8viVRJaFg7zcmoIIH_XdAz9uYmJzVxqokqb_5mTRtc7aoG8_va2I10Sp_RoXUEMq3RqD6Xsj2a7h_oPTeLeXtd9k2LExGjyt0dsyNuVpKj1Xr61bDDUcR6QYa7cxIS-pZVk28YmG16YtK-gx9KryNIHAmDUCXsg3Y4GC8vFtGtsPD9jd6QvQ"  # Βάλε εδώ το token που βρήκες από το Network του Browser
    if not credentials:
        print("❌ Δεν υπάρχουν αποθηκευμένα credentials!")
        return None
    
    payload = {
        "grant_type": "password",
        "client_id": "iris.client",
        "client_secret": "21B5F798-BE55-42BC-8AA8-0025B893DC3B",
        "username": credentials["username"],
        "password": credentials["password"],
        "scope": "iris_api ddr_api auth_api"
    }
    
    response = requests.post("https://iridacloud.gov.gr/auth/connect/token", data=payload, verify=False)
    
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("❌ Αποτυχία στη λήψη token:", response.text)
        return None

# 📥 Λήψη εισερχόμενων εγγράφων

def fetch_pending_documents(limit=10):
    """ Ανακτά τα τελευταία εκκρεμή έγγραφα για ενέργεια """
    token = get_access_token()
    if not token:
        return []

    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get("https://iridacloud.gov.gr/iris/api/v2/external/inbox/false", headers=headers, verify=False)

    if response.status_code == 200:
        all_documents = response.json()

        # 🔍 Φιλτράρουμε μόνο τα έγγραφα που είναι "Για Ενέργεια"
        pending_documents = [doc for doc in all_documents if "Για Ενέργεια" in doc.get("title", "")]

        # 🔢 Παίρνουμε μόνο τα 10 πιο πρόσφατα
        return pending_documents[:limit]

    else:
        print("❌ Αποτυχία στη λήψη εγγράφων:", response.text)
        return []


# 📂 Λήψη αρχείων για κάθε έγγραφο

def download_files_for_document(document_id):
    token = get_access_token()
    if not token:
        return
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"https://iridacloud.gov.gr/iris/api/v2/external/document/{document_id}/files", headers=headers, verify=False)
    
    if response.status_code == 200:
        files = response.json().get("files", [])
        os.makedirs("downloads", exist_ok=True)
        
        for file in files:
            file_url = file.get("download_url")
            filename = file.get("Description")
            file_response = requests.get(file_url, headers=headers, stream=True)
            
            if file_response.status_code == 200:
                with open(f"downloads/{filename}", "wb") as f:
                    for chunk in file_response.iter_content(1024):
                        f.write(chunk)
                print(f"✅ Κατέβηκε το αρχείο: {filename}")
            else:
                print(f"❌ Αποτυχία στο κατέβασμα του αρχείου {filename}")
    else:
        print("❌ Σφάλμα κατά την ανάκτηση αρχείων:", response.text)

# 📝 Περίληψη θεμάτων της ημέρας (Placeholder για NLP)

def summarize_documents(documents):
    summaries = []
    for doc in documents:
        title = doc.get("title", "Χωρίς τίτλο")
        regNo = doc.get("regNo", "-")
        summaries.append(f"📌 {title} (Πρωτόκολλο: {regNo})")
    return "\n".join(summaries)

# 📌 Κύρια εκτέλεση
if __name__ == "__main__":
    print("🔐 Ρύθμιση Credentials (μόνο την πρώτη φορά)")
    if not os.path.exists(CREDENTIALS_FILE):
        username = input("Εισάγετε το email σας: ")
        password = input("Εισάγετε τον κωδικό σας: ")
        save_credentials(username, password)
    
    print("📥 Ανάκτηση εισερχομένων...")
    documents = fetch_pending_documents()
    if not documents:
        print("⚠ Δεν βρέθηκαν νέα έγγραφα.")
    else:
        print("📝 Περίληψη ημερήσιων θεμάτων:")
        print(summarize_documents(documents))
        
        print("⬇ Κατέβασμα αρχείων...")
        for doc in documents:
            download_files_for_document(doc["documentId"])
