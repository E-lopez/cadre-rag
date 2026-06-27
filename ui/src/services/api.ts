const API_BASE = import.meta.env.VITE_API_BASE ?? 'http://localhost:8000'

export interface QueryResponse {
  answer: string
  sources: string[]
}

export interface IndexResponse {
  indexed: number
  message: string
}

export async function createIndex(): Promise<IndexResponse> {
  const res = await fetch(`${API_BASE}/v1/create-index`, { method: 'POST' })
  if (!res.ok) throw new Error('Failed to initialize knowledge base.')
  return res.json() as Promise<IndexResponse>
}

export async function queryKnowledgeBase(question: string): Promise<QueryResponse> {
  const res = await fetch(`${API_BASE}/v1/query`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question }),
  })
  if (!res.ok) {
    const body = await res.json().catch(() => ({})) as { detail?: string }
    throw new Error(body.detail ?? 'Request failed.')
  }
  return res.json() as Promise<QueryResponse>
}
