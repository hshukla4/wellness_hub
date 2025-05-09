# Basic test cases for CLI and modules
# test_run.py


# from parsers.resume_parser import parse_resume
# from parsers.job_parser import load_jobs


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

FILE_NAME = ".docs/sample_resume_generated.pdf"
from parsers.resume_parser import parse_resume

resume_text = parse_resume(FILE_NAME)
