from employee_dao_proxy import EmployeeDaoProxy
from employee_do import EmployeeDo

class EmployeeMangement:
    def operations(self):
        emp_proxy = EmployeeDaoProxy()
        emp_proxy.create("ADMIN", EmployeeDo("Test User"))
        emp_proxy.delete("ADMIN", 1)
        print(emp_proxy.get("USER").name)


EmployeeMangement().operations()