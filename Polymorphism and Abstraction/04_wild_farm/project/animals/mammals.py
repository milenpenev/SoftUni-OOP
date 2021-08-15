from animals.animal import Mammal
from food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not type(food) == Vegetable or not type(food) == Fruit:
            return f"Mouse does not eat {type(food).__name__}!"
        self.weight += 0.1 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not type(food) == Meat:
            return f"Dog does not eat {type(food).__name__}!"
        self.weight += 0.4 * food.quantity
        self.food_eaten += food.quantity

class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not type(food) == Vegetable or not type(food) == Meat:
            return f"Cat does not eat {type(food).__name__}!"
        self.weight += 0.3 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not type(food) == Meat:
            return f"Tiger does not eat {type(food).__name__}!"
        self.weight += 1 * food.quantity
        self.food_eaten += food.quantity
