class Vehicle:
    def __init__(self, fuel, horse_power, DEFAULT_FUEL_CONSUMPTION = 1.25):
        self.horse_power = horse_power
        self.fuel = fuel
        self.fuel_consumption = DEFAULT_FUEL_CONSUMPTION
        self.DEFAULT_FUEL_CONSUMPTION = DEFAULT_FUEL_CONSUMPTION

    def drive(self,kilometers):
        if kilometers <= self.fuel / self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption

