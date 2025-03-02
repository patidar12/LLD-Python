from employee_do import EmployeeDo
from abc import ABC, abstractmethod
class EmployeeDao(ABC):
    @abstractmethod
    def create(self, client: str, eployee: EmployeeDo): pass
    @abstractmethod
    def delete(self, client: str, emp_id: int): pass
    @abstractmethod
    def get(self, client: str): pass
