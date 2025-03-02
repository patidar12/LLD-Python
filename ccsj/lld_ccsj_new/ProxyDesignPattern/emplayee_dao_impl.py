from employee_do import EmployeeDo
from employee_dao import EmployeeDao
class EmployeeDaoImpl(EmployeeDao):
    def create(self, client: str, employee: EmployeeDo):
        print(f"Employee: {employee.name} created")
    def delete(self, client: str, emp_id: int):
        print(f"Employee: {emp_id} deleted")
    def get(self, client: str):
        print("Employe fetch succesfull")
        return EmployeeDo("Test Proxy")
