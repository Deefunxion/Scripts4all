import os
import re

# Ρυθμίσεις φακέλου
input_folder = "C:\\Users\\dee\\Desktop\\LLM_txt"

# Καθαρισμός ακατάληπτου κειμένου
def clean_text(text):
    text = re.sub(r'[^\x00-\x7FΑ-Ωα-ωΆΈΉΊΌΎΏάέήίόύώ\s.,;:!?()«»"]+', '', text)  # Αφαίρεση άγνωστων χαρακτήρων
    text = re.sub(r'[\t\n\r]+', '\n', text)  # Αφαίρεση πολλαπλών κενών γραμμών
    return text

# Σάρωση όλων των .txt αρχείων
for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        file_path = os.path.join(input_folder, file)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Καθαρισμός του κειμένου
            cleaned_text = clean_text(text)

            # Σπάσιμο του κειμένου στη μέση
            mid_point = len(cleaned_text) // 2
            part1 = cleaned_text[:mid_point]
            part2 = cleaned_text[mid_point:]

            # Δημιουργία νέων αρχείων
            base_name = os.path.splitext(file)[0]
            new_file1 = os.path.join(input_folder, f"{base_name}_1.txt")
            new_file2 = os.path.join(input_folder, f"{base_name}_2.txt")

            with open(new_file1, "w", encoding="utf-8") as f:
                f.write(part1)

            with open(new_file2, "w", encoding="utf-8") as f:
                f.write(part2)

            print(f"✅ {file} → {new_file1}, {new_file2}")

        except Exception as e:
            print(f"❌ Πρόβλημα με {file}: {e}")

print("\n🎉 Όλα τα αρχεία κόπηκαν στη μέση και καθαρίστηκαν!")
