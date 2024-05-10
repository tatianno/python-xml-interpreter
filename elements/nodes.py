from abc import ABC, abstractmethod


class Node(ABC):
    
    def __init__(self, id: str, name: str=None, *args, **kwargs) -> None:
        self.id = id
        self.name = name
        self.performed = False