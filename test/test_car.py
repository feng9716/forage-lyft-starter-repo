import os
import sys

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)

from datetime import datetime

from utils.utils import add_years_to_date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car_factory import CarFactory
import unittest


class TestTires(unittest.TestCase):
    def test_carrigan_tire_should_be_serviced(self):
        tire_wear = [0, 0.9, 0.5, 0.99]
        carrigan_tire = CarriganTire(tire_wear)
        self.assertTrue(carrigan_tire.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        tire_wear = [0, 0.3, 0.1, 0.2]
        carrigan_tire = CarriganTire(tire_wear)
        self.assertFalse(carrigan_tire.needs_service())

    def test_octoprime_tire_should_be_serviced(self):
        tire_wear = [0.5, 0.9, 0.8, 0.99]
        octoprime_tire = OctoprimeTire(tire_wear)
        self.assertTrue(octoprime_tire.needs_service())

    def test_octoprime_tire_should_not_be_serviced(self):
        tire_wear = [0.1, 0.9, 0.5, 0.99]
        octoprime_tire = OctoprimeTire(tire_wear)
        self.assertFalse(octoprime_tire.needs_service())


class TestBatteries(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        battery = NubbinBattery(
            datetime.today().date(), add_years_to_date(datetime.today().date(), -9)
        )
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        battery = NubbinBattery(
            datetime.today().date(), add_years_to_date(datetime.today().date(), -2)
        )

        self.assertFalse(battery.needs_service())

    def test_spindler_battery_should_be_serviced(self):
        battery = SpindlerBattery(
            datetime.today().date(), add_years_to_date(datetime.today().date(), -5)
        )
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        battery = SpindlerBattery(
            datetime.today().date(), add_years_to_date(datetime.today().date(), -1)
        )
        self.assertFalse(battery.needs_service())


class TestEngines(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        engine = CapuletEngine(50000, 5000)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        engine = CapuletEngine(10000, 5000)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_should_be_serviced(self):
        engine = WilloughbyEngine(100000, 5000)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(20000, 5000)
        self.assertFalse(engine.needs_service())


class TestCalliope(unittest.TestCase):
    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 15000
        last_service_mileage = 10000
        tire_wear = [0, 0.3, 0.5, 0.1]

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, tire_wear
        )
        self.assertFalse(car.battery.needs_service())
        self.assertFalse(car.engine.needs_service())
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 15000
        last_service_mileage = 10000
        tire_wear = [0, 0.3, 0.5, 0.1]

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, tire_wear
        )
        self.assertFalse(car.battery.needs_service())
        self.assertFalse(car.engine.needs_service())
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 15000
        last_service_mileage = 10000
        tire_wear = [0, 0.3, 0.5, 0.1]

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, tire_wear
        )
        self.assertFalse(car.battery.needs_service())
        self.assertFalse(car.engine.needs_service())
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 15000
        last_service_mileage = 10000
        tire_wear = [0, 0.3, 0.5, 0.1]

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, tire_wear
        )
        self.assertFalse(car.battery.needs_service())
        self.assertFalse(car.engine.needs_service())
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 15000
        last_service_mileage = 10000
        tire_wear = [0, 0.3, 0.5, 0.1]

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, tire_wear
        )
        self.assertFalse(car.battery.needs_service())
        self.assertFalse(car.engine.needs_service())
        self.assertFalse(car.needs_service())


if __name__ == "__main__":
    unittest.main()
