import os

# Ρυθμίσεις φακέλων
input_folder = "C:\\Users\\dee\\Desktop\\LLM_txt"
output_folder = "C:\\Users\\dee\\Desktop\\LLM_txt_merged"

# Δημιουργία του output folder αν δεν υπάρχει
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Παίρνουμε όλα τα αρχεία TXT
txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

# Χωρίζουμε τα αρχεία σε ομάδες των 20 (ή λιγότερο αν είναι λίγα συνολικά)
chunk_size = max(20, len(txt_files) // 10)  # 10 μεγάλα αρχεία αν είναι πολλά
chunks = [txt_files[i:i + chunk_size] for i in range(0, len(txt_files), chunk_size)]

# Συγχώνευση κάθε ομάδας σε ένα TXT
for idx, chunk in enumerate(chunks):
    merged_text = ""
    for txt in chunk:
        txt_path = os.path.join(input_folder, txt)
        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                text = f.read()
            merged_text += f"\n\n===== ΑΡΧΕΙΟ: {txt} =====\n\n{text}"
        except Exception as e:
            print(f"❌ Πρόβλημα με {txt}: {e}")

    # Αποθήκευση του νέου TXT αρχείου
    txt_filename = os.path.join(output_folder, f"merged_{idx+1}.txt")
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(merged_text)
    print(f"✅ Δημιουργήθηκε: {txt_filename}")

print("\n🎉 Όλα τα αρχεία συγχωνεύτηκαν σε μεγαλύτερα TXT!")
