from datetime import datetime
from product.enums import VType, VStatus
from unique_id_generator import UniqueIDGenerator


class Vechile:
    def __init__(
            self,
            vno,
            v_company,
            v_model,
            kmdriven,
            m_date,
            average,
            cc,
            no_of_seat = 4,
            daily_rental_cost = 1000,
            hourly_rental_cost = 200,
            vtype: VType = VType.CAR,
            status: VStatus = VStatus.ACTIVE
            ):
        self.vid = UniqueIDGenerator.next_id()
        self.vno = vno
        self.vtype = vtype
        self.status = status
        self.v_company = v_company
        self.v_model = v_model
        self.kmdriven = kmdriven
        self.m_date = m_date
        self.average = average
        self.cc = cc
        self.daily_rental_cost = daily_rental_cost
        self.hourly_rental_cost = hourly_rental_cost
        self.no_of_seat = no_of_seat
    
    def __str__(self):
        return f"Vechile Details->\n\
        Vechile id: {self.vid}\n\
        vechile number: {self.vno}\n\
        vechile type: {self.vtype}\n\
        vechile company: {self.v_company}\n\
        vechile model: {self.v_model}\n\
        km driven: {self.kmdriven}\n\
        manufacturer date: {self.m_date}\n\
        Average: {self.average}\n\
        CC: {self.cc}\n\
        daily rental cost: {self.daily_rental_cost}\n\
        Hourly rental cost: {self.hourly_rental_cost}\n\
        No of seat: {self.no_of_seat}\n\
        Vechile type: {self.vtype.value}\n\
        Vechile status: {self.status}\n"
    
    def set_vstatus(self, status: VStatus):
        self.status = status
    
    def set_kmdriven(self, kmdriven):
        self.kmdriven = kmdriven
    
    def set_average(self, average):
        self.average = average
    
    def set_daily_rental_cost(self, daily_rental_cost):
        self.daily_rental_cost = daily_rental_cost

    def set_hourly_rental_cost(self, hourly_rental_cost):
        self.hourly_rental_cost = hourly_rental_cost

print(Vechile(123, "TATA", "Safari", 20000, datetime.now(), 20, 500, 7))
print(Vechile(123, "TATA", "Safari", 20000, datetime.now(), 20, 500, 7))
print(Vechile(123, "TATA", "Safari", 20000, datetime.now(), 20, 500, 7))
print(Vechile(123, "TATA", "Safari", 20000, datetime.now(), 20, 500, 7))