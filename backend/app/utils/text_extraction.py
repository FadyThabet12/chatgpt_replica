from pathlib import Path
from pypdf import PdfReader

def extract_text(path):
    ext = Path(path).suffix.lower()
    if ext == ".pdf":
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if ext == ".txt":
        return Path(path).read_text(encoding="utf-8")
    raise ValueError("Only PDF and TXT files are supported")
