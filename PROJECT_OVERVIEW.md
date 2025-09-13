# AI-Powered Learning Assistant — Project Overview

This document is a knowledge base for LLM agents working on the project.  
It summarizes the **vision, architecture, stack, constraints, and design rules**.

---

## Core Vision

Create a study assistant that:

- Accepts ANY textbook PDF as input.
- Helps users deeply understand each chapter via Socratic Q&A.
- Assigns relevant exercises:
  - Coding labs (CS/robotics).
  - Problem sets (math/science).
  - Essays (humanities).
- Provides iterative feedback until mastery is achieved.
- Acts as both **teacher** (concepts) and **instructor** (exercise review).
- Tracks mastery through consistency, not single scores.

---

## Desired User Flow

1. Upload textbook PDF.
2. System parses content (sections, equations, figures).
3. User selects chapter.
4. Socratic Q&A dialogue loop.
5. Continues until concept mastery.
6. Assigns exercises.
7. Reviews submissions, provides feedback.
8. Confirms mastery → move to next chapter.

---

## High-Level Architecture

**Services**

1. **Ingestion & Parsing**
   - Extract text, equations, figures → JSON structure.
   - Tools: `pymupdf`, Nougat, pix2tex, Mathpix (optional).

2. **Indexing**
   - Multi-index: text, equations, figures, glossary.
   - Store embeddings (dense + symbolic).

3. **Tutor Orchestrator**
   - Socratic loop: question planning, remediation, mastery tracking.

4. **Exercise Engine**
   - Subject-specific templates (code, math, essays).
   - Deterministic seeding for reproducibility.

5. **Grader**
   - Auto (tests for code).
   - Rubric-based (essays/math).
   - Feedback includes "what’s right," "what’s missing," actionable hint.

6. **Progress & Mastery**
   - Track per-skill confidence.
   - Require consistent correctness (e.g., 3/4 attempts).
   - Spaced refresh over time.

7. **Storage**
   - Postgres: chapters, mastery, sessions.
   - Vector DB: Chroma (local), Qdrant/pgvector (cloud).
   - MinIO/S3: PDFs, figures, submissions.

8. **UI/API**
   - SvelteKit frontend.
   - FastAPI backend.
   - REST/GraphQL endpoints.

---

## Tech Stack (opinionated, swappable)

- **Frontend**: SvelteKit + Tailwind + shadcn/ui.
- **Backend**: FastAPI (Python), Redis + RQ for async jobs.
- **DB**: Postgres + Chroma.
- **Object storage**: MinIO locally, S3 cloud.
- **Vector search**: Chroma (MVP), pgvector/Qdrant later.
- **Parsing**: pymupdf, Nougat, pix2tex, Mathpix (paid fallback).
- **Models**: ChatGPT/Claude/Gemini, router by task.

---

## PDF & Equation Handling

1. Extract text/structure → `pymupdf`.
2. Detect equations:
   - Nougat (vision transformer).
   - Fallback: pix2tex.
   - Paid fallback: Mathpix.
3. Normalize LaTeX (spacing, macros).
4. Store LaTeX + PNG/SVG render.
5. Index:
   - Text embeddings for surrounding context.
   - Natural-language gloss for equations.
   - Symbol bag for operator/variable matching.

---

## Retrieval-Augmented Generation (RAG)

- Chunk by logical sections, not fixed tokens.
- Hybrid retrieval (BM25 + dense).
- Boost equation-bearing chunks when math present.
- Include figures, captions, definitions in context.
- Answer style: English + LaTeX + optional “show steps.”

---

## Tutor Loop (state machine)

1. Detect learner state (confidence, errors).
2. Plan micro-goal.
3. Ask probing question.
4. Remediate if wrong.
5. Re-probe in new context.
6. Update mastery.

---

## Exercise Engine

- Templates per subject:
  - CS/Robotics: small coding labs + tests.
  - Math: proofs, problem sets, step-by-step.
  - Humanities: synthesis, essays.
  - Physics: numerical + symbolic.
- Exercises seeded → reproducible.
- Stored in YAML (`goal`, `difficulty`, `rubric`).

---

## Grading

- **Code**: containerized runner, unit tests.
- **Math**: LaTeX diff + rubric.
- **Essay**: rubric + exemplars.

Feedback always contains:
- ✅ Correct parts.
- ❌ Missing/incorrect.
- 🔑 One actionable hint.
- 📖 Reference back to chapter.

---

## Mastery Model

- Per-skill tracking at difficulty bands.
- Rule of consistency: 3/4 correct across time.
- Confidence decays → triggers spaced refresh.
- Mastery visualized as heatmap.

---

## Data Model (simplified)

- `document(id, title, metadata)`
- `chapter(id, document_id, order, title)`
- `node(id, chapter_id, type, text, latex, figure_url)`
- `embedding(node_id, kind, vector)`
- `skill(id, chapter_id, name, prereq[])`
- `attempt(id, user_id, skill_id, type, result, rubric, ts)`
- `mastery(user_id, skill_id, level, confidence)`
- `exercise(id, chapter_id, template, seed, rubric)`
- `submission(id, exercise_id, artifact_url, grade)`

---

## Monetization Options

1. **Open-core** (local OSS, paid hosted).
2. **Freemium SaaS** (limits lifted in paid tier).
3. **Academic licensing** (classroom dashboards).
4. **Consulting/white-label**.

---

## Constraints & Design Rules

- Determinism > Cleverness (seeded exercises).
- Logging all tutor turns for evaluation.
- Subject-specific policies defined in YAML.
- Guardrails: system can ask student for cited passage.
- Keep small helper tools explicit (`run_py_tests`, `render_equation`, etc.).
- Local-first → Cloud upgrade path.

---
