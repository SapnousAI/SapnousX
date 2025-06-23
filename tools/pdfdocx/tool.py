try:
    import fitz  # PyMuPDF
    from docx import Document
    pdfdocx_available = True
except ImportError:
    pdfdocx_available = False

def extract_text_pdf(pdf_path):
    if not pdfdocx_available:
        return 'PyMuPDF not installed.'
    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

def create_docx(text, docx_path):
    if not pdfdocx_available:
        return 'python-docx not installed.'
    doc = Document()
    doc.add_paragraph(text)
    doc.save(docx_path)
    return f'Docx saved to {docx_path}'
