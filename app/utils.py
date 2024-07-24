import io
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_bytes):
    # Convert bytes to a file-like object
    pdf_file = io.BytesIO(pdf_bytes)
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text