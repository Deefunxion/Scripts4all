import re
from pathlib import Path

# Καθορισμός φακέλων εισόδου και εξόδου
INPUT_DIR = Path(r"C:\Users\dee\Desktop\input_txt_files")
OUTPUT_DIR = Path(r"C:\Users\dee\Desktop\dms4llms\superbasicdms\output_md_files")

# Δημιουργία φακέλου εξόδου αν δεν υπάρχει
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def clean_and_convert_to_md(file_path: Path) -> None:
    """Καθαρίζει ένα .txt αρχείο και το μετατρέπει σε .md"""
    try:
        # Φόρτωση του αρχείου με χειρισμό σφαλμάτων κωδικοποίησης
        text = file_path.read_text(encoding="utf-8", errors="ignore")

        # Αφαίρεση άχρηστων metadata και σχολίων
        text = re.sub(r"(?i)Σύνδεση με Νομολογία.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)
        text = re.sub(r"(?i)Κατά εξουσιοδότηση.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)
        text = re.sub(r"(?i)Προισχύσασες μορφές άρθρου.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)
        text = re.sub(r"(?i)ΑΙΤΙΟΛΟΓΙΚΗ ΕΚΘΕΣΗ.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)
        text = re.sub(r"(?i)\*\*\*.*?(?=Αρθρο|\Z)", "", text, flags=re.DOTALL)

        # Εύρεση τίτλου νόμου (πρώτη γραμμή συνήθως)
        title_match = re.search(r"^(.+?)(?=\n)", text)
        law_title = title_match.group(1).strip() if title_match else "Χωρίς Τίτλο"

        # Σπάσιμο σε άρθρα
        articles = re.split(r"\n+\s*Αρθρο\s+([^\n]+)\s*\n+", text)
        output_lines = [f"# {law_title}\n"]

        # Επεξεργασία κάθε άρθρου
        for i in range(1, len(articles), 2):
            number = articles[i].strip()
            content = articles[i + 1].strip()

            # Παράλειψη άσχετων άρθρων
            if re.match(r"(?i)αρθρογραφία|σχόλια|σχετική βιβλιογραφία", content):
                continue

            # Εξαγωγή τίτλου άρθρου αν υπάρχει
            match = re.match(r"([Α-Ω].*?)\n+", content)
            if match:
                article_title = match.group(1).strip()
                content_body = content[match.end():].strip()
            else:
                article_title = ""
                content_body = content

            # Καθαρισμός υπερβολικών κενών
            content_body = re.sub(r"\n{3,}", "\n\n", content_body)

            # Προσθήκη στο output
            output_lines.append(f"## Άρθρο {number} – {article_title}\n")
            output_lines.append(content_body)
            output_lines.append("\n---\n")

        # Αποθήκευση ως .md
        output_file = OUTPUT_DIR / f"{file_path.stem}_clean.md"
        output_file.write_text("\n".join(output_lines), encoding="utf-8")
        print(f"✅ Επεξεργάστηκε: {file_path.name} -> {output_file.name}")

    except Exception as e:
        print(f"❌ Σφάλμα κατά την επεξεργασία του {file_path.name}: {str(e)}")

# Επεξεργασία όλων των .txt αρχείων στον φάκελο εισόδου
for txt_file in INPUT_DIR.glob("*.txt"):
    clean_and_convert_to_md(txt_file)

print(f"✅ Ολοκληρώθηκε η επεξεργασία όλων των αρχείων στο {INPUT_DIR}")