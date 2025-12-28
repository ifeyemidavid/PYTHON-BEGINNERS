from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_info(self):
        pass