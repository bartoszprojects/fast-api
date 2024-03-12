import models, schemas, services
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from typing import List
from dependencies import get_db

router = APIRouter()


@router.get("/devices/", response_model=List[schemas.DeviceWholeSchema])
def get_devices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db))-> List[schemas.DeviceWholeSchema]:
    devices = services.get_devices(db, skip=skip, limit=limit)
    return devices

@router.post("/devices/", response_model=schemas.DeviceSchema)
def create_device(device: schemas.DeviceSchema, db: Session = Depends(get_db)):
    return services.create_device(db=db, device=device)


@router.post("/devices/whole-schema", response_model=schemas.DeviceWholeSchema)
def create_whole_schema_device(device: schemas.DeviceWholeSchema, db: Session = Depends(get_db)):
    return services.create_whole_schema_device(db=db, device=device)