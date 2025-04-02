import json
import os

# 🔹 Φάκελος με τα cleaned JSON αρχεία
input_folder = r"C:\Users\dee\Desktop\cleaned_json"
output_file = r"C:\Users\dee\Desktop\cleaned_data.jsonl"

# 🔹 Δημιουργία/καθαρισμός του JSONL αρχείου
with open(output_file, "w", encoding="utf-8") as jsonl_out:
    # Διατρέχουμε όλα τα JSON αρχεία στον φάκελο
    for file in os.listdir(input_folder):
        if file.startswith("cleaned_converted_part") and file.endswith(".json"):
            file_path = os.path.join(input_folder, file)

            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    if not data:
                        print(f"⚠️ Προσοχή! Το αρχείο {file} είναι άδειο.")
                        continue
                except json.JSONDecodeError as e:
                    print(f"⚠️ Σφάλμα JSON στο {file}: {e}")
                    continue

            # 🔹 Μετατροπή κάθε εγγραφής σε JSONL format (μία εγγραφή ανά γραμμή)
            for entry in data:
                jsonl_out.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"✅ Μετατροπή ολοκληρώθηκε! Το JSONL αποθηκεύτηκε στο: {output_file}")
