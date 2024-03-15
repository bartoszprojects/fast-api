from pydantic import BaseModel
from typing import List, get_type_hints

from pydantic_xml import BaseXmlModel, element, RootXmlModel

from models import DNSServerModel, InterfaceModel, RouteModel, DeviceModel


class DNSServerSchema(BaseXmlModel):
    dns_server: str

    def serialize_orm(self):
        return DNSServerModel(**self.model_dump())


class DNSServersSchema(BaseXmlModel):
    dns_server: List[DNSServerSchema] = element()

    def serialize_orm(self):
        return [o.serialize_orm() for o in self.dns_server]


class InterfaceSchema(BaseXmlModel):
    name: str = element()
    ip_address: str = element()
    subnet_mask: str = element()
    status: str = element()

    def serialize_orm(self):
        return InterfaceModel(**self.model_dump())


class RouteSchema(BaseXmlModel):
    destination: str = element()
    gateway: str = element()
    interface: str = element()

    def serialize_orm(self):
        return RouteModel(**self.model_dump())


class BaseDeviceSchema(BaseXmlModel, tag='DeviceSchema-Input'):
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
    route: List[RouteSchema] = element()

    def serialize_orm(self):
        return [o.serialize_orm() for o in self.route]


class DeviceSchema(BaseDeviceSchema, tag='DeviceSchema-Input'):
    dns_servers: DNSServersSchema = element()
    interfaces: InterfacesSchema = element()
    routing_table: RoutesSchema = element()

    # to handle nested data I created my own method that mapping each Model Children and inside
    # it makes 'model_dump()'
    def serialize_orm(self):
        out = {}

        for k, v in self.model_dump().items():
            if isinstance(v, str):
                out[k] = v
            else:
                out[k] = getattr(self, k).serialize_orm()

        # here I return Model Schema with mapped & dumped data and I forward it to service to make db action
        return DeviceModel(**out)


class ResponseSchema(BaseXmlModel):
    status: str = element()
