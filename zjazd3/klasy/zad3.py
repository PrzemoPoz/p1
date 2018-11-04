class ElectricCar:
    def __init__(self, bat):
        self.bat = bat

    def drive(self, km):
        if self.bat < km:
            temp = self.bat
            self.bat = 0
            return temp
        else:
            temp = km
            self.bat -= km
            return temp

    def charge(self):
        self.bat += 50
        return self.bat

def test_electric():
    car = ElectricCar(100)
    assert car.drive(70) == 70

def test_electric1():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50
