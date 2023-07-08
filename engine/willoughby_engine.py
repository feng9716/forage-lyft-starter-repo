from engine.engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.service_mileage_limit = 60000

    def needs_service(self):
        return (
            self.current_mileage - self.last_service_mileage
            > self.service_mileage_limit
        )
