import os
import re
import pandas as pd
from collections import defaultdict

# Categorize files based on keywords
def categorize_files(input_folder, output_folder, categories):
    os.makedirs(output_folder, exist_ok=True)
    categorized_data = defaultdict(list)

    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            category = "Άλλο"
            for cat, keywords in categories.items():
                if any(re.search(keyword, file, re.IGNORECASE) for keyword in keywords):
                    category = cat
                    break
            category_folder = os.path.join(output_folder, category)
            os.makedirs(category_folder, exist_ok=True)
            os.rename(file_path, os.path.join(category_folder, file))
            categorized_data[category].append(file)
            print(f"✅ Categorized: {file} → {category}")

    return categorized_data

# Index categorized files into an Excel sheet
def index_files(output_folder, excel_path):
    data = []
    for root, _, files in os.walk(output_folder):
        for file in files:
            file_path = os.path.join(root, file)
            data.append({"Category": os.path.basename(root), "Filename": file, "Path": file_path})

    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False)
    print(f"✅ Indexed: {excel_path}")

# Example usage
if __name__ == "__main__":
    input_folder = r"C:\Users\dee\Desktop\organize_txt"
    output_folder = r"C:\Users\dee\Desktop\organized_files"
    excel_path = r"C:\Users\dee\Desktop\organized_files_index.xlsx"

    categories = {
        "Δημόσια Διοίκηση": ["διοίκηση", "Ν. 2690/1999"],
        "Προμήθειες & Συμβάσεις": ["σύμβαση", "Ν. 4412/2016"],
        "Άλλο": []
    }

    categorized_data = categorize_files(input_folder, output_folder, categories)
    index_files(output_folder, excel_path)
