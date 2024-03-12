from pydantic import BaseModel
from typing import List
from models import DNSServerModel, InterfaceModel, RouteModel


class DNSServerSchema(BaseModel):
    dns_server: str

    class Meta:
        orm_model = DNSServerModel

    class Config:
        orm_mode = True


class InterfaceSchema(BaseModel):
    name: str
    ip_address: str
    subnet_mask: str
    status: str

    class Meta:
        orm_model = InterfaceModel

    class Config:
        orm_mode = True


class RouteSchema(BaseModel):
    destination: str
    gateway: str
    interface_name: str

    class Meta:
        orm_model = RouteModel

    class Config:
        orm_mode = True


class DeviceSchema(BaseModel):
    name: str
    type: str
    ip_address: str
    subnet_mask: str
    gateway: str

    class Config:
        orm_mode = True


class DeviceWholeSchema(DeviceSchema):
    dns_servers: List[DNSServerSchema]
    interfaces: List[InterfaceSchema]
    routing_table: List[RouteSchema]

    class Config:
        orm_mode = True
