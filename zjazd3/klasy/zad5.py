class CashMachine:
    def __init__(self):
        self.bank = []
        self.broken=False

    def __str__(self):
        return "CashMachine"

    @property
    def is_available(self):
        return bool(len(self.bank))

    def put_money(self, cash):
        self.cash = cash
        self.bank.extend(self.cash)
        sorted(self.bank)

    def withdraw_money(self, amount):
        self.amount = amount
        bank_amount = 0
        for c in self.bank:
            bank_amount += c
        if amount >= bank_amount:
            amount = bank_amount
        cash_out=[]
        for a in self.bank:
            if a <= amount:
                amount-=a
                cash_out.append(a)
                self.bank.remove(a)
        print(f'''Chciał {self.amount}, Wypłacono {cash_out}''')
        return cash_out

cash_machine = CashMachine()
print(cash_machine.bank)
cash_machine.put_money([200, 100, 100, 50])
print(f'''W banku jest{cash_machine.bank}''')
cash_machine.withdraw_money(150)
print(f'''W banku jest{cash_machine.bank}''')
cash_machine.withdraw_money(150)
print(f'''W banku jest {cash_machine.bank}''')


def test_is_available():
    cash_machine = CashMachine()
    assert cash_machine.is_available==False


def test_is_available1():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available==True


def test_is_available2():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150)== [100, 50]

def test_is_available2():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available==True
    cash_machine.withdraw_money(150)
    assert cash_machine.is_available==True
