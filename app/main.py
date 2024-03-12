from database import SessionLocal, engine
from typing import Generator
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, FastAPI
import models, schemas
from typing import List

app = FastAPI()

# temporary auto-sync here => later using alembic
models.Base.metadata.create_all(bind=engine)

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


@app.get("/devices/", response_model=List[schemas.DeviceSchema])
def get_devices(db: Session = Depends(get_db)) -> List[schemas.DeviceSchema]:
    return db.query(models.DeviceModel).all()
