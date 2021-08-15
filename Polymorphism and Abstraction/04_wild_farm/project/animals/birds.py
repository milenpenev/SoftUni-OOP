from food import Meat
from project.animals.animal import Bird


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not type(food) == Meat:
            return f"Owl does not eat {type(food).__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity

class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self,food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
