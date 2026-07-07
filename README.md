# Ephemeral Multi-Model RAG Monolith with AI Context Layering

A high-performance, cost-optimized Retrieval-Augmented Generation (RAG) monolith featuring automated multi-model guardrails, an ephemeral in-memory vector storage layer, and asynchronous LLM-as-a-Judge evaluations.

This repository serves as a concrete proof-of-concept demonstrating how to build enterprise-grade AI features for small and mid-sized businesses (SMBs) with strict unit economics, totalizing a development and stress-testing runtime cost of just **$5.16**.

---

## 🎯 The Core Innovation: AI Context Isolation (`CLAUDE.md`)

When building with next-gen AI coding tools like **Claude Code** or **Cursor**, context window bloat is the primary driver of high API bills and instruction drift. If an AI agent reads frontend component constraints while writing backend routers, it wastes tokens and generates buggy code.

This project introduces a **Layered Markdown Context Framework** that keeps the AI on a short leash by mapping specific engineering boundaries straight to their structural domains:

*   **`./CLAUDE.md` (Root):** Controls global monorepo conventions, explicit Git branch workflows, strict conventional commits, secrets protection, and data layer boundaries.
*   **`./api/CLAUDE.md`:** Sandboxes the AI agent into Python FastAPI development. Restricts it to Pydantic v2 schemas, absolute imports, boto3 Bedrock profiles, and domain-grouped prompts.
*   **`./ui/CLAUDE.md`:** Restricts the agent to TypeScript interfaces, presentation-focused React components, and strict state management via React Context + `useReducer` to eliminate prop-drilling.

*By separating contexts, the AI agent only reads rules relevant to the file it is actively modifying. Token consumption scales linearly rather than exponentially.*

---

## 🏗️ System Architecture & Tech Stack

This repository is built as a unified monolith to eliminate networking overhead, deployment complexity, and cross-origin latency.

### 🛠️ The Tech Stack
*   **Frontend:** Vite + React + TypeScript + Tailwind CSS (Isolated inside `ui/src/`).
*   **Backend:** FastAPI + Python (Isolated inside `api/app/`).
*   **Vector Database:** Ephemeral, zero-disk instance via `chromadb.EphemeralClient()`.
*   **Guardrails Firewall:** `meta.llama3-8b-instruct-v1:0` via Amazon Bedrock (Interceptors for prohibited topics before invoking expensive downstream generation).
*   **Embeddings Engine:** `amazon.titan-embed-text-v2:0` for precise semantic search.
*   **Synthesis & Evaluation:** `us.anthropic.claude-sonnet-4-6` via cross-region inference profiles for output synthesis and asynchronous RAG Triad judging.

---

## 📂 Repository Navigation

> ⚠️ **Developer Note:** This repository is an agile, fast-paced MVP built in a single intensive session. While secondary folders contain experimental scrap files and multi-domain discovery tools, the core production-ready logic is strictly isolated below:
