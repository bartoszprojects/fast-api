import dataclasses

from fastapi_xml import XmlBody, XmlRoute
from pydantic_xml import element, BaseXmlModel

import schemas, services
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from dependencies import get_db

router = APIRouter()
router.route_class = XmlRoute


@router.post("/devices/", response_model=schemas.DeviceDataClass)
def create_device(device: schemas.DeviceDataClass = XmlBody(), db: Session = Depends(get_db)):
    return services.create_device(db=db, device=device)


@router.post("/devices/whole_schema", response_model=schemas.ResponseSchemaDataClass)
def create_device_whole_schema(device: schemas.DeviceDataClass = XmlBody(), db: Session = Depends(get_db)):
    services.create_whole_schema_device(db, device)
    return schemas.ResponseSchemaDataClass(status='ok')

