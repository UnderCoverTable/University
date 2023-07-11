##TASK 2

class Employee:

    def __init__(self, iden, name, salary):
        self.EmpID = iden
        self.EmpName = name
        self.EmpSalary = salary

    def salary_status(self):
        return self.EmpSalary

    def details(self):
        if self.salary_status() == 10000:
            print("-Building Manager")
        if self.salary_status() == 12000:
            print("-Procurement Manager")
        if self.salary_status() == 15000:
            print("-Logistics Manager")

        print("ID: ", self.EmpID)
        print("Name: ", self.EmpName)
        print("Salary: $", self.salary_status())
        print("-" * 3)


class BuildingManager(Employee):

    def __init__(self, iden, name):
        super().__init__(iden, name, 10000)


class ProcurementManager(Employee):
    def __init__(self, iden, name):
        super().__init__(iden, name, 12000)


class LogisticsManager(Employee):
    def __init__(self, iden, name):
        super().__init__(iden, name, 15000)


def task2_main():
    print(" Task 2", "\n", "-" * 6)

    bm = BuildingManager(2553, "Ali")
    bm2 = BuildingManager(6985, "Roberto")

    pm = ProcurementManager(3569, "Poppy")
    pm2 = ProcurementManager(3256, "Kim")

    lm = LogisticsManager(4289, "Jon")

    empss = [bm, pm, lm, pm2, bm2]
    for i in range(len(empss)):
        empss[i].details()


task2_main()
