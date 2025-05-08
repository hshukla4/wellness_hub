# Code to parse resumes (PDF/DOCX)
# This code is designed to extract information from resumes in PDF or DOCX format for IT job applications.
# It uses the PyMuPDF library to read PDF files and the python-docx library to read DOCX files.
# It also uses the spaCy library for natural language processing to identify named entities and noun chunks.
# It includes functions to extract skills, education, certifications, projects, languages, experience, publications, and references from the resume text.
# Import necessary libraries
from parsers.utils.pdf_docx_file_utils import  extract_text_from_file
import spacy

import re
import logging
import os
import sys
import warnings


from urllib3.exceptions import InsecureRequestWarning
# Suppress InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)
# Suppress NotOpenSSLWarning
# Suppress NotOpenSSLWarning
# Suppress InsecureRequestWarning
# Suppress InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)
# Suppress NotOpenSSLWarning
# Suppress NotOpenSSLWarning        
from urllib3.exceptions import NotOpenSSLWarning
warnings.simplefilter('ignore', NotOpenSSLWarning)
# Suppress InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from parsers.job_parser import load_jobs
# from parsers.resume_parser import parse_resume
# Load English model
nlp = spacy.load("en_core_web_sm")

# Sample resume text (for demonstration purposes)
skill_keywords = ['Python', 'SQL', 'GCP', 'machine learning', 'data analysis', 'web scraping', 'pandas', 'NumPy', 'scikit-learn', 'Flask', 'Docker', 'REST APIs']
education_keywords = ['Bachelor', 'Master', 'PhD', 'University', 'College', 'High School', 'School']
experience_keywords = ['Python', 'SQL', 'GCP', 'machine learning', 'data analysis', 'web scraping', 'pandas', 'NumPy', 'scikit-learn', 'Flask', 'Docker', 'REST APIs']
languages_keywords = ['Java', 'Python', 'Ruby', 'JavaScript', 'C++', 'C#', 'HTML', 'CSS', 'SQL', 'PHP', 'Swift', 'Go', 'Rust']
certificates_keywords = ['Certificate', 'Certification', 'Diploma', 'License']


    
def parse_resume(filename):
    returned_value = ""
    # Initialize lists to store extracted information
    educations_found =[]
    certifications_found = []
    skills_found = []
    languages_found = []
    experiences_found = []
    projects_found = []
    publications_found = []
    references_found = []
    # Extract text from the resume file

    cleaned_text = extract_text_from_file(filename)

    # Check if the file is a PDF or DOCX
    try:

        
        # Extract information from the cleaned text
        # Extracted information
        cleaned_text = extract_text_from_file(filename)
        educations_found = _extract_education(cleaned_text)
        certifications_found = _extract_certifications(cleaned_text)

        skills_found = _extract_skills(cleaned_text)
        languages_found = _extract_languages(cleaned_text)
        experiences_found = _extract_experience(cleaned_text)
        projects_found = _extract_projects(cleaned_text)
        publications_found = _extract_publications(cleaned_text)
        references_found = _extract_references(cleaned_text)
        returned_value = {
            "educations": educations_found,
            "certifications": certifications_found,
            "skills": skills_found,
            "languages": languages_found,
            "experiences": experiences_found,
            "projects": projects_found,
            "publications": publications_found,
            "references": references_found
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")
        returned_value = e
    # Return the extracted information
    return returned_value 

    
def _extract_skills(cleaned_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(cleaned_text)
    skills = []
    for ent in doc.ents:
        print(ent.text, ent.label_)
        skills += [ent.text for ent in doc.ents if ent.label_]
    for chunk in doc.noun_chunks:
        print(chunk.text)
    
    return skills

def _extract_education(cleaned_text):
    extract_education = []
    extract_education = [kw for kw in education_keywords if kw.lower() in cleaned_text.lower()]
    
    return extract_education

def _extract_certifications(cleaned_text):
    extract_certification = []
    extract_certification = [kw for kw in certificates_keywords if kw.lower() in cleaned_text.lower()]
    
    return extract_certification

def _extract_projects(cleaned_text):
    extract_projects = []
    
    for proj in cleaned_text.split('\n'):
        if re.search(r'\b(project|project name|project title)\b', proj, re.IGNORECASE):
            extract_projects+=proj;
    
    return extract_projects

def _extract_languages(cleaned_text):
    extract_languages = []
    
    extract_languages = [kw for kw in languages_keywords if kw.lower() in cleaned_text.lower()]
    
    return extract_languages


def _extract_publications(cleaned_text): 
    extract_publications = []
    
    for pub in cleaned_text.split('\n'):
        if re.search(r'\b(publication|paper|article)\b', pub, re.IGNORECASE):
            extract_publications+=pub;
    
    return extract_publications

def _extract_experience(cleaned_text):
    extract_experience = []
    
    for exp in cleaned_text.split('\n'):
        if re.search(r'\b(experience|work experience|job title)\b', exp, re.IGNORECASE):
            extract_experience+=exp;
    
    return extract_experience

def _extract_references(cleaned_text):
    extract_references = []
    
    for ref in cleaned_text.split('\n'):
        if re.search(r'\b(reference|referee)\b', ref, re.IGNORECASE):
            extract_references+=ref;
            
    return extract_references


logging.basicConfig(
    level=logging.ERROR,  # or DEBUG, INFO, WARNING
    format='%(asctime)s - %(levelname)s - %(message)s'
)