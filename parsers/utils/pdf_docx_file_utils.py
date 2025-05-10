import logging
import os
import re
import sys
import warnings
from typing import Final

import fitz  # This is PyMuPDF
from docx import Document  # Import Document from python-docx
from urllib3.exceptions import InsecureRequestWarning, NotOpenSSLWarning

# Suppress InsecureRequestWarning
warnings.simplefilter("ignore", InsecureRequestWarning)
# Suppress NotOpenSSLWarning
warnings.simplefilter("ignore", NotOpenSSLWarning)
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Suppress InsecureRequestWarning
warnings.simplefilter("ignore", InsecureRequestWarning)
# Suppress NotOpenSSLWarning
warnings.simplefilter("ignore", NotOpenSSLWarning)

NEW_LINE: Final = "\n"


def _check_file_type(filename):
    if filename is None or filename == "":
        print("Filename is empty or None.")
        raise FileNotFoundError("Filename is empty or None.")
    import os

    # Check if the file exists
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        raise FileNotFoundError(f"File {filename} does not exist.")

    # Check if the file is a PDFor DOCX
    else:
        if not filename.endswith(".pdf") and not filename.endswith(".docx"):
            print(f"File {filename} is not a PDF or DOCX file.")
            raise FileNotFoundError(f"File {filename} is not a PDF or DOCX file.")


def extract_text_from_file(filename):
    # Check if the file is a PDF or DOCX
    # If the file is a PDF, use PyMuPDF to extract text
    _check_file_type(filename)
    try:
        if filename.endswith(".pdf"):
            # Open the PDF file
            doc = fitz.open(filename)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
        # If the file is a DOCX, use python-docx to extract text
        elif filename.endswith(".docx"):
            # Open the DOCX file
            doc = Document(filename)
            for para in doc.paragraphs:
                text += para.text + NEW_LINE
            doc.close()  # Clean the text by removing extra spaces and newlines
        text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
        text = re.sub(
            r"\n+", NEW_LINE, text
        )  # Replace multiple newlines with a single newline
        text = text.strip()  # Remove leading and trailing spaces
    except Exception as e:
        print(f"Error extracting text from {filename}: {e}")
        logging.error(f"Error extracting text from {filename}: {e}")
        raise e
    return text


def extract_section(cleaned_text, section_names, stop_words):
    for name in section_names:
        pattern = rf"{name}[\s:]*\n([\s\S]+?)(?=\n(?:{'|'.join(stop_words)})[\s:]|\Z)"
        match = re.search(pattern, cleaned_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ""
