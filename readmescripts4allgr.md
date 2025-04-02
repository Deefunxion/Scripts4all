Περιεχόμενα
Splitters
Organizers
Mergers
Indexers
Extractors
Converters
Cleaners
Collaborations
Miscellaneous
Splitters (Διαχωριστές)
split_jsonl.py
Purpose: Διαχωρίζει ένα μεγάλο αρχείο .jsonl σε μικρότερα κομμάτια βάσει ενός καθορισμένου αριθμού εγγραφών ανά αρχείο.
Usage: Τροποποιήστε τις μεταβλητές input_file, output_folder και chunk_size για να προσαρμόσετε τη διαδικασία διαχωρισμού.
split_json.py
Purpose: Διαχωρίζει ένα αρχείο .json σε μικρότερα αρχεία .json, καθένα από τα οποία περιέχει έναν καθορισμένο αριθμό εγγραφών.
Usage: Ορίστε τις μεταβλητές input_file, chunk_size και output_folder για να ρυθμίσετε τον διαχωρισμό.
split_and_clean_txt.py
Purpose: Καθαρίζει και διαχωρίζει αρχεία .txt σε δύο μέρη, αφαιρώντας ανεπιθύμητους χαρακτήρες και προβλήματα μορφοποίησης.
Usage: Τοποθετήστε τα αρχεία .txt στον φάκελο input_folder και εκτελέστε το script.
Organizers (Οργανωτές)
organize_txt.py
Purpose: Κατηγοριοποιεί αρχεία .txt σε φακέλους με βάση λέξεις-κλειδιά και διαχωρίζει μεγάλα αρχεία σε μικρότερα.
Usage: Ορίστε τη μεταβλητή folder_path και προσαρμόστε τη συνάρτηση categorize_text με τις σχετικές λέξεις-κλειδιά.
organize_files.py
Purpose: Οργανώνει αρχεία και φακέλους σε προκαθορισμένες κατηγορίες με βάση τα ονόματά τους.
Usage: Τοποθετήστε τα αρχεία στη μεταβλητή desktop_path και εκτελέστε το script.
organize_files_smart.py
Purpose: Διαβάζει το περιεχόμενο αρχείων (PDF, DOCX, TXT, XLSX) και τα κατηγοριοποιεί με βάση λέξεις-κλειδιά.
Usage: Τοποθετήστε τα αρχεία στη μεταβλητή desktop_path και εκτελέστε το script.
Mergers (Συγχωνευτές)
merge_txt.py
Purpose: Συγχωνεύει πολλαπλά αρχεία .txt σε μεγαλύτερα αρχεία, ομαδοποιώντας τα σε τμήματα.
Usage: Τοποθετήστε τα αρχεία .txt στον φάκελο input_folder και ορίστε τον φάκελο output_folder.
merge_txt_per_folder.py
Purpose: Συγχωνεύει όλα τα αρχεία .txt σε κάθε υποφάκελο σε ένα ενιαίο αρχείο ανά φάκελο.
Usage: Τοποθετήστε τους υποφακέλους με τα αρχεία .txt στον φάκελο input_folder.
merge_selected_txt.py
Purpose: Συγχωνεύει συγκεκριμένα αρχεία .txt σε ένα ενιαίο αρχείο με βάση προκαθορισμένες ομάδες.
Usage: Ορίστε το λεξικό groups με τα ονόματα των αρχείων που θέλετε να συγχωνεύσετε.
merge_jsonl.py
Purpose: Συγχωνεύει πολλαπλά αρχεία .json σε ένα ενιαίο αρχείο .jsonl.
Usage: Τοποθετήστε τα αρχεία .json στον φάκελο input_folder και ορίστε το αρχείο output_file.
Indexers (Δημιουργία Ευρετηρίου)
indexerwordmax.py
Purpose: Εξάγει κείμενο από αρχεία .doc και .docx, επεξεργάζεται το πρώτο μισό του περιεχομένου και αποθηκεύει τα αποτελέσματα σε ένα αρχείο Excel.
Usage: Τοποθετήστε τα αρχεία Word στον φάκελο folder_path.
indexermax.py
Purpose: Εξάγει κείμενο από την πρώτη σελίδα αρχείων PDF, επεξεργάζεται το πρώτο μισό του περιεχομένου και αποθηκεύει τα αποτελέσματα σε ένα αρχείο Excel.
Usage: Τοποθετήστε τα αρχεία PDF στον φάκελο folder_path.
indexer.py
Purpose: Παρόμοιο με το indexermax.py, αλλά εστιάζει στην επεξεργασία όλων των αρχείων PDF σε έναν φάκελο.
Usage: Τοποθετήστε τα αρχεία PDF στον φάκελο folder_path.
Extractors (Εξαγωγείς)
extract_subject.py
Purpose: Εξάγει το "ΘΕΜΑ" από αρχεία PDF και αποθηκεύει τα αποτελέσματα σε ένα αρχείο CSV.
Usage: Τοποθετήστε τα αρχεία PDF στον φάκελο folder_path.
extract_subject_rename.py
Purpose: Εξάγει το "ΘΕΜΑ" από αρχεία PDF, μετονομάζει τα αρχεία με βάση το εξαγόμενο θέμα και αποθηκεύει τα αποτελέσματα σε ένα αρχείο CSV.
Usage: Τοποθετήστε τα αρχεία PDF στον φάκελο folder_path.
extract_subject_rename_fek.py
Purpose: Εξάγει μεταδεδομένα (π.χ., αριθμός "ΦΕΚ", έτος) από αρχεία PDF και τα μετονομάζει ανάλογα.
Usage: Τοποθετήστε τα αρχεία PDF στον φάκελο folder_path.
Converters (Μετατροπείς)
convert_to_jsonl1.py
Purpose: Μετατρέπει πολλαπλά αρχεία .json σε ένα ενιαίο αρχείο .jsonl.
Usage: Τοποθετήστε τα αρχεία .json στον φάκελο input_folder.
convert_to_jsonl.py
Purpose: Μετατρέπει διάφορες μορφές αρχείων (PDF, DOCX, TXT) σε ένα αρχείο .json.
Usage: Τοποθετήστε τα αρχεία στον φάκελο input_folder.
convert_pdfs_to_txt.py
Purpose: Μετατρέπει αρχεία PDF σε μορφή .txt χρησιμοποιώντας OCR εάν είναι απαραίτητο.
Usage: Τοποθετήστε τα αρχεία PDF στον φάκελο PDF_FOLDER.
convert_local.py
Purpose: Παρόμοιο με το convert_to_jsonl.py, αλλά εστιάζει στην επεξεργασία τοπικών αρχείων.
Usage: Τοποθετήστε τα αρχεία στον φάκελο input_folder.
convert_documents.py
Purpose: Μετατρέπει αρχεία PDF, DOCX και DOC σε μορφή .txt.
Usage: Τοποθετήστε τα αρχεία στον φάκελο input_folder.
Cleaners (Καθαριστές)
clean_txt_fek.py
Purpose: Καθαρίζει αρχεία .txt αφαιρώντας μεταδεδομένα και τα μορφοποιεί σε αρχεία Markdown.
Usage: Τοποθετήστε τα αρχεία .txt στον φάκελο INPUT_DIR.
clean_text.py
Purpose: Καθαρίζει ένα μεμονωμένο αρχείο .txt και το μετατρέπει σε ένα αρχείο Markdown.
Usage: Ορίστε τις μεταβλητές INPUT_PATH και OUTPUT_PATH.
clean_json.py
Purpose: Καθαρίζει αρχεία .json αφαιρώντας περιττά πεδία και προβλήματα μορφοποίησης.
Usage: Τοποθετήστε τα αρχεία .json στον φάκελο input_folder.
Collaborations (Συνεργασίες)
split_process_merge_jsonl.py
Purpose: Διαχωρίζει ένα μεγάλο αρχείο .jsonl, επεξεργάζεται κάθε τμήμα και συγχωνεύει τα αποτελέσματα ξανά σε ένα ενιαίο αρχείο.
Usage: Ορίστε τις μεταβλητές input_file, split_folder, processed_folder και output_file.
organize_and_index.py
Purpose: Κατηγοριοποιεί αρχεία σε φακέλους με βάση λέξεις-κλειδιά και δημιουργεί ένα ευρετήριο σε Excel.
Usage: Τοποθετήστε τα αρχεία στον φάκελο input_folder.
Miscellaneous (Διάφορα)
sort_files_offline.py
Purpose: Κατηγοριοποιεί αρχεία και φακέλους με βάση τα ονόματά τους χωρίς τη χρήση API.
Usage: Τοποθετήστε τα αρχεία στη μεταβλητή desktop_path.
irida_script.py
Purpose: Αλληλεπιδρά με το IRIDA API για την ανάκτηση και επεξεργασία εγγράφων.
Usage: Ρυθμίστε τα διαπιστευτήρια και τα endpoints του API.
importtext.py
Purpose: Εξάγει κείμενο από την πρώτη σελίδα ενός αρχείου PDF χρησιμοποιώντας OCR εάν είναι απαραίτητο.
Usage: Ορίστε τη μεταβλητή pdf_path.
fix_json.py
Purpose: Διορθώνει προβλήματα μορφοποίησης JSON σε ένα μεμονωμένο αρχείο.
Usage: Ορίστε τις μεταβλητές input_file και output_file.
create_index.py
Purpose: Δημιουργεί ένα ευρετήριο καθαρισμένων αρχείων JSON με μεταδεδομένα και δείγματα εγγραφών.
Usage: Τοποθετήστε τα αρχεία .json στον φάκελο cleaned_folder.
Notes (Σημειώσεις)
Purpose: Βεβαιωθείτε ότι όλες οι εξαρτήσεις είναι εγκατεστημένες πριν εκτελέσετε τα scripts.
Usage: Τροποποιήστε τις διαδρομές αρχείων και τις παραμέτρους όπως απαιτείται για τη συγκεκριμένη περίπτωση χρήσης σας.
Usage: Για scripts που σχετίζονται με OCR, βεβαιωθείτε ότι τα Tesseract και Poppler είναι σωστά εγκατεστημένα και ρυθμισμένα.
Ελπίζω αυτή η έκδοση να είναι σωστή και να ανταποκρίνεται στην επιθυμία σας. Αν χρειάζεστε κάτι άλλο, παρακαλώ πείτε μου.