import os

# Ρυθμίσεις φακέλων
input_folder = "C:\\Users\\dee\\Desktop\\LLM_txt_merged"
output_folder = "C:\\Users\\dee\\Desktop\\LLM_txt_final"

# Δημιουργία του output folder αν δεν υπάρχει
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Ομάδες αρχείων που θα συγχωνεύσουμε
groups = {
    "final_1.txt": ["merged_11.txt", "merged_6.txt", "merged_7.txt", "merged_2.txt"],
    "final_2.txt": ["merged_10.txt", "merged_3.txt"]
}

# Συγχώνευση αρχείων
for output_file, files in groups.items():
    merged_text = ""
    for file in files:
        txt_path = os.path.join(input_folder, file)
        if os.path.exists(txt_path):
            try:
                with open(txt_path, "r", encoding="utf-8") as f:
                    text = f.read()
                merged_text += f"\n\n===== ΑΡΧΕΙΟ: {file} =====\n\n{text}"
            except Exception as e:
                print(f"❌ Πρόβλημα με {file}: {e}")
        else:
            print(f"⚠️ Το αρχείο {file} δεν βρέθηκε.")

    # Αποθήκευση του νέου TXT αρχείου
    final_path = os.path.join(output_folder, output_file)
    with open(final_path, "w", encoding="utf-8") as f:
        f.write(merged_text)
    print(f"✅ Δημιουργήθηκε: {final_path}")

print("\n🎉 Η συγχώνευση ολοκληρώθηκε!")
