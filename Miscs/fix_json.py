import json

# 🔹 Ρύθμιση αρχείου
input_file = r"C:\Users\dee\Desktop\cleaned_json\cleaned_converted_part1.json"
output_file = r"C:\Users\dee\Desktop\cleaned_json\fixed_converted_part1.json"

fixed_data = []
with open(input_file, "r", encoding="utf-8") as f:
    try:
        data = json.load(f)
        fixed_data = data  # Αν διαβαστεί σωστά, το αποθηκεύουμε κανονικά
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON Error: {e}")

# 🔹 Αποθήκευση διορθωμένου JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(fixed_data, f, ensure_ascii=False, indent=4)

print(f"✅ Το καθαρισμένο JSON αποθηκεύτηκε στο: {output_file}")
