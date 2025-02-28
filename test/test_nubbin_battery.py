import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery

class testNubbinBattery(unittest.testCase):
    def test_needs_service_true(self):
        today = date.today().date()
        last_service_date = date.fromisoformat("2014-06-16")
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())      

    def test_needs_service_false(self):
        today = date.today().date()
        last_service_date = date.fromisoformat("2021-06-16")
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())   