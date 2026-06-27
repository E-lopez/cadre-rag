from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = FastAPI(title="Cadre AI API")


@app.get("/health")
def health():
    return {"status": "ok"}
