from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import os
import shutil
from typing import Dict, Any
import pymupdf
from datetime import datetime

app = FastAPI(
    title="MentorAI API",
    description="AI-Powered Learning Assistant API",
    version="0.1.0"
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # SvelteKit dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory if it doesn't exist
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "MentorAI API is running", "timestamp": datetime.now().isoformat()}

@app.post("/api/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)) -> Dict[str, Any]:
    """
    Upload and parse a PDF textbook.

    This endpoint:
    1. Validates the uploaded file is a PDF
    2. Saves it to disk
    3. Extracts basic metadata using PyMuPDF
    4. Returns parsing results
    """

    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="File must have .pdf extension"
        )

    try:
        # Save uploaded file
        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Parse PDF with PyMuPDF
        doc = pymupdf.open(file_path)

        # Extract basic metadata
        metadata = doc.metadata
        page_count = len(doc)

        # Extract text from first few pages for preview
        preview_text = ""
        for page_num in range(min(3, page_count)):  # First 3 pages
            page = doc[page_num]
            preview_text += page.get_text()
            if len(preview_text) > 1000:  # Limit preview length
                preview_text = preview_text[:1000] + "..."
                break

        doc.close()

        # Return parsing results
        return {
            "status": "success",
            "filename": file.filename,
            "file_path": str(file_path),
            "page_count": page_count,
            "metadata": {
                "title": metadata.get("title", ""),
                "author": metadata.get("author", ""),
                "subject": metadata.get("subject", ""),
                "creator": metadata.get("creator", ""),
                "producer": metadata.get("producer", ""),
            },
            "preview_text": preview_text[:500] + "..." if len(preview_text) > 500 else preview_text,
            "message": f"Successfully parsed PDF with {page_count} pages"
        }

    except Exception as e:
        # Clean up file if parsing failed
        if file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {str(e)}"
        )

@app.get("/api/health")
async def health_check():
    """Extended health check with service status"""
    return {
        "status": "healthy",
        "services": {
            "api": "running",
            "upload_dir": str(UPLOAD_DIR.absolute()),
            "upload_dir_exists": UPLOAD_DIR.exists()
        },
        "timestamp": datetime.now().isoformat()
    }