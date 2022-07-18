from abc import abstractmethod
import enum

from pydantic import BaseModel


class ContextType(str, enum.Enum):
    client = 'client'
    server = 'server'


class Entity(BaseModel):
    type: ContextType = None


class Interface:
    def __init__(self, entity: Entity, connector=None):
        self.entity = entity
        self.connector = connector

    @abstractmethod
    def is_runnable(self):
        pass


class Server(Interface):
    def is_runnable(self) -> bool:
        return self.entity.type == ContextType.server


class Client(Interface):
    def is_runnable(self) -> bool:
        return self.entity.type == ContextType.client
