from setuptools import setup, find_packages

setup(
    name="wellness_hub",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "spacy",
        "PyMuPDF>=1.21",
        "torch",
        "durable_rules",
        "Flask",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "wellness=wellness_hub.main:main"
        ]
    },
    include_package_data=True
)