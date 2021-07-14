class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if not self.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price += price_per_ingredient * quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price += price_per_ingredient * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient, quantity, price_per_ingredient):
        if not self.ordered:
            if ingredient in self.ingredients:
                if self.ingredients[ingredient] < quantity:
                    return f"Please check again the desired quantity of {ingredient}!"
                self.ingredients[ingredient] -= quantity
                self.price -= price_per_ingredient * quantity
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        else:
            result = ''
            self.ordered = True
            index = 0
            for k, v in self.ingredients.items():
                index += 1
                if index == len(self.ingredients):
                    result += f"{k}: {v} "
                else:
                    result += f"{k}: {v}, "
            return f"You've ordered pizza {self.name} prepared with {result}and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

