from sqlalchemy.orm import Session

import models
import schemas

import utils

def get_devices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DeviceModel).offset(skip).limit(limit).all()


def create_device(db: Session, device: schemas.DeviceSchema):
    db_route = models.DeviceModel(**device.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

def create_whole_schema_device(db: Session, device: schemas.DeviceWholeSchema):
    parsed_schema = utils.parse_pydantic_schema(device)
    db_device = models.DeviceModel(**parsed_schema)

    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device