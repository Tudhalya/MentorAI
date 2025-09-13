#!/usr/bin/env python3
"""
Development server startup script for MentorAI backend
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.mentorai.main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    )