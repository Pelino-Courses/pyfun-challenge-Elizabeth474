from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str):
       
        self.name = name

    @abstractmethod
    def get_role(self) -> str:
        pass
