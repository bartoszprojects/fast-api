from pydantic import BaseModel
from typing import List

from pydantic_xml import BaseXmlModel, element

from models import DNSServerModel, InterfaceModel, RouteModel


class DNSServerSchema(BaseXmlModel):
    dns_server: str  = element()

    class Meta:
        orm_model = DNSServerModel

    class Config:
        orm_mode = True


class InterfaceSchema(BaseXmlModel):
    name: str  = element()
    ip_address: str  = element()
    subnet_mask: str  = element()
    status: str  = element()

    class Meta:
        orm_model = InterfaceModel

    class Config:
        orm_mode = True



class RouteSchema(BaseXmlModel):
    destination: str  = element()
    gateway: str  = element()
    interface_name: str  = element()

    class Meta:
        orm_model = RouteModel

    class Config:
        orm_mode = True


class DeviceSchema(BaseXmlModel):
    name: str = element()
    type: str = element()
    ip_address: str = element()
    subnet_mask: str = element()
    gateway: str = element()

    class Config:
        orm_mode = True

class InterfacesSchema(BaseXmlModel):
    interface: List[InterfaceSchema] = element()
class RoutesSchema(BaseXmlModel):
    routes: List[RouteSchema] = element()



class DeviceWholeSchema(DeviceSchema):
    dns_servers: List[DNSServerSchema] = element()
    interfaces: InterfacesSchema = element()
    routing_table: RoutesSchema = element()

    class Config:
        orm_mode = True


class ResponseSchema(BaseXmlModel):
    status: str = element()
