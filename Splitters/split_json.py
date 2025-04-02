import json
import os

# 🔹 Ρύθμιση αρχείων
input_file = r"C:\Users\dee\Desktop\converted_data.json"  # Αρχικό JSON
chunk_size = 100  # Ορισμένο μέγεθος αρχείου
output_folder = r"C:\Users\dee\Desktop"  # Φάκελος αποθήκευσης

# 🔹 Φόρτωση του JSON αρχείου
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 🔹 Εμφάνιση του συνολικού αριθμού των εγγραφών
total_records = len(data)
print(f"📌 Το αρχείο περιέχει {total_records} αρχεία.")

# 🔹 Δημιουργία των νέων JSON αρχείων
file_count = 0
for i in range(0, total_records, chunk_size):
    file_count += 1
    chunk = data[i:i + chunk_size]  # Παίρνουμε το αντίστοιχο κομμάτι των εγγραφών
    output_file = os.path.join(output_folder, f"converted_part{file_count}.json")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunk, f, ensure_ascii=False, indent=4)

    print(f"✅ Αποθηκεύτηκε: {output_file}")

print(f"🎉 Ο διαχωρισμός ολοκληρώθηκε! Δημιουργήθηκαν {file_count} αρχεία.")
