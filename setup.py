from setuptools import find_packages, setup  # type: ignore

setup(
    name="smart_job_ai",
    version="0.1",
    packages=find_packages(),
    install_requires=["spacy", "PyMuPDF>=1.21", "torch"],
    entry_points={"console_scripts": ["smartjob = smart_job_ai.main:main"]},
)
