class Product:

    def __init__(self, cena, nazwa, ID):
        self.cena = cena
        self.nazwa = nazwa
        self.ID = ID

    def print_info(self):
        return f"Produkt {self.nazwa}, ID: {self.ID}, cena {self.cena} PLN"


product = Product(10.99, "woda", 1)
Product.print_info(product)


def test_product():
    product = Product(10.99, "woda", 1)
    assert hasattr(product,"ID")
    assert product.ID==1
    assert product.nazwa=="woda"
    assert product.cena==10.99


def test_product_print_info():
    product = Product(10.99, "woda", 1)
    assert product.print_info()=="Produkt woda, ID: 1, cena 10.99 PLN"
