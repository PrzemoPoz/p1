class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.czas = 0
    def register_time(self, czas):
        self.czas += czas

    def pay_salary_wob(self):
        temp = self.czas
        if self.czas > 8:
            self.czas = 0
            return (temp - 8) * self.stawka * 2 + 8 * self.stawka
        else:
            self.czas = 0
            return temp * self.stawka

class PremiumEmployee(Employee):
    def __init__ (self,imie,nazwisko,stawka):
        super().__init__(imie, nazwisko,stawka)
        self.bon=0

    def give_bonus(self, bon):
        self.bon=bon
        if bon>0:
            return bon
        else:
            return 0

    def pay_salary(self):
        return super().pay_salary_wob()+self.bon

employee = PremiumEmployee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.give_bonus(1000.0)
employee.pay_salary()






#utwórz klasę Company, którą inicjalizuje się z nazwą
#>>>employee=Employee('Jan', 'Nowak', 100.0)
#>>>employee.register_time(5)
#>>>google=Company("google")
#>>>google.add_employee(employee)
#>>>google.size()
#1
#>>>google.pay_all_salary()
#500
##>>>google.pay_all_salary()
#0
#>>>employee2=Employee('Krzysztof', 'Nowak', 200.0)
#>>>employee2.register_time(5)
#>>>google.pay_all_salary()
#>>>google.add_employee(employee2)
#>>>google.pay_all_salary()
#1000

class Company:
    licznik = 0
    def __init__ (self,comp):
        self.comp=comp
        self.employees=set()

    def add_employee(self,employee):
        self.employees.add(employee)

    def pay_all_salary(self):
        sum_=0
        for e in self.employees:
            sum_+=e.pay_salary_wob()
        return sum_

    def size(self):
        return len(self.employees)

employee=Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
google=Company("google")
google.add_employee(employee)
google.size()
google.pay_all_salary()
google.pay_all_salary()
employee2=Employee('Krzysztof', 'Nowak', 200.0)
employee2.register_time(5)
google.pay_all_salary()
google.add_employee(employee2)
google.pay_all_salary()



def test_pay_salary_with_bon():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000.0)
    assert employee.pay_salary()==1500.0

def test_company():
    employee=Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    google=Company('google')
    google.add_employee(employee)
    assert google.size()==1
    assert google.pay_all_salary()==500
    assert google.pay_all_salary()==0
    employee2=Employee('Krzysztof', 'Nowak', 200.0)
    employee2.register_time(5)
    google.pay_all_salary()
    google.add_employee(employee2)
    assert google.pay_all_salary()==1000

