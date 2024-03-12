import models, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from typing import List
from dependencies import get_db

router = APIRouter()


@router.get("/devices/", response_model=List[schemas.DeviceSchema])
def get_devices(db: Session = Depends(get_db)) -> List[schemas.DeviceSchema]:
    return db.query(models.DeviceModel).all()
