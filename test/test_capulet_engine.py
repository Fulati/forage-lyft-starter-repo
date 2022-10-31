import unittest
from datetime import date
from engine import capulet_engine

class testCapuletEngine(unittest.testCase):
    def test_needs_service_true(self):
        current_mileage = 59000
        last_service_mileage = 19000
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())      

    def test_needs_service_false(self):
        current_mileage = 59000
        last_service_mileage = 49000
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())   