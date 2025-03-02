from EmployeDao import EmaployeDao
from EmployeDo import EmaployeDo

class EmaployeDaoImpl(EmaployeDao):

    def create(self, client: str, employee: EmaployeDo):
        print("Created new row in Employee table")

    def delete(self, client: str, employe_id: str):
        print("Deleted row in Employee table")

    def get(self, client: str) -> EmaployeDo:
        print("fetching data from DB")
        return EmaployeDo()

