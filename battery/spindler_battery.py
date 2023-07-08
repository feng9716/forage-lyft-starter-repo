from battery.battery import Battery
from datetime import datetime
from utils.utils import add_years_to_date


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_year_limit = 2

    def needs_service(self) -> bool:
        service_threshold_date = add_years_to_date(
            self.last_service_date, self.service_year_limit
        )

        return datetime.today().date() > service_threshold_date
