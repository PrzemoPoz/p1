class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.czas = 0

    def register_time(self, czas):
        self.czas += czas

    def pay_salary(self):
        temp = self.czas
        if self.czas > 8:
            self.czas = 0
            return (temp - 8) * self.stawka * 2 + 8 * self.stawka
        else:
            self.czas = 0
            return temp * self.stawka

employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.pay_salary()
employee.pay_salary()
employee.register_time(10)
employee.pay_salary()



def test_pay_salary():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary()==500.0

def test_pay_salary1():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary()==500.0
    assert employee.pay_salary() == 0.0

def test_pay_salary2():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.register_time(5)
    assert employee.pay_salary() == 1200.0
