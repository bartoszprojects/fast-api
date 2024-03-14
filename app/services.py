import xmltodict
from sqlalchemy.orm import Session

import models
import schemas

import utils

def get_devices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DeviceModel).offset(skip).limit(limit).all()


def create_device(db: Session, device: schemas.DeviceSchema):

    db_route = models.DeviceModel(**device.model_dump())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return device


def create_whole_schema_device(db: Session, device: schemas.DeviceWholeSchema):

    print(device)

    db_device = device.serialize_orm()

    print(db_device.dns_servers)

    db.add(db_device)
    db.commit()
    db.refresh(db_device)
