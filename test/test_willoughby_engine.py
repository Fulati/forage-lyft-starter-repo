import unittest
from datetime import date
from engine import willoughby_engine

class testWilloughbyEngine(unittest.testCase):
    def test_needs_service_true(self):
        current_mileage = 89000
        last_service_mileage = 19000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())      

    def test_needs_service_false(self):
        current_mileage = 59000
        last_service_mileage = 49000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())   