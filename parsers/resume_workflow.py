import os
import sys
import warnings

import spacy  # type: ignore
from spacy.matcher import PhraseMatcher

# Suppress NotOpenSSLWarning
from urllib3.exceptions import InsecureRequestWarning  # type: ignore
from urllib3.exceptions import NotOpenSSLWarning

from parsers.utils.pdf_docx_file_utils import extract_text_from_file

warnings.simplefilter("ignore", NotOpenSSLWarning)
# Suppress InsecureRequestWarning
warnings.simplefilter("ignore", InsecureRequestWarning)
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


nlp = spacy.load("en_core_web_sm")


def parse_resume_workflow(file_path):
    """
    Parse the resume file and extract relevant information.
    """
    # For demonstration, we will just return a sample text
    # In a real scenario, you would read the file and extract text
    return """
    John Doe
    Python Developer with 5 years of experience in machine learning and data analysis.
    Skills: Python, SQL, GCP, machine learning, data analysis, web scraping.
    Education: Bachelor of Science in Computer Science from XYZ University.
    Languages: English, Spanish.
    """
    resume_text = extract_text_from_file(file_path)

    doc = nlp(resume_text)

    # Example: Extract Named Entities
    for ent in doc.ents:
        print(ent.text, ent.label_)

    # Example: Match skills
    skills = ["Python", "TensorFlow", "Docker", "REST APIs"]
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp.make_doc(skill) for skill in skills]
    matcher.add("SKILLS", patterns)

    matches = matcher(doc)
    for match_id, start, end in matches:
        print("Skill found:", doc[start:end].text)
    return doc
