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

Βοηθήματα Python για Διαχείριση, Επεξεργασία και Μετατροπή Αρχείων
Αυτό το αποθετήριο περιέχει μια συλλογή από scripts Python σχεδιασμένα για να χειρίζονται διάφορες εργασίες όπως οργάνωση αρχείων, εξαγωγή κειμένου, επεξεργασία JSON, μετατροπή PDF και άλλα. Παρακάτω είναι μια αναλυτική επισκόπηση κάθε script για να βοηθήσει τους χρήστες να κατανοήσουν τον σκοπό και τη χρήση του.

# Πίνακας Περιεχομένων

- [Διαχωριστές](#διαχωριστές)
- [Οργανωτές](#οργανωτές)
- [Συγχωνευτές](#συγχωνευτές)
- [Ευρετηριαστές](#ευρετηριαστές)
- [Εξαγωγείς](#εξαγωγείς)
- [Μετατροπείς](#μετατροπείς)
- [Καθαριστές](#καθαριστές)
- [Συνεργασίες](#συνεργασίες)
- [Διάφορα](#διάφορα)

---

## Διαχωριστές

### `split_jsonl.py`
**Σκοπός**: Διαχωρίζει ένα μεγάλο αρχείο `.jsonl` σε μικρότερα κομμάτια βάσει ενός καθορισμένου αριθμού εγγραφών ανά αρχείο.  
**Χρήση**: Τροποποιήστε τις μεταβλητές `input_file`, `output_folder` και `chunk_size` για να προσαρμόσετε τη διαδικασία διαχωρισμού.

### `split_json.py`
**Σκοπός**: Διαχωρίζει ένα αρχείο `.json` σε μικρότερα αρχεία `.json`, καθένα από τα οποία περιέχει έναν καθορισμένο αριθμό εγγραφών.  
**Χρήση**: Ορίστε τις μεταβλητές `input_file`, `chunk_size` και `output_folder` για να διαμορφώσετε τον διαχωρισμό.

### `split_and_clean_txt.py`
**Σκοπός**: Καθαρίζει και διαχωρίζει αρχεία `.txt` σε δύο μέρη, αφαιρώντας ανεπιθύμητους χαρακτήρες και προβλήματα μορφοποίησης.  
**Χρήση**: Τοποθετήστε αρχεία `.txt` στον φάκελο `input_folder` και εκτελέστε το script.

---

## Οργανωτές

### `organize_txt.py`
**Σκοπός**: Κατηγοριοποιεί αρχεία `.txt` σε φακέλους βάσει λέξεων-κλειδιών και διαχωρίζει μεγάλα αρχεία σε μικρότερα.  
**Χρήση**: Ορίστε τη διαδρομή `folder_path` και προσαρμόστε τη συνάρτηση `categorize_text` με σχετικές λέξεις-κλειδιά.

### `organize_files.py`
**Σκοπός**: Οργανώνει αρχεία και φακέλους σε προκαθορισμένες κατηγορίες βάσει των ονομάτων τους.  
**Χρήση**: Τοποθετήστε αρχεία στη διαδρομή `desktop_path` και εκτελέστε το script.

### `organize_files_smart.py`
**Σκοπός**: Διαβάζει το περιεχόμενο αρχείων (PDF, DOCX, TXT, XLSX) και τα κατηγοριοποιεί βάσει λέξεων-κλειδιών.  
**Χρήση**: Τοποθετήστε αρχεία στη διαδρομή `desktop_path` και εκτελέστε το script.

---

## Συγχωνευτές

### `merge_txt.py`
**Σκοπός**: Συγχωνεύει πολλαπλά αρχεία `.txt` σε μεγαλύτερα αρχεία, ομαδοποιώντας τα σε κομμάτια.  
**Χρήση**: Τοποθετήστε αρχεία `.txt` στον φάκελο `input_folder` και ορίστε τον φάκελο `output_folder`.

### `merge_txt_per_folder.py`
**Σκοπός**: Συγχωνεύει όλα τα αρχεία `.txt` σε κάθε υποφάκελο σε ένα ενιαίο αρχείο ανά φάκελο.  
**Χρήση**: Τοποθετήστε υποφακέλους με αρχεία `.txt` στον φάκελο `input_folder`.

### `merge_selected_txt.py`
**Σκοπός**: Συγχωνεύει συγκεκριμένα αρχεία `.txt` σε ένα ενιαίο αρχείο βάσει προκαθορισμένων ομάδων.  
**Χρήση**: Ορίστε το λεξικό `groups` με τα ονόματα των αρχείων προς συγχώνευση.

### `merge_jsonl.py`
**Σκοπός**: Συγχωνεύει πολλαπλά αρχεία `.json` σε ένα ενιαίο αρχείο `.jsonl`.  
**Χρήση**: Τοποθετήστε αρχεία `.json` στον φάκελο `input_folder` και ορίστε το αρχείο `output_file`.

---

## Ευρετηριαστές

### `indexerwordmax.py`
**Σκοπός**: Εξάγει κείμενο από αρχεία `.doc` και `.docx`, επεξεργάζεται το πρώτο μισό του περιεχομένου και αποθηκεύει τα αποτελέσματα σε ένα αρχείο Excel.  
**Χρήση**: Τοποθετήστε αρχεία Word στη διαδρομή `folder_path`.

### `indexermax.py`
**Σκοπός**: Εξάγει κείμενο από την πρώτη σελίδα αρχείων PDF, επεξεργάζεται το πρώτο μισό του περιεχομένου και αποθηκεύει τα αποτελέσματα σε ένα αρχείο Excel.  
**Χρήση**: Τοποθετήστε αρχεία PDF στη διαδρομή `folder_path`.

### `indexer.py`
**Σκοπός**: Παρόμοιο με το `indexermax.py`, αλλά εστιάζει στην επεξεργασία όλων των αρχείων PDF σε έναν φάκελο.  
**Χρήση**: Τοποθετήστε αρχεία PDF στη διαδρομή `folder_path`.

---

## Εξαγωγείς

### `extract_subject.py`
**Σκοπός**: Εξάγει το "ΘΕΜΑ" από αρχεία PDF και αποθηκεύει τα αποτελέσματα σε ένα αρχείο CSV.  
**Χρήση**: Τοποθετήστε αρχεία PDF στη διαδρομή `folder_path`.

### `extract_subject_rename.py`
**Σκοπός**: Εξάγει το "ΘΕΜΑ" από αρχεία PDF, μετονομάζει τα αρχεία βάσει του εξαγόμενου θέματος και αποθηκεύει τα αποτελέσματα σε ένα αρχείο CSV.  
**Χρήση**: Τοποθετήστε αρχεία PDF στη διαδρομή `folder_path`.

### `extract_subject_rename_fek.py`
**Σκοπός**: Εξάγει μεταδεδομένα (π.χ., αριθμός "ΦΕΚ", έτος) από αρχεία PDF και τα μετονομάζει ανάλογα.  
**Χρήση**: Τοποθετήστε αρχεία PDF στη διαδρομή `folder_path`.

---

## Μετατροπείς

### `convert_to_jsonl1.py`
**Σκοπός**: Μετατρέπει πολλαπλά αρχεία `.json` σε ένα ενιαίο αρχείο `.jsonl`.  
**Χρήση**: Τοποθετήστε αρχεία `.json` στον φάκελο `input_folder`.

### `convert_to_jsonl.py`
**Σκοπός**: Μετατρέπει διάφορες μορφές αρχείων (PDF, DOCX, TXT) σε ένα αρχείο `.json`.  
**Χρήση**: Τοποθετήστε αρχεία στον φάκελο `input_folder`.

### `convert_pdfs_to_txt.py`
**Σκοπός**: Μετατρέπει αρχεία PDF σε μορφή `.txt` χρησιμοποιώντας OCR εάν είναι απαραίτητο.  
**Χρήση**: Τοποθετήστε αρχεία PDF στον φάκελο `PDF_FOLDER`.

### `convert_local.py`
**Σκοπός**: Παρόμοιο με το `convert_to_jsonl.py`, αλλά εστιάζει στην τοπική επεξεργασία αρχείων.  
**Χρήση**: Τοποθετήστε αρχεία στον φάκελο `input_folder`.

### `convert_documents.py`
**Σκοπός**: Μετατρέπει αρχεία PDF, DOCX και DOC σε μορφή `.txt`.  
**Χρήση**: Τοποθετήστε αρχεία στον φάκελο `input_folder`.

---

## Καθαριστές

### `clean_txt_fek.py`
**Σκοπός**: Καθαρίζει αρχεία `.txt` αφαιρώντας μεταδεδομένα και τα μορφοποιεί σε αρχεία Markdown.  
**Χρήση**: Τοποθετήστε αρχεία `.txt` στον κατάλογο `INPUT_DIR`.

### `clean_text.py`
**Σκοπός**: Καθαρίζει ένα ενιαίο αρχείο `.txt` και το μετατρέπει σε αρχείο Markdown.  
**Χρήση**: Ορίστε τις διαδρομές `INPUT_PATH` και `OUTPUT_PATH`.

### `clean_json.py`
**Σκοπός**: Καθαρίζει αρχεία `.json` αφαιρώντας περιττά πεδία και προβλήματα μορφοποίησης.  
**Χρήση**: Τοποθετήστε αρχεία `.json` στον φάκελο `input_folder`.

---

## Συνεργασίες

### `split_process_merge_jsonl.py`
**Σκοπός**: Διαχωρίζει ένα μεγάλο αρχείο `.jsonl`, επεξεργάζεται κάθε κομμάτι και συγχωνεύει τα αποτελέσματα ξανά σε ένα ενιαίο αρχείο.  
**Χρήση**: Ορίστε τα `input_file`, `split_folder`, `processed_folder` και `output_file`.

### `organize_and_index.py`
**Σκοπός**: Κατηγοριοποιεί αρχεία σε φακέλους βάσει λέξεων-κλειδιών και δημιουργεί ένα ευρετήριο Excel.  
**Χρήση**: Τοποθετήστε αρχεία στον φάκελο `input_folder`.

---

## Διάφορα

### `sort_files_offline.py`
**Σκοπός**: Κατηγοριοποιεί αρχεία και φακέλους βάσει των ονομάτων τους χωρίς τη χρήση API.  
**Χρήση**: Τοποθετήστε αρχεία στη διαδρομή `desktop_path`.

### `irida_script.py`
**Σκοπός**: Αλληλεπιδρά με το IRIDA API για την ανάκτηση και επεξεργασία εγγράφων.  
**Χρήση**: Ρυθμίστε τα διαπιστευτήρια και τα τελικά σημεία (endpoints) του API.

### `importtext.py`
**Σκοπός**: Εξάγει κείμενο από την πρώτη σελίδα ενός αρχείου PDF χρησιμοποιώντας OCR εάν είναι απαραίτητο.  
**Χρήση**: Ορίστε τη διαδρομή `pdf_path`.

### `fix_json.py`
**Σκοπός**: Διορθώνει προβλήματα μορφοποίησης JSON σε ένα ενιαίο αρχείο.  
**Χρήση**: Ορίστε τα αρχεία `input_file` και `output_file`.

### `create_index.py`
**Σκοπός**: Δημιουργεί ένα ευρετήριο καθαρισμένων αρχείων JSON με μεταδεδομένα και δείγματα εγγραφών.  
**Χρήση**: Τοποθετήστε αρχεία `.json` στον φάκελο `cleaned_folder`.

---

## Σημειώσεις

1. Βεβαιωθείτε ότι όλες οι εξαρτήσεις (dependencies) έχουν εγκατασταθεί πριν την εκτέλεση των scripts.
2. Τροποποιήστε τις διαδρομές αρχείων και τις παραμέτρους όπως απαιτείται για τη δική σας περίπτωση χρήσης.
3. Για τα scripts που σχετίζονται με OCR, βεβαιωθείτε ότι τα Tesseract και Poppler είναι σωστά εγκατεστημένα και ρυθμισμένα.
