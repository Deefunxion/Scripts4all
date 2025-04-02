import os

# Ρυθμίσεις φακέλου
input_folder = "C:\\Users\\dee\\Desktop\\LLM_txt"

# Σάρωση όλων των υποφακέλων
for folder in os.listdir(input_folder):
    folder_path = os.path.join(input_folder, folder)

    if os.path.isdir(folder_path):  # Αν είναι φάκελος
        merged_text = ""
        txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

        if not txt_files:
            print(f"⚠️ Ο φάκελος {folder} δεν έχει αρχεία .txt, τον παραλείπουμε.")
            continue

        for txt in txt_files:
            txt_path = os.path.join(folder_path, txt)
            try:
                with open(txt_path, "r", encoding="utf-8") as f:
                    text = f.read()
                merged_text += f"\n\n===== ΑΡΧΕΙΟ: {txt} =====\n\n{text}"
            except Exception as e:
                print(f"❌ Πρόβλημα με {txt}: {e}")

        # Δημιουργία νέου μεγάλου TXT αρχείου
        final_txt_path = os.path.join(folder_path, f"{folder}_merged.txt")
        with open(final_txt_path, "w", encoding="utf-8") as f:
            f.write(merged_text)
        print(f"✅ Δημιουργήθηκε: {final_txt_path}")

print("\n🎉 Όλα τα αρχεία σε κάθε φάκελο συγχωνεύτηκαν σε ένα!")
