from database import SessionLocal, engine
from typing import Generator
from fastapi import FastAPI
import models
from views import router as api_router

app = FastAPI()

# temporary auto-sync here => later using alembic
models.Base.metadata.create_all(bind=engine)

app.include_router(api_router)

