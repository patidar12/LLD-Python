from abc import ABC, abstractmethod

from EmployeDo import EmaployeDo

class EmaployeDao(ABC):

    @abstractmethod
    def create(self, client: str, employee: EmaployeDo):
        pass

    @abstractmethod
    def delete(self, client: str, employe_id: str):
        pass

    @abstractmethod
    def get(self, client: str) -> EmaployeDo:
        pass
