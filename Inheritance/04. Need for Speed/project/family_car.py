from project.car import Car


class FamilyCar(Car):
    def __init__(self, fuel, horse_power, DEFAULT_FUEL_CONSUMPTION = 3):
        super().__init__(fuel, horse_power, DEFAULT_FUEL_CONSUMPTION = 3)
        self.fuel_consumption = DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if kilometers <= self.fuel / self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption