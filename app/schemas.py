import dataclasses
from dataclasses import field
from typing import List
import models


# Define the equivalent dataclass for DNSServerSchema
@dataclasses.dataclass
class DNSServerDataClass:
    dns_server: str = dataclasses.field(metadata={"name": "dns_server", "type": "Element"})

    def serialize_orm(self):
        return models.DNSServerModel(dns_server=self.dns_server)

# Define the equivalent dataclass for DNSServersSchema
@dataclasses.dataclass
class DNSServersDataClass:
    dns_server: List[DNSServerDataClass] = dataclasses.field(default_factory=list)

    def serialize_orm(self):
        return [o.serialize_orm() for o in self.dns_server]

# Define the equivalent dataclass for InterfaceSchema
@dataclasses.dataclass
class InterfaceDataClass:
    name: str = dataclasses.field(metadata={"name": "name", "type": "Element"})
    ip_address: str = dataclasses.field(metadata={"name": "ip_address", "type": "Element"})
    subnet_mask: str = dataclasses.field(metadata={"name": "subnet_mask", "type": "Element"})
    status: str = dataclasses.field(metadata={"name": "status", "type": "Element"})

    def serialize_orm(self):
        return models.InterfaceModel(name=self.name, ip_address=self.ip_address, subnet_mask=self.subnet_mask, status=self.status)

# Define the equivalent dataclass for RouteSchema
@dataclasses.dataclass
class RouteDataClass:
    destination: str = dataclasses.field(metadata={"name": "destination", "type": "Element"})
    gateway: str = dataclasses.field(metadata={"name": "gateway", "type": "Element"})
    interface: str = dataclasses.field(metadata={"name": "interface", "type": "Element"})

    def serialize_orm(self):
        return models.RouteModel(destination=self.destination, gateway=self.gateway, interface=self.interface)

# Define the equivalent dataclass for BaseDeviceSchema
@dataclasses.dataclass
class BaseDeviceDataClass:
    name: str = dataclasses.field(metadata={"name": "name", "type": "Element"})
    type: str = dataclasses.field(metadata={"name": "type", "type": "Element"})
    ip_address: str = dataclasses.field(metadata={"name": "ip_address", "type": "Element"})
    subnet_mask: str = dataclasses.field(metadata={"name": "subnet_mask", "type": "Element"})
    gateway: str = dataclasses.field(metadata={"name": "gateway", "type": "Element"})

# Define the equivalent dataclass for InterfacesSchema
@dataclasses.dataclass
class InterfacesDataClass:
    interface: List[InterfaceDataClass] = dataclasses.field(default_factory=list)

    def serialize_orm(self):
        return [o.serialize_orm() for o in self.interface]

# Define the equivalent dataclass for RoutesSchema
@dataclasses.dataclass
class RoutesDataClass:
    route: List[RouteDataClass] = dataclasses.field(default_factory=list)

    def serialize_orm(self):
        return [o.serialize_orm() for o in self.route]

# Define the equivalent dataclass for DeviceSchema
@dataclasses.dataclass
class DeviceDataClass:
    name: str
    type: str
    ip_address: str
    subnet_mask: str
    gateway: str
    dns_servers: DNSServersDataClass
    interfaces: InterfacesDataClass
    routing_table: RoutesDataClass

    def serialize_orm(self):
        return models.DeviceModel(name=self.name, type=self.type, ip_address=self.ip_address, subnet_mask=self.subnet_mask,
                           gateway=self.gateway, dns_servers=self.dns_servers.serialize_orm(),
                           interfaces=self.interfaces.serialize_orm(), routing_table=self.routing_table.serialize_orm())

@dataclasses.dataclass
class ResponseSchemaDataClass:
    status: str = dataclasses.field(metadata={"name": "status", "type": "Element"})

