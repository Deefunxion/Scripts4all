
import os

def split_folder_to_chunks(folder_path, max_chunks=4):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    txt_files.sort()
    
    chunk_size = len(txt_files) // max_chunks
    remainder = len(txt_files) % max_chunks

    chunks = []
    start = 0
    for i in range(max_chunks):
        end = start + chunk_size + (1 if i < remainder else 0)
        chunks.append(txt_files[start:end])
        start = end

    for i, chunk in enumerate(chunks):
        output_file = os.path.join(folder_path, f'chunk_{i+1}.txt')
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for fname in chunk:
                file_path = os.path.join(folder_path, fname)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(f"--- FILE: {fname} ---\\n")
                    outfile.write(infile.read())
                    outfile.write("\\n\\n")

# Corrected Windows paths with raw strings
folders = [
    r'C:\Users\dee\Desktop\ΔΙΑΦΟΡΕΣ ΕΦΑΡΜΟΓΕΣ\just-text-main\just-text-main\2021',
    r'C:\Users\dee\Desktop\ΔΙΑΦΟΡΕΣ ΕΦΑΡΜΟΓΕΣ\just-text-main\just-text-main\2022',
    r'C:\Users\dee\Desktop\ΔΙΑΦΟΡΕΣ ΕΦΑΡΜΟΓΕΣ\just-text-main\just-text-main\2023',
    r'C:\Users\dee\Desktop\ΔΙΑΦΟΡΕΣ ΕΦΑΡΜΟΓΕΣ\just-text-main\just-text-main\2024'
]

for folder in folders:
    split_folder_to_chunks(folder)
