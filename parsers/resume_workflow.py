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
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

nlp = spacy.load("en_core_web_sm")


def parse_resume_workflow(file_path):
    """
    Parse the resume file and extract relevant information.
    """
    resume_text = extract_text_from_file(file_path)
    doc = nlp(resume_text)

    # Example: Extract Named Entities
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Match skills
    skills = ["Python", "TensorFlow", "Docker", "REST APIs"]
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp.make_doc(skill) for skill in skills]
    matcher.add("SKILLS", patterns)

    matched_skills = []
    matches = matcher(doc)
    for match_id, start, end in matches:
        matched_skills.append(doc[start:end].text)

    return {"text": resume_text, "entities": named_entities, "skills": matched_skills}
