from PyPDF2 import PdfReader

def pdf_loader(file_path):
    """
    Load a PDF file and extract its text content.

    Args:
        file_path (str): The path to the PDF file.
    """
    pdf_reader = PdfReader(file_path)
    text_content = ""
    for page in pdf_reader.pages:
        text_content += page.extract_text()
    return text_content

