# Python Utilities for File Management, Processing, and Conversion

This repository contains a collection of Python scripts designed to handle various tasks such as file organization, text extraction, JSON processing, PDF conversion, and more. Below is an analytical overview of each script to help users understand its purpose and usage.

---

## Table of Contents

1. [Splitters](#splitters)
2. [Organizers](#organizers)
3. [Mergers](#mergers)
4. [Indexers](#indexers)
5. [Extractors](#extractors)
6. [Converters](#converters)
7. [Cleaners](#cleaners)
8. [Collaborations](#collaborations)
9. [Miscellaneous](#miscellaneous)

---

## Splitters

### `split_jsonl.py`
- **Purpose**: Splits a large `.jsonl` file into smaller chunks based on a specified number of entries per file.
- **Usage**: Modify the `input_file`, `output_folder`, and `chunk_size` variables to customize the splitting process.

### `split_json.py`
- **Purpose**: Splits a `.json` file into smaller `.json` files, each containing a specified number of records.
- **Usage**: Set the `input_file`, `chunk_size`, and `output_folder` variables to configure the splitting.

### `split_and_clean_txt.py`
- **Purpose**: Cleans and splits `.txt` files into two parts, removing unwanted characters and formatting issues.
- **Usage**: Place `.txt` files in the `input_folder` and run the script.

---

## Organizers

### `organize_txt.py`
- **Purpose**: Categorizes `.txt` files into folders based on keywords and splits large files into smaller ones.
- **Usage**: Define the `folder_path` and customize the `categorize_text` function with relevant keywords.

### `organize_files.py`
- **Purpose**: Organizes files and folders into predefined categories based on their names.
- **Usage**: Place files in the `desktop_path` and run the script.

### `organize_files_smart.py`
- **Purpose**: Reads the content of files (PDF, DOCX, TXT, XLSX) and categorizes them based on keywords.
- **Usage**: Place files in the `desktop_path` and run the script.

---

## Mergers

### `merge_txt.py`
- **Purpose**: Merges multiple `.txt` files into larger files, grouping them into chunks.
- **Usage**: Place `.txt` files in the `input_folder` and set the `output_folder`.

### `merge_txt_per_folder.py`
- **Purpose**: Merges all `.txt` files in each subfolder into a single file per folder.
- **Usage**: Place subfolders with `.txt` files in the `input_folder`.

### `merge_selected_txt.py`
- **Purpose**: Merges specific `.txt` files into a single file based on predefined groups.
- **Usage**: Define the `groups` dictionary with file names to merge.

### `merge_jsonl.py`
- **Purpose**: Merges multiple `.json` files into a single `.jsonl` file.
- **Usage**: Place `.json` files in the `input_folder` and set the `output_file`.

---

## Indexers

### `indexerwordmax.py`
- **Purpose**: Extracts text from `.doc` and `.docx` files, processes the first half of the content, and saves results in an Excel file.
- **Usage**: Place Word files in the `folder_path`.

### `indexermax.py`
- **Purpose**: Extracts text from the first page of PDF files, processes the first half of the content, and saves results in an Excel file.
- **Usage**: Place PDF files in the `folder_path`.

### `indexer.py`
- **Purpose**: Similar to `indexermax.py`, but focuses on processing all PDF files in a folder.
- **Usage**: Place PDF files in the `folder_path`.

---

## Extractors

### `extract_subject.py`
- **Purpose**: Extracts the "ΘΕΜΑ" (subject) from PDF files and saves the results in a CSV file.
- **Usage**: Place PDF files in the `folder_path`.

### `extract_subject_rename.py`
- **Purpose**: Extracts the "ΘΕΜΑ" from PDF files, renames the files based on the extracted subject, and saves results in a CSV file.
- **Usage**: Place PDF files in the `folder_path`.

### `extract_subject_rename_fek.py`
- **Purpose**: Extracts metadata (e.g., "ΦΕΚ" number, year) from PDF files and renames them accordingly.
- **Usage**: Place PDF files in the `folder_path`.

---

## Converters

### `convert_to_jsonl1.py`
- **Purpose**: Converts multiple `.json` files into a single `.jsonl` file.
- **Usage**: Place `.json` files in the `input_folder`.

### `convert_to_jsonl.py`
- **Purpose**: Converts various file formats (PDF, DOCX, TXT) into a `.json` file.
- **Usage**: Place files in the `input_folder`.

### `convert_pdfs_to_txt.py`
- **Purpose**: Converts PDF files to `.txt` format using OCR if necessary.
- **Usage**: Place PDF files in the `PDF_FOLDER`.

### `convert_local.py`
- **Purpose**: Similar to `convert_to_jsonl.py`, but focuses on local file processing.
- **Usage**: Place files in the `input_folder`.

### `convert_documents.py`
- **Purpose**: Converts PDF, DOCX, and DOC files to `.txt` format.
- **Usage**: Place files in the `input_folder`.

---

## Cleaners

### `clean_txt_fek.py`
- **Purpose**: Cleans `.txt` files by removing metadata and formatting them into Markdown files.
- **Usage**: Place `.txt` files in the `INPUT_DIR`.

### `clean_text.py`
- **Purpose**: Cleans a single `.txt` file and converts it into a Markdown file.
- **Usage**: Set the `INPUT_PATH` and `OUTPUT_PATH`.

### `clean_json.py`
- **Purpose**: Cleans `.json` files by removing unnecessary fields and formatting issues.
- **Usage**: Place `.json` files in the `input_folder`.

---

## Collaborations

### `split_process_merge_jsonl.py`
- **Purpose**: Splits a large `.jsonl` file, processes each chunk, and merges the results back into a single file.
- **Usage**: Set the `input_file`, `split_folder`, `processed_folder`, and `output_file`.

### `organize_and_index.py`
- **Purpose**: Categorizes files into folders based on keywords and creates an Excel index.
- **Usage**: Place files in the `input_folder`.

---

## Miscellaneous

### `sort_files_offline.py`
- **Purpose**: Categorizes files and folders based on their names without using an API.
- **Usage**: Place files in the `desktop_path`.

### `irida_script.py`
- **Purpose**: Interacts with the IRIDA API to fetch and process documents.
- **Usage**: Configure credentials and API endpoints.

### `importtext.py`
- **Purpose**: Extracts text from the first page of a PDF file using OCR if necessary.
- **Usage**: Set the `pdf_path`.

### `fix_json.py`
- **Purpose**: Fixes JSON formatting issues in a single file.
- **Usage**: Set the `input_file` and `output_file`.

### `create_index.py`
- **Purpose**: Creates an index of cleaned JSON files with metadata and sample records.
- **Usage**: Place `.json` files in the `cleaned_folder`.

---
## Notes

- Ensure all dependencies are installed before running the scripts.
- Modify file paths and parameters as needed for your specific use case.
- For OCR-related scripts, ensure Tesseract and Poppler are correctly installed and configured.
