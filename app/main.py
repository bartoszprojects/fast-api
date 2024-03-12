from database import SessionLocal
from typing import Generator

from fastapi import FastAPI

app = FastAPI()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"data": "HomePage"}


@app.get("/items/{item}")
def sample_endpoint(item: str):
    return {"sample_item": item}