from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv, find_dotenv

from app.routes import index, query

load_dotenv(find_dotenv())

app = FastAPI(title="Cadre AI API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.router, prefix="/v1")
app.include_router(query.router, prefix="/v1")


@app.get("/health")
def health():
    return {"status": "ok"}
