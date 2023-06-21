class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.limit = -500

    def withdraw(self, amount):
        if self.balance - amount > self.limit:
            self.balance -= amount


    def deposit(self, amount):
        self.balance += amount


my_bank = BankAccount(100)

print((my_bank.balance))

my_bank.withdraw(1000)

print((my_bank.balance))

my_bank.deposit(9000)

print((my_bank.balance))


