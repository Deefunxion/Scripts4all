import re
from pathlib import Path

INPUT_PATH = r"C:\Users\dee\Desktop\N.2690.txt"
OUTPUT_PATH = r"C:\Users\dee\Desktop\dms4llms\superbasicdms/N_2690_1999_clean.md"

# Ensure output directory exists
Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)

# Φόρτωσε το αρχείο
text = Path(INPUT_PATH).read_text(encoding="utf-8", errors="ignore")

# Αφαίρεσε άχρηστα metadata
text = re.sub(r"(?i)Σύνδεση με Νομολογία.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)
text = re.sub(r"(?i)Κατά εξουσιοδότηση.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)
text = re.sub(r"(?i)Προισχύσασες μορφές άρθρου.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)
text = re.sub(r"(?i)ΑΙΤΙΟΛΟΓΙΚΗ ΕΚΘΕΣΗ.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)
text = re.sub(r"(?i)\*\*\*.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)  # Τροποποιήσεις τύπου *** Το άρθρο

# Σπάσε το σε άρθρα
articles = re.split(r"\n+\s*Αρθρο\s+(\d+)\s*\n+", text)

output_lines = []
output_lines.append("# Νόμος 2690/1999 – Κώδικας Διοικητικής Διαδικασίας\n")

for i in range(1, len(articles), 2):
    number = articles[i].strip()
    content = articles[i + 1].strip()

    # Πετάμε άσχετα άρθρα τύπου "Αρθρο 1 – Αρθρογραφία"
    if re.match(r"(?i)αρθρογραφία|σχόλια|σχετική βιβλιογραφία", content):
        continue

    # Απόσπασε τίτλο αν υπάρχει
    match = re.match(r"([Α-Ω].*?)\n+", content)
    if match:
        title = match.group(1).strip()
        content_body = content[match.end():].strip()
    else:
        title = ""
        content_body = content

    # Καθαρισμός διπλών κενών
    content_body = re.sub(r"\n{3,}", "\n\n", content_body)

    output_lines.append(f"## Άρθρο {number} – {title}\n")
    output_lines.append(content_body)
    output_lines.append("\n---\n")

# Αποθήκευσε το markdown
Path(OUTPUT_PATH).write_text("\n\n".join(output_lines), encoding="utf-8")
print(f"✅ Καθαρό .md αρχείο αποθηκεύτηκε: {OUTPUT_PATH}")
