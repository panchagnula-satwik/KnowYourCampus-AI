import os
import json
from pypdf import PdfReader

# Folder paths
RAW_PDF_DIR = "data/raw_pdfs"
PROCESSED_DIR = "data/processed"
OUTPUT_FILE = os.path.join(PROCESSED_DIR, "extracted_text.json")


def extract_text_from_pdf(pdf_path):
    """
    This function reads ONE PDF file and returns all the text inside it.
    """
    reader = PdfReader(pdf_path)
    text = ""

    # Read each page one by one
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text.strip()


def ingest_pdfs():
    """
    This function goes through all PDFs in data/raw_pdfs
    and extracts their text.
    """
    extracted_data = []

    for file_name in os.listdir(RAW_PDF_DIR):
        if file_name.lower().endswith(".pdf"):
            pdf_path = os.path.join(RAW_PDF_DIR, file_name)
            print(f"Processing: {file_name}")

            text = extract_text_from_pdf(pdf_path)

            extracted_data.append({
                "source": file_name,
                "text": text
            })

    return extracted_data


def save_extracted_text(data):
    """
    This function saves the extracted text into a JSON file.
    """
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nExtraction complete. Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    extracted_data = ingest_pdfs()
    save_extracted_text(extracted_data)