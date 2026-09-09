from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from pgvector.sqlalchemy import Vector
from app.config import settings

engine = create_engine(settings.POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class DocumentChunk(Base):
    __tablename__ = "document_chunks"
    id = Column(Integer, primary_key=True)
    document_id = Column(String, nullable=False)
    text = Column(String, nullable=False)
    embedding = Column(Vector(384), nullable=False)

Base.metadata.create_all(engine)

def store_chunk(document_id, text, embedding):
    db = SessionLocal()
    try:
        db.add(DocumentChunk(document_id=document_id, text=text, embedding=embedding))
        db.commit()
    finally:
        db.close()

def search(query_embedding, top_k=5):
    db = SessionLocal()
    try:
        return db.query(DocumentChunk).order_by(DocumentChunk.embedding.cosine_distance(query_embedding)).limit(top_k).all()
    finally:
        db.close()
