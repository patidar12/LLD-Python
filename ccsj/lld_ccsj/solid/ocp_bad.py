from srp import Invoice

class InvoiceDao:
    def __init__(self, invoice: Invoice):
        self.__invoice: Invoice = invoice
    
    def saveToDB(self) -> None:
        print("saved to db")
    
    def savetoFile(self) -> None:
        print("save to file")


''''
OCP: open closed principle.
Open for extension but closed for modification

InvoiceDao class already having saveToDB method and code of this class is live.
Later we get a requirement to sane the invoice to FIle.
We modified the existing class that already live that is voilating the OCP.

As the OCP code is open for extension but closed for modification.

please check ocp.py for Correct implmantation of above problem.
'''