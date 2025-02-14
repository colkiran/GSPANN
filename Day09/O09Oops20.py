
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account....")

    @abstractmethod
    def get_balance(self):
        pass

    def deposit(self):
        pass

    def withdraw(self):
        pass

class Savings(Account):

    def get_balance(self):
        print("Balance in the account is #####")

    def deposit(self):
        print("Deposited ##### successfully into account ending 0000")

sav = Savings()
sav.deposit()
sav.get_balance()
