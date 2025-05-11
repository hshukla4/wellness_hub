import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

FILE_NAME_PDF = ".docs/sample_resume.pdf"
FILE_NAME_DOCX = ".docs/sample_resume.docx"
FILE_DOES_NOT_EXIST = ".docs/sample_resume_does_not_exist.pdf"
INVALID_FILE_TYPE = ".docs/sample_resume_wrong.PNG"
EMPTY_FILE = ".docs/empty_resume.pdf"


from parsers.resume_parser import parse_resume
from parsers.utils.pdf_docx_file_utils import extract_section


def test_main():

    _parse_resume_pdf()
    _parse_resume_docx()
    _parse_resume_invalid_file_type()
    _parse_resume_empty_file()
    _parse_resume_none_input()
    _parse_resume_file_does_not_exist()
    _parse_resume_with_no_section_headers()


def _parse_resume_pdf():
    try:
        resume_text = parse_resume(FILE_NAME_PDF)
        assert resume_text is not None, "Resume should not be None"
        assert isinstance(resume_text, dict), "Resume output should be a dictionary"
        assert len(resume_text.keys()) > 0, "Resume dictionary should not be empty"
        print("[PASS] PDF resume parsed successfully")
    except Exception as e:
        print(f"[FAIL] PDF test failed: {e}")


def _parse_resume_docx():
    try:
        resume_text = parse_resume(FILE_NAME_DOCX)
        assert resume_text is not None, "Resume should not be None"
        assert isinstance(resume_text, dict), "Resume output should be a dictionary"
        assert len(resume_text.keys()) > 0, "Resume dictionary should not be empty"
        print("[PASS] DOCX resume parsed successfully")
    except Exception as e:
        print(f"[FAIL] DOCX test failed: {e}")


def _parse_resume_with_no_section_headers():
    text = "Just a plain file with no headers like Education or Skills."
    result = extract_section(text, "Education", ["Summary", "Skills"])
    assert result == "", "Expected no content extracted"
    print("[PASS] No section headers test passed")


def _parse_resume_invalid_file_type():
    try:
        parse_resume(INVALID_FILE_TYPE)
        assert False, "Should raise FileNotFoundError for invalid file type"
    except FileNotFoundError:
        print("[PASS] Invalid file type test passed")
    except Exception as e:
        print(f"[FAIL] Unexpected error for invalid file: {e}")


def _parse_resume_empty_file():
    try:
        parse_resume(EMPTY_FILE)
        assert False, "Should raise ValueError or return empty for blank file"
    except ValueError:
        print("[PASS] Blank file test passed (ValueError)")
    except Exception as e:
        print(f"[FAIL] Unexpected error for blank file: {e}")


def _parse_resume_none_input():
    try:
        parse_resume(None)
        assert False, "Should raise FileNotFoundError for None input"
    except FileNotFoundError:
        print("[PASS] None input test passed")
    except Exception as e:
        print(f"[FAIL] Unexpected error for None input: {e}")


def _parse_resume_file_does_not_exist():
    try:
        parse_resume(FILE_DOES_NOT_EXIST)
        assert False, "Should raise FileNotFoundError for missing file"
    except FileNotFoundError:
        print("[PASS] Missing file test passed")
    except Exception as e:
        print(f"[FAIL] Unexpected error for missing file: {e}")


if __name__ == "__main__":
    test_main()
