class Product:
    def __init__(self, ID, nazwa, cena):
        self.cena = cena
        self.nazwa = nazwa
        self.ID =ID

class Basket(Product):
    def __init__(self):
        pass

    def add_product(self, ile):
        basket=Basket(product.ID, product.nazwa, product.cena)


    def count_total_price(self):
        pass

    def generate_report(self):
        pass

basket=Basket()

product=Product(1,"Woda",10.99)
basket.add_product(product,5)
basket.count_total_price()

basket.generate_report()

