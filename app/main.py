from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"data": "HomePage"}


@app.get("/items/{item}")
def sample_endpoint(item: str):
    return {"sample_item": item}