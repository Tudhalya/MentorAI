# MentorAI - MVP Development

AI-Powered Learning Assistant that processes textbook PDFs and provides Socratic tutoring.

## Project Structure

```
MentorAI/
├── frontend/           # SvelteKit web application
├── backend/           # FastAPI Python service
└── infrastructure/    # DevOps and infrastructure configs
    ├── database/      # Database schemas and migrations
    ├── docker/        # Docker Compose and container configs
    └── deployment/    # Deployment scripts and configs
```

## Quick Start

### 1. Start Services (Postgres + Chroma)
```bash
cd infrastructure/docker
docker-compose up -d
```

### 2. Backend Setup
```bash
cd backend
poetry install
poetry run python run.py
```
Backend runs on: http://localhost:8001

### 3. Frontend Setup
```bash
cd frontend
pnpm install
pnpm dev
```
Frontend runs on: http://localhost:5173

## Current Implementation Status

✅ **Phase 0 - Foundations (COMPLETED)**
- [x] Monorepo structure with frontend/ and backend/
- [x] FastAPI backend initialized
- [x] SvelteKit frontend initialized
- [x] Docker Compose for Postgres + Chroma
- [x] Basic REST endpoint: `POST /api/upload_pdf`

## API Endpoints

### `POST /api/upload_pdf`
Upload and parse a PDF textbook.
- Accepts PDF files via multipart/form-data
- Returns basic metadata and text preview
- Stores file in `backend/uploads/`

### `GET /api/health`
Health check endpoint with service status.

## Database Schema

Initial tables created:
- `documents` - Uploaded PDF metadata
- `chapters` - Chapter structure within documents
- `nodes` - Content nodes (text, equations, figures)

## Development Notes

- Backend uses Poetry for dependency management
- Frontend uses pnpm for package management
- Database migrations handled by Alembic (to be implemented)
- File uploads stored locally in `backend/uploads/`

## Next Steps (Phase 1)

See `TODO_MVP.md` for the complete roadmap. Next phase involves:
- Parse PDF structure with pymupdf
- Extract sections, headers, paragraphs
- Store JSON structure in Postgres
- Render chapter outline in UI