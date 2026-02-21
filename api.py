from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app  = FastAPI(title="Research AI Backend", version="1.0")

class DocumentRequest(BaseModel):
    title: str 
    content: str 
    max_summary_length: int = 100

@app.get("/")
def health_check():
    return {"status":"operational" , "message" : "AI Backend is running."}

@app.post("/process-document")
def process_document(doc: DocumentRequest):
    if not doc.content.strip():
        raise HTTPException(status_code=400, detail="Document content cannot be empty.")
    
    word_count = len(doc.content.split())
    simulated_summary = f"This document is about {doc.title}. It contains {word_count} words."

    return {
        "success": True,
        "document_tile": doc.title,
        "summary": simulated_summary,
        "model_used": "mock-nano-v1"
    }