class Product:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

    def print_info(self):
        return f'Produkt {self.name}, id: {self.ID}, cena: {self.price} PLN'


class Basket_entry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity


class Basket:
    def __init__(self):
        self.entries = []

    def __str__(self):
        return "Basket"

    def add_product(self, product, quantity):
        basket_entry = Basket_entry(product, quantity)
        self.entries.append(basket_entry)

    def count_total_price(self):
        sum_ = 0
        for entry in self.entries:
            sum_ += entry.count_price()
        return sum_

    def generate_report(self):
        txt1 = f'''Produkty w koszyku:\n'''
        txt2 = str()
        for e in self.entries:
            txt2 += f'''- {e.product.name} ({e.product.ID}), cena: {e.product.price} x {e.quantity}\n'''
        txt3 = '''W sumie: {}'''
        return txt1 + txt2 + txt3.format(self.count_total_price())


basket = Basket()
prod1 = Product(1, "Woda", 10)
basket.add_product(prod1, 5)
prod2 = Product(2, "Wóda", 6)
basket.add_product(prod2, 11)
print(basket.count_total_price())
print(basket.generate_report())


def test_create_basket():
    basket = Basket()
    assert str(basket) == "Basket"

def test_basket_count_total_price():
    basket = Basket()
    prod1 = Product(1, "Woda", 5)
    basket.add_product(prod1, 10.00)
    assert basket.count_total_price() == 50
    prod2 = Product(2, "Wóda", 6)
    basket.add_product(prod2, 11.00)
    assert basket.count_total_price() == 116

def test_basket_generate_report():
    basket = Basket()
    prod1 = Product(1, "Woda", 10)
    basket.add_product(prod1, 5)
    assert basket.generate_report() == '''Produkty w koszyku:
- Woda (1), cena: 10 x 5
W sumie: 50'''

def test_basket_generate_report1():
    basket = Basket()
    prod1 = Product(1, "Woda", 10)
    basket.add_product(prod1, 5)
    prod2 = Product(2, "Wóda", 6)
    basket.add_product(prod2, 11)
    assert basket.generate_report() == '''Produkty w koszyku:
- Woda (1), cena: 10 x 5
- Wóda (2), cena: 6 x 11
W sumie: 116'''
