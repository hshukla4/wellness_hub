# Code to parse resumes (PDF/DOCX)
# This code is designed to extract information from resumes in PDF or DOCX format for IT job applications.
# It uses the PyMuPDF library to read PDF files and the python-docx library to read DOCX files.
# It also uses the spaCy library for natural language processing to identify named entities and noun chunks.
# It includes functions to extract skills, education, certifications, projects, languages, experience, publications, and references from the resume text.
# Import necessary libraries
import json
import logging
import os
import re
import sys
import warnings

import spacy  # type: ignore

# Suppress NotOpenSSLWarning
# Suppress NotOpenSSLWarning
from urllib3.exceptions import InsecureRequestWarning  # type: ignore
from urllib3.exceptions import NotOpenSSLWarning

from parsers.utils.pdf_docx_file_utils import extract_text_from_file

warnings.simplefilter("ignore", NotOpenSSLWarning)
# Suppress InsecureRequestWarning
warnings.simplefilter("ignore", InsecureRequestWarning)
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# from parsers.job_parser import load_jobs
# from parsers.resume_parser import parse_resume
# Load English model
nlp = spacy.load("en_core_web_sm")

# Sample resume text (for demonstration purposes)
skill_keywords = [
    "Python",
    "SQL",
    "GCP",
    "machine learning",
    "data analysis",
    "web scraping",
    "pandas",
    "NumPy",
    "scikit-learn",
    "Flask",
    "Docker",
    "REST APIs",
]
education_keywords = [
    "Bachelor",
    "Master",
    "PhD",
    "University",
    "College",
    "High School",
    "School",
]
experience_keywords = [
    "Python",
    "SQL",
    "GCP",
    "machine learning",
    "data analysis",
    "web scraping",
    "pandas",
    "NumPy",
    "scikit-learn",
    "Flask",
    "Docker",
    "REST APIs",
]
languages_keywords = [
    "Java",
    "Python",
    "Ruby",
    "JavaScript",
    "C++",
    "C#",
    "HTML",
    "CSS",
    "SQL",
    "PHP",
    "Swift",
    "Go",
    "Rust",
]
certificates_keywords = ["Certificate", "Certification", "Diploma", "License"]
SECTION_STOP_WORDS = [
    "Summary",
    "Skills",
    "Experience",
    "Projects",
    "Education",
    "Certifications",
    "Publications",
    "References",
]

SECTION_HEADERS = {
    "education": ["Education", "Educational Background", "Academic Qualifications"],
    "experience": ["Experience", "Work Experience", "Professional Experience"],
    "projects": ["Projects", "Project Work", "Project Experience"],
}


def parse_resume(filename):

    returned_value = ""
    # Extract text from the resume file

    # Check if the file is a PDF or DOCX
    # try:
    # Extract information from the cleaned text
    # Extracted information
    cleaned_text = extract_text_from_file(filename)
    # cleaned_text = normalize_headers(cleaned_text, SECTION_STOP_WORDS)
    returned_value = _parse_resume_text(
        cleaned_text, skill_keywords, languages_keywords, certificates_keywords
    )

    print(json.dumps(returned_value, indent=4, ensure_ascii=False))
    return returned_value


def _normalize_headers(text, headers):
    for header in headers:
        pattern = rf"(?<!\n)({header}[:])"
        text = re.sub(pattern, r"\n\1", text, flags=re.IGNORECASE)
    return text


def _extract_section(cleaned_text, section_names, stop_words):
    for name in section_names:
        # Final fix: match full line section headers only
        # pattern = rf"(?:^|\n){name}\b[\s:]*([\s\S]+?)(?=\n(?:{'|'.join(stop_words)})(?:\s|:|\n|\Z))"
        pattern = rf"(?:^|\n){name}[\s:]+([^\n]+)"
        match = re.search(pattern, cleaned_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ""


def _extract_skills(cleaned_text, skill_keywords):
    return [kw for kw in skill_keywords if kw.lower() in cleaned_text.lower()]


def _extract_languages(cleaned_text, language_keywords):
    return [kw for kw in language_keywords if kw.lower() in cleaned_text.lower()]


def _extract_certifications(cleaned_text, certificate_keywords):
    return [kw for kw in certificate_keywords if kw.lower() in cleaned_text.lower()]


def _extract_list_from_section(section_text):
    return [line.strip("-• \t") for line in section_text.splitlines() if line.strip()]


def _parse_resume_text(
    cleaned_text, skill_keywords, language_keywords, certificate_keywords
):
    try:
        cleaned_text = _normalize_headers(cleaned_text, SECTION_STOP_WORDS)

        education = _extract_section(
            cleaned_text, SECTION_HEADERS["education"], SECTION_STOP_WORDS
        )
        experience = _extract_section(
            cleaned_text, SECTION_HEADERS["experience"], SECTION_STOP_WORDS
        )
        project_text = _extract_section(
            cleaned_text, SECTION_HEADERS["projects"], SECTION_STOP_WORDS
        )

        result = {
            "education": _extract_list_from_section(education),
            "certifications": _extract_certifications(
                cleaned_text, certificate_keywords
            ),
            "skills": _extract_skills(cleaned_text, skill_keywords),
            "languages": _extract_languages(cleaned_text, language_keywords),
            "experiences": _extract_list_from_section(experience),
            "projects": _extract_list_from_section(project_text),
            "publications": _extract_publications(cleaned_text),
            "references": _extract_references(cleaned_text),
        }
        return result

    except Exception as e:
        logging.error(f"Resume parsing error: {e}")
        return {"error": str(e)}


# def _extract_skills(cleaned_text):
#     # nlp = spacy.load("en_core_web_sm")
#     # doc = nlp(cleaned_text)
#     # skills = []
#     # for ent in doc.ents:
#     #     skills += [ent.text for ent in doc.ents if ent.label_]

#     skills = [kw for kw in skill_keywords if kw.lower() in cleaned_text.lower()]

#     return skills


# def _extract_certifications(cleaned_text):
#     extract_certification = [
#         kw for kw in certificates_keywords if kw.lower() in cleaned_text.lower()
#     ]

#     return extract_certification


# def _extract_languages(cleaned_text):

#     extract_languages = [
#         kw for kw in languages_keywords if kw.lower() in cleaned_text.lower()
#     ]

#     return extract_languages


def _extract_publications(cleaned_text):
    extract_publications = []

    for pub in cleaned_text.split("\n"):
        if re.search(r"\b(publication|paper|article)\b", pub, re.IGNORECASE):
            extract_publications += pub

    return extract_publications


def _extract_references(cleaned_text):
    extract_references = []

    for ref in cleaned_text.split("\n"):
        if re.search(r"\b(reference|referee)\b", ref, re.IGNORECASE):
            extract_references += ref

    return extract_references


logging.basicConfig(
    level=logging.ERROR,  # or DEBUG, INFO, WARNING
    format="%(asctime)s - %(levelname)s - %(message)s",
)
