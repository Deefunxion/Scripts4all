import os

# 🔹 Ρύθμιση αρχείων
input_file = r"C:\Users\dee\Desktop\cleaned_data.jsonl"
output_folder = r"C:\Users\dee\Desktop\cleaned_jsonl_parts"
chunk_size = 20  # Πόσα entries ανά αρχείο

# 🔹 Δημιουργία φακέλου εξόδου αν δεν υπάρχει
os.makedirs(output_folder, exist_ok=True)

# 🔹 Διαβάζουμε το JSONL αρχείο
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 🔹 Σπάμε το JSONL σε μικρότερα κομμάτια
total_parts = (len(lines) // chunk_size) + (1 if len(lines) % chunk_size > 0 else 0)

for i in range(total_parts):
    part_filename = os.path.join(output_folder, f"cleaned_part{i+1}.jsonl")
    with open(part_filename, "w", encoding="utf-8") as part_file:
        part_file.writelines(lines[i * chunk_size:(i + 1) * chunk_size])
    print(f"✅ Αποθηκεύτηκε: {part_filename}")

print("🎉 Ο διαχωρισμός ολοκληρώθηκε! Τα αρχεία αποθηκεύτηκαν στον φάκελο 'cleaned_jsonl_parts'.")
