from employee_do import EmployeeDo
from employee_dao import EmployeeDao
from emplayee_dao_impl import EmployeeDaoImpl

class EmployeeDaoProxy(EmployeeDao):
    def __init__(self):
        self.employee_dao_impl = EmployeeDaoImpl()

    def create(self, client: str, employee: EmployeeDo):
        if client == "ADMIN":
            self.employee_dao_impl.create(client, employee)
            return
        raise Exception("Access Denied")
    def delete(self, client: str, emp_id: int):
        if client == "ADMIN":
            self.employee_dao_impl.delete(client, emp_id)
            return
        raise Exception("Access Denied")
    def get(self, client: str):
        if client in ["ADMIN", "USER"]:
            return self.employee_dao_impl.get(client)
        return Exception("Access Denied")
