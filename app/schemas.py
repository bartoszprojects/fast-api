from pydantic import BaseModel
from typing import List, get_type_hints

from pydantic_xml import BaseXmlModel, element

from models import DNSServerModel, InterfaceModel, RouteModel, DeviceModel


class DNSServerSchema(BaseXmlModel):
    dns_server: str = element()

    def serialize_orm(self):
        return DNSServerModel(**self.model_dump())


class InterfaceSchema(BaseXmlModel):
    name: str  = element()
    ip_address: str  = element()
    subnet_mask: str  = element()
    status: str  = element()

    def serialize_orm(self):
        return InterfaceModel(**self.model_dump())



class RouteSchema(BaseXmlModel):
    destination: str  = element()
    gateway: str  = element()
    interface_name: str  = element()

    def serialize_orm(self):
        return RouteModel(**self.model_dump())


class DeviceSchema(BaseXmlModel):
    name: str = element()
    type: str = element()
    ip_address: str = element()
    subnet_mask: str = element()
    gateway: str = element()


class InterfacesSchema(BaseXmlModel):
    interface: List[InterfaceSchema] = element()

    def serialize_orm(self):
        return [o.serialize_orm() for o in self.interface]


class RoutesSchema(BaseXmlModel):
    routes: List[RouteSchema] = element()

    def serialize_orm(self):
        return [o.serialize_orm() for o in self.routes]


class DeviceWholeSchema(DeviceSchema):
    dns_servers: List[DNSServerSchema] = element(tag='dns_servers', default_factory=list)
    interfaces: InterfacesSchema = element()
    routing_table: RoutesSchema = element()

    def serialize_orm(self):
        out = {}

        for k, v in self.model_dump().items():
            if isinstance(v, str):
                out[k] = v
            elif isinstance(v, list):
                out[k] = [o.serialize_orm() for o in getattr(self, k)]
            else:
                out[k] = getattr(self, k).serialize_orm()

        return DeviceModel(**out)


class ResponseSchema(BaseXmlModel):
    status: str = element()
