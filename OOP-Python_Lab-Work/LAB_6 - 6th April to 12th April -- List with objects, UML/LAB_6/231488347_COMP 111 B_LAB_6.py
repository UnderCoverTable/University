# QUESTION 1

class Car:
    def __init__(self,mileage=0):
        print("*")
        self.mileage = mileage
        self.gas_level = 0

    def add_gas(self, gas = 0):
        self.gas_level = self.gas_level + gas

    def get_gas_level(self):
        return self.gas_level

    def drive(self,miles=0):
        a = (miles / self.mileage)
        self.gas_level = self.gas_level - a

def car_main():
    mycar = Car(10)
    mycar.add_gas(50)
    mycar.add_gas(50)
    mycar.drive(350)

    print("Gas: ",mycar.get_gas_level())

car_main()

# QUESTION 2

class Employee:
    type_Emp = 0
    def __init__(self,ID=0,Name="-",Salary=0):
        print("**")
        self.EmployeeID = ID
        self.EmployeeName = Name
        self.EmployeeSalary = Salary
        self.type_Emp = "Lower Grade"

    def set_EmpID(self,ID=0):
        self.EmployeeID = ID
    def set_EmpName(self,Name="-"):
        self.EmployeeName = Name
    def set_EmpSalary(self,Salary):
        self.EmployeeSalary = Salary

    def get_EmpID(self):
        return self.EmployeeID
    def get_EmpName(self):
        return EmployeeName
    def get_EmpSalary(self):
        return self.EmployeeSalary
    def get_EmpDetails(self):
        print("Grade: ",self.type_Emp,"\n","ID: ",self.EmployeeID,"\n","Name: ",self.EmployeeName,"\n","Salary: ","$",self.EmployeeSalary)


class Manager():
    type_Emp = 0
    def __init__(self,ID=0,Name="-"):
        print("**")
        self.ManagerID = ID
        self.ManagerName = Name
        self.type_Emp = "Upper Grade"

    def set_ManaID(self,ID=0):
        self.ManagerID = ID
    def set_ManaName(self,Name="-"):
        self.ManagerName = Name

    def get_ManaID(self):
        return self.ManagerID
    def get_ManaName(self):
        return self.ManagerName
    def get_ManaDetails(self):
        print("Grade: ",self.type_Emp,"\n","ID: ",self.ManagerID,"\n","Name: ",self.ManagerName,)


def com_main():
    emp_list=[]
    mana_list=[]
    for i in range(0,3):
        e_id = input("Enter an employee ID: ")
        e_name = input("Enter the employee name: ")
        e_salary = input("Enter employee salary: ")
        emp = Employee(e_id,e_name,e_salary)
        emp_list.append(emp)
    for employees in emp_list:
        employees.get_EmpDetails()
        print("-"*10)

    for i in range(0,2):
        m_id = input("Enter a manager ID: ")
        m_name = input("Enter the manager name: ")
        man = Manager(m_id,m_name)
        mana_list.append(man)
    for managers in mana_list:
        managers.get_ManaDetails()
        print("-"*10)
com_main()

# QUESTION 3

class Student:

    def __init__(self, ID=0,name="-",sem=0,mrks=0):
        print("***")
        self.StudentID = ID
        self.StudentName = name
        self.Semester = sem
        self.TotalMarks = mrks

    def set_studentID(self,ID=0):
        self.StudentID = ID
    def set_studentName(self,name="-"):
        self.StudentName = name
    def set_semester(self,sem=0):
        self.Semester = sem
    def set_marks(self,mrks):
        self.TotalMarks = mrks

    def get_studentID(self):
        return self.StudentID
    def get_studentName(self):
        return self.StudentName
    def get_semester(self):
        return self.Semester
    def get_marks(self):
        return self.TotalMarks
    def StudentInfo(self):
        print("ID: ",self.StudentID,"\n","Name: ",self.StudentName,"\n","Semester: ",self.Semester,"\n","Total Marks: ",self.TotalMarks)


infile = open("my_file.txt","r")
line_list=[]
final_list=[]
line = infile.readline()
while line != "":
    line_list.append(line)
    line=infile.readline()
for i in range(0,len(line_list)):
    a = line_list[i].split()
    final_list.append(a)
infile.close()


def student_main():
    stu_list=[]
    for u in range(0,4):
        stu = Student(final_list[u][0],final_list[u][1],final_list[u][2],final_list[u][3])
        stu_list.append(stu)

    for students in stu_list:
        students.StudentInfo()
student_main()


# QUESTION 4

class Actor:

    def __init__(self,name="-",date="_",gen="=",movies=""):
        print("****")
        self.Actorname = name
        self.Actordob = date
        self.Gender = gen
        self.Movies = movies.split(",")

    def set_name(self,name=""):
        self.Actorname = name
    def set_dob(self,date=""):
        self.Actordob = date
    def set_gender(self,gen=""):
        self.Gender = gen
    def add_movie(self,movie=""):
        self.Movies.append(movie)

    def get_name(self):
        return self.Actorname
    def get_dob(self):
        return self.Actordob
    def get_gender(self):
        return self.Gender
    def get_movies(self):
        return self.Movies

    def DisplayActor(self):
        print(self.Actorname,self.Actordob,self.Gender)
        print("Movies: ")
        for i in range(0,len(self.Movies)):
            print(self.Movies[i])
        print("_"*5)

    def CompareActor(self,a2=0):
        com_movies=[]
        a = self.Movies
        b = a2.get_movies()

        for i in range(0,len(a)):
            if a[i] in b :
                com_movies.append(a[i])
        print("Common movies between both actors are: ",com_movies)

def act_main():
    act1 = Actor()
    act1.set_name("Tom")
    act1.set_dob("05/03/1965")
    act1.set_gender("M")
    act1.add_movie("Mov1")
    act1.add_movie("Mov4")

    act2 = Actor("Sam","02/23/2663","F","Mov4,Mov5,Mov6")

    act1.DisplayActor()
    act2.DisplayActor()
    act1.CompareActor(act2)
act_main()

