from database import SessionLocal, engine
from typing import Generator
from fastapi import FastAPI
import models
from views import router as api_router

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)
# replaced by alembic command: python3 -m alembic upgrade head

app.include_router(api_router)

