import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from parsers.resume_workflow import parse_resume_workflow
# from parsers.utils.pdf_docx_file_utils import extract_section

FILE_NAME = ".docs/sample_resume.pdf"


@pytest.mark.parse_workflow
@pytest.mark.skipif(not os.path.exists(FILE_NAME), reason="Resume file not found")
def test_parse_resume_workflow():
    print("Testing resume parsing workflow...")
    from parsers.resume_workflow import parse_resume_workflow

    result = parse_resume_workflow(FILE_NAME)

    assert result is not None, "Resume parsing failed, result is None"
    assert isinstance(result, dict), "Expected dict as output"

    assert "Python" in result["text"], "Expected 'Python' in resume text"
    assert "Python" in result["skills"], "Expected 'Python' in extracted skills"

    print("[PASS] Resume parsing workflow test passed")
