#QUESTION 1

class Address:

    def __init__(self,HouseNum=0,street="-",city="-",country="-"):
        print("*")
        self.HouseNumber = HouseNum
        self.Street = street
        self.City = city
        self.Country = country
    def DisplayAddress(self):
        print("Address: ",self.HouseNumber,"/",self.Street,"/",self.City,"/",self.Country)
        print("-"*5)

class Customer:

    def __init__(self,name,id,hn,st,ci,co):
        self.Name = name
        self.ID = id
        self.CusAddress = Address(hn,st,ci,co)

    def DisplayInfo(self):
        print("Name: ",self.Name)
        print("ID: ",self.ID)
        self.CusAddress.DisplayAddress()
def cus_main():
    cus1 = Customer("Jhon","0312",244,"Street 56","Lahore","Pakistan")
    cus2 = Customer("Ali", "0256",566,"Street 21","Karachi","Pakistan")

    cus1.DisplayInfo()
    cus2.DisplayInfo()
cus_main()


#QUESTION 2

class Movie:

    def __init__(self,name="",actorHero="-",actorVillain="-",genre="-"):
        self.MovieName = name
        self.Hero = actorHero
        self.Villain = actorVillain
        self.Genre = genre

    def setName(self,name):
        self.MovieName = name
    def getName(self):
        return self.MovieName
    def setGenre(self, gen):
        self.Genre = gen
    def getGenre(self):
        return self.Genre

    def getHero(self):
        return self.Hero.DisplayActor()
    def getVillain(self):
        return self.Villain.DisplayActor()


    def DisplayMovie(self):
        print("-Name:",self.MovieName)
        print("-Hero details: "),self.Hero.DisplayActor()
        print("-Villain details: "),self.Villain.DisplayActor()
        print("-Genre: ",self.Genre)


class Actor:

    def __init__(self,name="-",date="_",gen="="):
        print("**")
        self.Actorname = name
        self.Actordob = date
        self.Gender = gen

    def set_name(self,name=""):
        self.Actorname = name
    def set_dob(self,date=""):
        self.Actordob = date
    def set_gender(self,gen=""):
        self.Gender = gen

    def get_name(self):
        return self.Actorname
    def get_dob(self):
        return self.Actordob
    def get_gender(self):
        return self.Gender

    def DisplayActor(self):
        print(self.Actorname,self.Actordob,self.Gender)

def mov_main():

    hero = Actor("Luke","15/06/2036","M")
    villain = Actor("Darth vader","23/03/2019","M")
    mov1 = Movie("Star Wars",hero,villain,"Action/Sci-fi")

    print("-Name: ",mov1.getName())
    print("-Hero details: "),mov1.getHero()
    print("-Villain details: "),mov1.getVillain()
    print("-Genre: ",mov1.getGenre())

    hero2 = Actor("Peter","23/12/1985","M")
    villain2 = Actor("Mary Jane","15/1981","F")
    mov2 = Movie("SpiderMan",hero2,villain2,"Superhero movie")

    mov2.DisplayMovie()

mov_main()


#QUESTION 3

class Company:

    def __init__(self,name,type,address):
        print("***")
        self.CompanyName = name
        self.CompanyType = type
        self.CompanyAddress = address
        self.Employees = []


    def AddEmployee(self,emp):
        self.Employees.append(emp)


    def DisplayComp(self):
        print("Company Name: ",self.CompanyName)
        print("Service: ",self.CompanyType)
        print("Address: ",self.CompanyAddress)
        print()
        print("Employee Details: ")
        print("Number of Employess: ",len(self.Employees))
        for i in range(0,len(self.Employees)):
            print(i+1,end="- "),self.Employees[i].DisplayEmp()
        print("-"*10)


class Employee:
    def __init__(self,name,address,phone):
        self.EmployeeName = name
        self.EmployeeAddress = address
        self.EmployeeNum = phone

    def DisplayEmp(self):
        print("Name: ",self.EmployeeName,", ","Number: ",self.EmployeeNum)
        print("Address: ",self.EmployeeAddress)


def comp_main():

    com1 = Company("Storm Fibre", "ISP", "256/K Block Lahore")
    com2 = Company("Macrosoft","Software Provider","369/N Block Karachi")

    e1 = Employee("Sam","24/L Lahore","03211562365")
    e2 = Employee("John","56/O Lahore","03665987452")
    e3 = Employee("Cena","67/A Lahore","03264589621")
    e4 = Employee("Chris","36/P Karachi","03698574521")
    e5 = Employee("Luther","23/R Karachi","03124569856")


    com1.AddEmployee(e1)
    com1.AddEmployee(e2)
    com1.AddEmployee(e3)

    com2.AddEmployee(e4)
    com2.AddEmployee(e5)

    com1.DisplayComp()
    com2.DisplayComp()

comp_main()





