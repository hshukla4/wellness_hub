from markdown2 import markdown
from weasyprint import HTML
from pathlib import Path

# Ensure docs directory exists
Path("docs").mkdir(parents=True, exist_ok=True)

# Convert Markdown to HTML and then to PDF
with open("README.md", "r") as f:
    html_content = markdown(f.read())

output_path = "docs/README_WellnessHub.pdf"
HTML(string=html_content).write_pdf(output_path)

print(f"✅ PDF generated at: {output_path}")
