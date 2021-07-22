from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for el in self.products:
            if el == product_name:
                return el

    def remove(self, product_name):
        for el in self.products:
            if el.name == product_name:
                self.products.remove(el)

    def __repr__(self):
        result = []
        for el in self.products:
            result.append(f'{el.name}: {el.quantity}')
        new_line = "\n"
        return f'{new_line.join(x for x in result)}'

