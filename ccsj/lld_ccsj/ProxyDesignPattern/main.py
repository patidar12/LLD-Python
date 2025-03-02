from EmployeDaoProxy import EmaployeDaoProxy
from EmployeDo import EmaployeDo

class Main:

    def manage_employee(self):
        emp_proxy = EmaployeDaoProxy()
        emp = EmaployeDo()
        emp_proxy.create(client="ADMIN", employee=emp)
        emp_proxy.delete(client="ADMIN", employe_id=emp.emp_id)
        emp_proxy.get(client="USER")



Main().manage_employee()