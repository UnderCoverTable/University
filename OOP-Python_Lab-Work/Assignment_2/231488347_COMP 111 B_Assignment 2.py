# TASK 1

class Account:

    def __init__(self, name = "-", id = 0, typ = "--", bal = 0):
        self.AccountTitle = name
        self.AccountID = id
        self.AccountType = typ
        self.AccountBalance = bal

    def Balance(self):
        print("Acc Balance: ","$",self.AccountBalance)

    def Tile(self):
        print("Acc ID: ", self.AccountID)
        print("Acc Title: ", self.AccountTitle)


    def Details(self):
        print("Acc ID: ",self.AccountID)
        print("Acc Title: ",self.AccountTitle)
        print("Acc Type: ",self.AccountType)
        print("Acc Balance: ","$",self.AccountBalance)
        print("--"*6)

    def Deposit(self,money):
        self.AccountBalance = self.AccountBalance + money
        print("you have deposited, ","$",money)
        print("--","Account,",self.AccountTitle,self.AccountID,",new balance is :",self.AccountBalance)


    def Withdraw(self,money):
        if money>self.AccountBalance:
            print("Error. You are trying to withdraw more then your account balance")
        else:
            self.AccountBalance = self.AccountBalance - money
            print("you have withdrawn, ", "$", money)
            print("--","Account,", self.AccountTitle, self.AccountID, ",new balance is :", self.AccountBalance)

def bank_main():
    print("TASK 1")
    accs = []
    acc1 = Account("abc",3621,"Current",10000)
    acc2 = Account("ghi", 5648, "Saving", 30000)
    acc3 = Account("mlk",3256,"Saving",55000)
    accounts = [acc1,acc2,acc3]

    for i in range(1,len(accounts)+1):
        accs.append("acc"+str(i))
    print("Accounts with the bank are:")
    for ele in accs:
        print(ele)
    print("**"*2)

    acc1.Deposit(5000)
    acc1.Withdraw(200)
    acc3.Withdraw(10000)

bank_main()
print()
#TASK 2

class Joined:
        def __init__(self,day,month,year):
                self.Day = day
                self.Month = month
                self.Year = year
        def DOJ(self):
                print("Employee Joined on:",self.Day,"/",self.Month,"/",self.Year)



class Management:
        def __init__(self,code,name,doj,age,exp):
                self.EmployeeCode = code
                self.EmployeeName = name
                self.EmployeeDOJ = doj
                self.EmployeeAge = age
                self.EmployeeExperience = exp
        def EmployeeDetails(self):
                print("Employee Code: ",self.EmployeeCode)
                print("Employee Name: ",self.EmployeeName)
                self.EmployeeDOJ.DOJ()
                print("Employee Age:",self.EmployeeAge)
                print("Years of experience: ",self.EmployeeExperience)

        def Employee_Name(self):
                print("Name: ",self.EmployeeName)
                print("Code: ",self.EmployeeCode)

        def Tenure_check(self,d):

                current_date = input("Please enter todays date: ")
                date_list = current_date.split("/")
                print("Today is: ", current_date)
                d.DOJ()
                if (int(date_list[2]) - d.Year) > 2 :
                        print("2 years have passed")
                if (int(date_list[2]) - d.Year) < 2 :
                        print("2 years have not passed")
                if (int(date_list[2]) - d.Year) == 2 :
                        if int(date_list[1]) > d.Month:
                                print("2 years have passed")
                        if int(date_list[1]) < d.Month:
                                print("2 years have not passed")
                        if int(date_list[1]) == d.Month:
                                if int(date_list[0]) > d.Day:
                                        print("2 years have passed")
                                if int(date_list[0]) < d.Day:
                                        print("2 years have not passed")

def manage_main():
        print("TASK 2")
        d1 = Joined(25, 4, 2018)
        e1 = Management(5566, "Sam",d1 , 54, 12)
        d2 = Joined(15,6,2019)
        e2 = Management(8975,"Jon",d2,25,5)
        d3 = Joined(12,10,2000)
        e3 = Management(2314,"Julia",d3,34,8)

        dojs = [d1,d2,d3]
        emps = [e1,e2,e3]

        for i in range (0,len(dojs)):
                emps[i].Employee_Name()
                emps[i].Tenure_check(dojs[i])
                print("-"*6)
manage_main()
print()
#TASK 3

class NextBridgeEmployee:

        def __init__(self,name="-",address="--",number=0,awards={},exp=0,salary=0):

                self.EmployeeName = name
                self.EmployeeAddress = address
                self.EmployeeNumber = number
                self.EmployeeAwards = awards
                self.EmployeeExperience = exp
                self.EmployeeSalary = salary
                if self.EmployeeExperience == 0:
                        self.SalaryIncrement = 0
                if self.EmployeeExperience == 1 or self.EmployeeExperience == 2:
                        self.SalaryIncrement = 10
                if self.EmployeeExperience > 2 and self.EmployeeExperience <= 6:
                        self.SalaryIncrement = 20
                if self.EmployeeExperience > 6:
                        self.SalaryIncrement = 40


        def Get_Name(self):
                return self.EmployeeName
        def Get_Address(self):
                return self.EmployeeAddress
        def Get_Phone(self):
                return self.EmployeeNumber
        def Get_Awards(self):
                return self.EmployeeAwards
        def Get_Experince(self):
                return self.EmployeeExperience
        def Get_Salary(self):
                return self.EmployeeSalary
        def Get_Increment(self):
                return self.SalaryIncrement

        def Set_Name(self,name):
                self.EmployeeName = name
        def Set_Address(self,address):
                self.EmployeeAddress = address
        def Set_Phone(self,num):
                self.EmployeeNumber = num
        def Set_Awards(self,awd):
                self.EmployeeAwards = awd
        def Set_Experince(self,exp):
                self.EmployeeExperience = exp
        def Set_Salary(self,sal):
                self.EmployeeSalary = sal
        def Set_Increment(self,inc):
                self.SalaryIncrement = inc

        def EmployeeDetails(self):
                print("Name: ",self.EmployeeName)
                print("Address: ",self.EmployeeAddress)
                print("Phone number: ",self.EmployeeNumber)
                print("Awards: ",self.EmployeeAwards)
                print("Experience: ",self.EmployeeExperience," Years")
                print("Salary: ","$",self.EmployeeSalary)
                print("Salary Increment: ",self.SalaryIncrement,"%")

                print("_"*6)

        def CalculateIncrement(self):
                print("Employee Name:", self.EmployeeName)
                print("Increment % based on Experience: ",self.SalaryIncrement,"%")
                inc = self.EmployeeSalary * (self.SalaryIncrement/ 100)
                print("Incremented Salary: ","$",self.EmployeeSalary+inc)

                print("-"*6)


def NextBridgeMain():
        print("TASK 3")
        e1 = NextBridgeEmployee("Sam","25/N",130265,{2019:"Employee of the day"},1,25000)
        e2 = NextBridgeEmployee("Jim","96/P",255692,{2005:"Best Person"},5,50000)
        e3 = NextBridgeEmployee("Jhon","355/K",336598,{2016:"Good man",2002:"Nice person"},12,75000)

        emps = [e1,e2,e3]
        for i in range(0,len(emps)):
                emps[i].EmployeeDetails()
                emps[i].CalculateIncrement()

NextBridgeMain()
print()

# TASK 4

import math


class Complex:

    def __init__(self, real=0, img=0):
        self.Imaginary = img
        self.Real = real
        self.NumbersList = []

    def User_ComplexNumbers(self):

        write_file = open("complex_numbers.txt", "w")

        n_complex_nums = input("How many complex numbers do you want: ")

        for i in range(0, int(n_complex_nums)):
            if i == 0:
                print(n_complex_nums, file=write_file)
            c_n = input("Enter the complex number: ")
            print(c_n, file=write_file)
            self.NumbersList.append(c_n.split("+"))
        print("All complex numbers have been added to the file, complex_numbers.txt ")
        print("-" * 6)

    def Absolute_greater_then_4(self):
        chk = 0
        ch = 0
        for i in range(0, len(self.NumbersList)):
            a = int(self.NumbersList[i][0])
            b = int(self.NumbersList[i][1][0])
            abs = math.sqrt(a ** 2 + b ** 2)
            if abs > 4:
                if ch == 0:
                    print("Complex numbers, with Absolute > 4: ")
                ch = 1
                chk = 1
                print(self.NumbersList[i][0], "+", self.NumbersList[i][1], "-> Absolute = ", abs)
        if chk == 0:
            print("No complex numbers with Absolute value greater then 4")

    def Addition(self, real, img):
        sum_real = self.Real + real
        sum_img = self.Imaginary + img
        print("(", self.Real, "+", self.Imaginary, "i", ")", " + ", "(", real, "+", img, "i", ")")
        print("= ", sum_real, "+", sum_img, "i")
        print("-" * 6)

    def Subtraction(self, real, img):
        sum_real = self.Real - real
        sum_img = self.Imaginary - img
        print("(", self.Real, "+", self.Imaginary, "i", ")", " - ", "(", real, "+", img, "i", ")")
        print("= ", abs(sum_real), "+", sum_img, "i")
        print("-" * 6)

    def Multiplication(self, real, img):
        a1 = self.Real * real
        a2 = self.Real * img

        b1 = self.Imaginary * real
        b2 = self.Imaginary * img

        if img < 0:
            final_real = a1 + abs(b2)
            final_img = a2 + b1
            print("(", self.Real, "+", self.Imaginary, "i", ")", " * ", "(", real, "+", img, "i", ")")
            print("= ", final_real, "+", final_img, "i")

        else:
            final_real = a1 - b2
            final_img = a2 + b1
            print("(", self.Real, "+", self.Imaginary, "i", ")", " * ", "(", real, "+", img, "i", ")")
            print("= ", final_real, "+", final_img, "i")
        print("-" * 6)

    def div_help(self, real, img):
        a1 = self.Real * real
        a2 = self.Real * img

        b1 = self.Imaginary * real
        b2 = self.Imaginary * img

        if img < 0:
            final_real = a1 + abs(b2)
            final_img = a2 + b1
            aa = str(final_real)
            bb = str(final_img)
            return aa + "+" + bb + "i"
        else:
            final_real = a1 - b2
            final_img = a2 + b1
            aa = str(final_real)
            bb = str(final_img)
            return aa + "+" + bb + "i"

    def Division(self, real, img):
        d = Complex(real, img)
        print("(", self.Real, "+", self.Imaginary, "i", ")", " / ", "(", real, "+", img, "i", ")")

        if img < 0:
            nume = self.div_help(real, abs(img))
            denom = d.div_help(real, abs(img))
            print("=", nume, "/", denom)
        else:
            nume = self.div_help(real, -img)
            denom = d.div_help(real, -img)
            print("=", nume, "/", denom)
        print("-" * 6)


def complex_main():
    print("TASK 4")
    test = Complex()
    test.User_ComplexNumbers()
    test.Absolute_greater_then_4()

    n = Complex(2, 3)
    n.Addition(5, -6)
    n.Subtraction(-6, 5)
    n.Multiplication(4, -6)
    n.Division(7, -1)

complex_main()
