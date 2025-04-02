import os
import json

# Split a large JSONL file into smaller chunks
def split_jsonl(input_file, output_folder, chunk_size):
    os.makedirs(output_folder, exist_ok=True)
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_parts = (len(lines) // chunk_size) + (1 if len(lines) % chunk_size > 0 else 0)
    for i in range(total_parts):
        part_filename = os.path.join(output_folder, f"part_{i+1}.jsonl")
        with open(part_filename, "w", encoding="utf-8") as part_file:
            part_file.writelines(lines[i * chunk_size:(i + 1) * chunk_size])
        print(f"✅ Split: {part_filename}")

# Process each chunk (e.g., clean the content)
def process_jsonl_chunks(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(input_folder):
        if file.endswith(".jsonl"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, f"cleaned_{file}")
            with open(input_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            cleaned_lines = []
            for line in lines:
                try:
                    data = json.loads(line)
                    # Example cleaning: Remove empty fields
                    data = {k: v for k, v in data.items() if v}
                    cleaned_lines.append(json.dumps(data, ensure_ascii=False) + "\n")
                except json.JSONDecodeError:
                    print(f"⚠️ Skipping invalid JSON line in {file}")

            with open(output_path, "w", encoding="utf-8") as f:
                f.writelines(cleaned_lines)
            print(f"✅ Processed: {output_path}")

# Merge processed chunks back into a single JSONL file
def merge_jsonl(input_folder, output_file):
    with open(output_file, "w", encoding="utf-8") as jsonl_out:
        for file in os.listdir(input_folder):
            if file.endswith(".jsonl"):
                input_path = os.path.join(input_folder, file)
                with open(input_path, "r", encoding="utf-8") as f:
                    jsonl_out.writelines(f.readlines())
    print(f"✅ Merged: {output_file}")

# Example usage
if __name__ == "__main__":
    input_file = r"C:\Users\dee\Desktop\cleaned_data.jsonl"
    split_folder = r"C:\Users\dee\Desktop\split_jsonl_parts"
    processed_folder = r"C:\Users\dee\Desktop\processed_jsonl_parts"
    output_file = r"C:\Users\dee\Desktop\final_cleaned_data.jsonl"

    chunk_size = 20
    split_jsonl(input_file, split_folder, chunk_size)
    process_jsonl_chunks(split_folder, processed_folder)
    merge_jsonl(processed_folder, output_file)
