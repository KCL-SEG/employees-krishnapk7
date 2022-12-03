"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly, contract, commission, bonus_commission):
        self.name = name
        self.monthly = monthly
        self.contract = contract
        self.commission = commission
        self.bonus_commission = bonus_commission
        self.pay = 0

    def calc_pay(self):
        if self.monthly != None:
            self.pay = self.pay + self.monthly
        else:
            self.pay = self.pay + (self.contract[0]*self.contract[1])

        if self.commission != None:
            self.pay = self.pay + (self.commission[0]*self.commission[1])
        elif self.bonus_commission != None:
            self.pay = self.pay + self.bonus_commission
        else:
            pass

    def get_pay(self):
        return self.pay

    def __str__(self):
        return f"{self.name} works on a "


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, None, None, None)
billie.calc_pay()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', None, [25,100], None, None)
charlie.calc_pay()

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, None, [4,200], None)
renee.calc_pay()

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', None, [25,150], [3,220], None)
jan.calc_pay()

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, None, None, 1500)
robbie.calc_pay()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', None, [30,120], None, 600)
ariel.calc_pay()
