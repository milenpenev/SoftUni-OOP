class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        return

    @property
    def water(self):
        return

    @property
    def painkiller(self):
        return

    @property
    def salves(self):
        return

    def add_survivor(self,survivor):
        pass

    def add_supply(self, supply):
        pass

    def add_medicine(self, medicine):
        pass

    def heal(self, survivor, medicine_type):
        pass

    def sustain(self, survivor, sustenance_type):
        pass

    def next_day(self):
        pass