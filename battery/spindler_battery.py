from battery import Battery
from car import Car

class SpindlerBattery(Car, Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_needs_serviced(self):
        if (self.last_service_date.year + 2) <= self.current_date:
            return True
        else:
            return False
