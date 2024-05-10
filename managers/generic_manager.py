from abc import ABC, abstractmethod
from exceptions import DoesExistsException


class AbstractManager:

    def __init__(self):
        self._objects = {}

    @abstractmethod
    def set(self, obj) -> None:
        ...
    
    @abstractmethod
    def get(self, id: str) -> object:
        ...
    
    @abstractmethod
    def exists(self, id: str) -> bool:
        ...

    @abstractmethod
    def remove(self, id: str) -> None:
        ...


class GenericManager(AbstractManager):

    def set(self, obj: object) -> None:
        self._objects[obj.id] = obj
    
    def get(self, id: str) -> object:
        return self._objects.get(id)
    
    def exists(self, id: str) -> bool:
        return bool(id in self._objects)
    
    def remove(self, id: str) -> None:
        if not self.exists(id):
            raise DoesExistsException(f'obj {id} not found!')
        
        del self._objects[id]