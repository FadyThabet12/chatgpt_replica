from app.db.vector_db import search
from app.utils.embeddings import embed

def retrieve(query, top_k=5):
    rows = search(embed(query), top_k)
    return "\n\n---\n\n".join(r.text for r in rows)
