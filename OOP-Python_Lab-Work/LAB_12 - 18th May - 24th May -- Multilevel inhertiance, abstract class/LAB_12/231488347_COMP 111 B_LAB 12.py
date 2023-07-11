# TASK1
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def set_name(self, nam):
        self.name = nam

    def set_salary(self, sal):
        self.salary = sal


class Manager(Employee):

    def __init__(self, name, dep, sal):
        super().__init__(name, sal)
        self.department = dep

    def Display(self):
        print("Name: ", self.name)
        print("Department: ", self.department)
        print("Salary: $", self.salary)
        print("-" * 3)


class Executive(Manager):

    def __init__(self, name, dep, sal):
        super().__init__(name, dep, sal)


def main_task1():
    print(" Task 1", "\n", "-----")

    man1 = Manager("Sam", "People relations", 50000)
    man1.Display()

    exec1 = Executive("Jon", "Marketing", 80000)
    exec1.Display()


main_task1()


# TASK2
from abc import ABC, abstractmethod


class Polygon(ABC):

    def getnoofsides(self):
        pass

    def getrea(self):
        pass


class Triangle (Polygon):

    def getnoofsides(self):
        print("A triangle has 3 sides!")

    def getarea(self):
        self.base = int(input("Enter triangle base length: "))
        self.height = int(input("Enter triangle height: "))

        print("Area of Triangle= ", (1 / 2) * (self.base) * (self.height))
        print("--" * 3)


class Rectangle(Polygon):

    def getnoofsides(self):
        print("A rectangle has 4 sides!")

    def getarea(self):
        self.length = int(input("Enter rectangle length: "))
        self.width = int(input("Enter rectangle width: "))

        print("Area of rectangle= ", (self.length) * (self.width))
        print("--" * 3)


class Square(Polygon):

    def getnoofsides(self):
        print("A Square has 4 sides!")

    def getarea(self):
        self.length = int(input("Enter square side length: "))
        print("Area of square= ", (self.length) ** 2)
        print("--" * 3)


def main_task2():
    print(" Task 2", "\n", "-----")
    tri1 = Triangle()
    tri1.getnoofsides()
    tri1.getarea()

    rect1 = Rectangle()
    rect1.getnoofsides()
    rect1.getarea()

    sq1 = Square()
    sq1.getnoofsides()
    sq1.getarea()


main_task2()

# TASK3

class Account(ABC):

    def __init__(self, title, bal):
        self.AccountTitle = title
        self.CurrentBalance = bal

    def Interest_Rate(self):
        pass

    def getStatus(self):
        pass


class SBI(Account):

    def __init__(self, title, bal):
        super().__init__(title, bal)

    def Interest_Rate(self):
        interest = 0.05
        app_interest = (self.CurrentBalance * interest) + self.CurrentBalance
        print("Interest applied on current balance = ", app_interest)

    def get_status(self):
        print("Bank: SBI")
        print("Account title: ", self.AccountTitle)
        print("Balance: ", self.CurrentBalance)
        print("Interest rate: 5%")
        self.Interest_Rate()
        print("-"*5)


class ICICI(Account):

    def __init__(self, title, bal):
        super().__init__(title, bal)

    def Interest_Rate(self):
        interest = 0.06
        app_interest = (self.CurrentBalance * interest) + self.CurrentBalance
        print("Interest applied on current balance = ", app_interest)

    def get_status(self):
        print("Bank: ICICI")
        print("Account title: ", self.AccountTitle)
        print("Balance: ", self.CurrentBalance)
        print("Interest rate: 6%")
        self.Interest_Rate()
        print("-"*5)

class AXIS(Account):

    def __init__(self, title, bal):
        super().__init__(title, bal)

    def Interest_Rate(self):
        interest = 0.08
        app_interest = (self.CurrentBalance * interest) + self.CurrentBalance
        print("Interest applied on current balance = ", app_interest)

    def get_status(self):
        print("Bank: AXIS")
        print("Account title: ", self.AccountTitle)
        print("Balance: ", self.CurrentBalance)
        print("Interest rate: 8%")
        self.Interest_Rate()
        print("-"*5)

def main_task3():
    print(" Task 3", "\n", "-----")

    acc1 = SBI("Jonathan Joestar", 50000)
    acc2 = ICICI("Dio Brando", 25000)
    acc3 = AXIS("Caesar Zeppli", 80000)

    acc_list = [acc1, acc2, acc3]

    for i in range(0, len(acc_list)):
        acc_list[i].get_status()


main_task3()
