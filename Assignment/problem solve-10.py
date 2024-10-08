# Class to represent a Bank Account
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)
print(account.get_balance())

account.withdraw(300)
print(account.get_balance())

account.withdraw(1500)
