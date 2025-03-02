from EmployeDao import EmaployeDao
from EmployeDo import EmaployeDo
from EmployeDaoImpl import EmaployeDaoImpl

class EmaployeDaoProxy(EmaployeDao):
    def __init__(self):
        self.employee_dao_boj = EmaployeDaoImpl()

    def create(self, client: str, employee: EmaployeDo):
        if client == "ADMIN":
            self.employee_dao_boj.create(client, employee)
            return
        raise Exception("Access Denied!")

    def delete(self, client: str, employe_id: str):
        if client == "ADMIN":
            self.employee_dao_boj.delete(client, employe_id)
            return
        raise Exception("Access Denied!")

    def get(self, client) -> EmaployeDo:
        if client == "ADMIN" or client == "USER":
            self.employee_dao_boj.get(client)
            return
        raise Exception("Access Denied!")

