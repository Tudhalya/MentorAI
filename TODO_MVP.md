# TODO — MVP Roadmap

This file outlines all phases & steps to bring the MVP to completion.

---

## Phase 0 — Foundations (Week 0–1)

- [x] Repo setup (monorepo or split: `frontend/`, `backend/`).
- [x] Initialize FastAPI backend.
- [x] Initialize SvelteKit frontend.
- [x] Add Postgres + Chroma (Docker Compose).
- [x] Basic REST endpoint: `upload_pdf`.

---

## Phase 1 — Ingestion & Parsing (Week 1–2)

- [ ] Parse PDF with `pymupdf`.
- [ ] Extract sections, headers, paragraphs.
- [ ] Store JSON structure in Postgres.
- [ ] Render chapter outline in UI.
- [ ] (Stretch) Add Nougat + pix2tex pipeline for equations.
- [ ] Store LaTeX + PNG render.

---

## Phase 2 — Indexing & Retrieval (Week 2–3)

- [ ] Create embeddings for text + equations.
- [ ] Store embeddings in Chroma.
- [ ] Implement hybrid retriever (BM25 + dense).
- [ ] Backend API: `search_sections(query, chapter_id)`.
- [ ] UI: highlight retrieved context.

---

## Phase 3 — Socratic Tutor Loop (Week 3–4)

- [ ] Implement tutor orchestrator (state machine).
- [ ] Backend: `start_session(chapter_id)`.
- [ ] Basic Q&A loop using RAG context.
- [ ] Track attempts in Postgres.
- [ ] UI: chat interface with tutor.

---

## Phase 4 — Exercise Engine v1 (Week 4–5)

- [ ] Implement exercise templates for ONE subject (pick math or robotics).
- [ ] Define exercise YAML schema (`goal`, `difficulty`, `rubric`).
- [ ] Generate exercise based on chapter context.
- [ ] Display exercise in UI.
- [ ] Accept submission (text/code).

---

## Phase 5 — Grading v1 (Week 5–6)

- [ ] Implement rubric-based grading with LLM.
- [ ] For code: run `pytest` in container.
- [ ] Store submissions + results in DB.
- [ ] Return structured feedback (✅, ❌, 🔑, 📖).

---

## Phase 6 — Mastery Tracking (Week 6)

- [ ] Implement per-skill consistency rule (3-of-4).
- [ ] Update mastery confidence after attempts.
- [ ] Backend: `get_mastery(user_id, chapter_id)`.
- [ ] UI: mastery heatmap per chapter.

---

## Phase 7 — UX & Reliability (Week 7–8)

- [ ] Add background jobs with Redis + RQ.
- [ ] Add “Why this question?” explanations.
- [ ] Add “Show me a hint” tiers.
- [ ] Add error handling/logging.
- [ ] Polish frontend (heatmap, side panel).

---

## Phase 8 — Stretch Goals

- [ ] Add spaced repetition refresh.
- [ ] Add code labs for multiple languages.
- [ ] Add essay grading templates.
- [ ] Integrate Mathpix as equation fallback.
- [ ] Multi-user accounts.
- [ ] Cloud deployment (Railway/Fly.io).

---
