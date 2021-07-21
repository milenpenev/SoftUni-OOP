from project.car import Car


class SportCar(Car):
    def __init__(self, fuel, horse_power, DEFAULT_FUEL_CONSUMPTION = 10):
        super().__init__(fuel, horse_power, DEFAULT_FUEL_CONSUMPTION = 10)
        self.fuel_consumption = DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if kilometers <= self.fuel / self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption