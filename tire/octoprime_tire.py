from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.wear_threshold = 3

    def needs_service(self):
        total_wear = 0
        for _ in self.tire_wear:
            total_wear += _

        return total_wear > self.wear_threshold
