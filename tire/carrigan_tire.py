from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.wear_threshold = 0.9

    def needs_service(self):
        wear_count = 0
        for _ in self.tire_wear:
            if _ > self.wear_threshold:
                wear_count += 1

        return wear_count >= 1
