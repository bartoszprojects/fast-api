from pydantic import BaseModel
from typing import List, Optional
from models import DNSServerModel, InterfaceModel, RouteModel


class DNSServerSchema(BaseModel):
    dns_server: str


class InterfaceSchema(BaseModel):
    name: str
    ip_address: str
    subnet_mask: str
    status: str


class RouteSchema(BaseModel):
    destination: str
    gateway: str
    interface_name: str


class DeviceSchema(BaseModel):
    name: str
    type: str
    ip_address: str
    subnet_mask: str
    gateway: str
    dns_servers: List[DNSServerSchema]
    interfaces: List[InterfaceSchema]
    routing_table: List[RouteSchema]
