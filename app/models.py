from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class DeviceModel(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    ip_address = Column(String)
    subnet_mask = Column(String)
    gateway = Column(String)

    dns_servers = relationship("DNSServerModel", back_populates="device")
    interfaces = relationship("InterfaceModel", back_populates="device")
    routing_table = relationship("RouteModel", back_populates="device")


class DNSServerModel(Base):
    __tablename__ = 'dns_servers'

    id = Column(Integer, primary_key=True)
    dns_server = Column(String)
    device_id = Column(Integer, ForeignKey('devices.id'))

    device = relationship("DeviceModel", back_populates="dns_servers")


class InterfaceModel(Base):
    __tablename__ = 'interfaces'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip_address = Column(String)
    subnet_mask = Column(String)
    status = Column(String)
    device_id = Column(Integer, ForeignKey('devices.id'))

    device = relationship("DeviceModel", back_populates="interfaces")


class RouteModel(Base):
    __tablename__ = 'routing_table'

    id = Column(Integer, primary_key=True)
    destination = Column(String)
    gateway = Column(String)
    interface = Column(String)
    device_id = Column(Integer, ForeignKey('devices.id'))

    device = relationship("DeviceModel", back_populates="routing_table")
