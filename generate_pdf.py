from jinja2 import Template
from weasyprint import HTML
import os

# Load test data
from test_data import user_data
def generate_pixel_perfect_pdf(user_data):
# Load template
    with open('template.html', 'r', encoding='utf-8') as f:
        template_str = f.read()

    # Create Jinja2 template
    template = Template(template_str)

    # Render template with data
    rendered_html = template.render(**user_data)

    # Generate PDF
    pdf_output = 'output_cv.pdf'
    HTML(string=rendered_html).write_pdf(pdf_output)
    return pdf_output

    # print(f"✅ PDF generated successfully: {os.path.abspath(pdf_output)}")

    # Optional: Open PDF automatically (Windows only)
    # import subprocess
    # subprocess.Popen(['start', pdf_output], shell=True)