import fitz
from docx import Document
import tempfile

async def parse_document(file):

    suffix = file.filename.split('.')[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{suffix}') as tmp:
        tmp.write(await file.read())
        path = tmp.name

    if suffix == 'pdf':
        return parse_pdf(path)

    if suffix == 'docx':
        return parse_docx(path)

    return "Unsupported file type"


def parse_pdf(path):
    doc = fitz.open(path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


def parse_docx(path):
    doc = Document(path)

    return "\n".join([p.text for p in doc.paragraphs])