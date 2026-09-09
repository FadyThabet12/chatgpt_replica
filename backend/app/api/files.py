import uuid
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.text_extraction import extract_text
from app.utils.chunking import chunk_text
from app.utils.embeddings import embed
from app.db.vector_db import store_chunk

router = APIRouter(prefix="/files", tags=["files"])
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    if Path(file.filename).suffix.lower() not in {".pdf", ".txt"}:
        raise HTTPException(400, "Only PDF and TXT files are supported")
    doc_id = str(uuid.uuid4())
    path = UPLOAD_DIR / f"{doc_id}_{file.filename}"
    path.write_bytes(await file.read())
    text = extract_text(str(path))
    chunks = chunk_text(text)
    for chunk in chunks:
        store_chunk(doc_id, chunk, embed(chunk))
    return {"document_id": doc_id, "chunks": len(chunks), "status": "ready"}
