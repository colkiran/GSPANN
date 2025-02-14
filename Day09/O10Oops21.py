
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Managers job.....")


class Developer(Employee):

    def doJob(self):
        print("Developers job.....")


def BankJob(emp):
    print("Bankjob started.......")
    emp.doJob()
    print("Bankjob ended.........")
    print("-" * 60)

mike = Manager()
david = Developer()

BankJob(mike)
print("-" * 60)

BankJob(david)
