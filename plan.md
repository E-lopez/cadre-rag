# Engineering Plan: [Project Name]

> **What we are building:** A monorepo containing a FastAPI backend and a React frontend.
> **How we are working with AI:** We are keeping the AI on a short leash by separating frontend and backend context so it doesn't waste tokens, using shortcodes for tests, and logging when it spawns sub-tasks.

---

## 1. Project Folders & AI Context Boundaries
To stop the AI from getting confused or reading files it shouldn't be touching, we strictly isolate its memory using our folder setups. 

* **Backend Apps:** Located in `api/app/`. The AI only reads backend rules here.
* **Frontend Apps:** Located in `ui/src/`. The AI only reads UI rules here.

---

## 2. Step-by-Step Implementation

### Phase 1: Backend Setup
*Goal: set up the backend structure and external clients*
- [ ] **Milestone 1: Core API**
  * **Setup Clients:** 
    - AWS Bedrock client using `boto3` (authenticating via local `.env` access keys).
    - In-memory ChromaDB instance (`chromadb.EphemeralClient()`) for vector storage.
- [ ] **Milestone 2: Core API**
  * **Guardrails Services** (`app/services/guardrails.py`)
    - Build `run_query_guardrails(query: str) -> bool` pipeline.
    - Use `GUARDRAIL_PROHIBITED_PROMPT` from `app/prompts/guardrails.py` to model `meta.llama3-8b-instruct-v1:0`.
    - Stub the function to return `True` (ALLOWED) for this milestone's boilerplate test.
- [ ] **Milestone 3: Core API**
  * **Endpoints to Build:**
    - GET `/health` -> Simple uptime status check.
    - POST `/v1/create-index` -> Reads and indexes the raw JSON data located at `api/app/data/cadre_kb.json`.
    - POST `/v1/query` -> Accepts a question, uses `run_query_guardrails()`to identify restricted questions in it, if the returned value is `ALLOWED` then it embeds it via Bedrock Titan, searches ChromaDB using cosine similarity, and synthesizes a response using Claude Sonnet 4.6.
  * **Context Boundary:** All changes isolated inside `api/app/`.

  * **Planned File Structure:**
    `app/main.py` - Application entry point and router inclusion, includes GET /health endpoint.
    `app/dependencies/bedrock.py` - Independent AWS Bedrock client initialization using boto3.
    `app/dependencies/chroma.py` - Independent in-memory ChromaDB EphemeralClient initialization.
    `app/routes/query.py` - POST /v1/query endpoint with the guardrail logic wrapper. This endpoint will use the 'prohibited topics guardrail' as defined by `GUARDRAIL_PROHIBITED_PROMPT` from `app/functions/prompts.py` to model `meta.llama3-8b-instruct-v1:0`.
    `app/routes/index.py` - POST /v1/create-index endpoint.
    `app/prompts/prompts.py` - Llama 3 guardrail prompt constants.

### Phase 2: Ui setup

### Phase 3: Guardrailing and Evals

### Phase 4: 

---

## 4. Work Log & AI Context Notes
*This is where we log any time the AI shifts strategy, runs into an error, or spawns an independent sub-task to solve a problem.*

* **[2026-06-27]** Initialized repository structure and set up folder-level rules.
- **Hardened**: Manually wrapped AWS Bedrock, ChromaDB client initialization (`get_bedrock_client`) in a `try/except` block.
