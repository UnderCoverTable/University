#QUESTION 1
print("--TASK 1")
class Employee:

    def __init__(self,id,name,salary):
        self.EmployeeID = id
        self.EmployeeName = name
        self.EmployeeSalary = salary

        self.EmployeeDetails = []
        self.EmployeeDetails.append(self.EmployeeID)
        self.EmployeeDetails.append(self.EmployeeName)
        self.EmployeeDetails.append(self.EmployeeSalary)
    def get_EmpName(self):
        print(self.EmployeeName)
    def get_EmpID(self):
        print(self.EmployeeID)
    def get_EmpSalary(self):
        print(self.EmployeeDetails[2])


    def GetEmpDetails(self):
        print("Employee ID: ",self.EmployeeDetails[0])
        print("Employee Name: ",self.EmployeeDetails[1])
        print("Employee Salary: ",self.EmployeeDetails[2])
        print("-"*7)

class Manager:

    def __init__(self,name,id):
        self.ManagerID = id
        self.ManagerName = name

    def get_ManID(self):
        print(self.ManagerID)
    def get_ManName(self):
        print(self.ManagerName)
    def get_ManagerDetails(self):
        print("Manager Name: ",self.ManagerID)
        print("Manager ID: ",self.ManagerName)

    def IncrementSalary(self,e):
        e.EmployeeSalary = e.EmployeeSalary*(5/100)+e.EmployeeSalary
        e.EmployeeDetails[2] = e.EmployeeSalary


def emp_main():
    man1 = Manager("6666", "Sarah")
    emp1 = Employee("0321","sam",5000)
    emp1.GetEmpDetails()
    man1.IncrementSalary(emp1)
    emp1.GetEmpDetails()

    emp2 = Employee("2569","Jack",100)
    man1.IncrementSalary(emp2)
    emp2.GetEmpDetails()

    man1.get_ManagerDetails()

emp_main()


#QUESTION 2
print("--TASK 2")
class Patient:

    def __init__(self,id=0,name="-",dis="--",treat="----"):
        self.PatientID = id
        self.PatientName = name
        self.PatientDisease = dis
        self.PatientTreatment = treat

    def Chart(self):
        print("Patient ID: ",self.PatientID)
        print("Patient Name: ",self.PatientName)
        print("Patient Disease: ",self.PatientDisease)
        print("Patient Treatment: ",self.PatientTreatment)
        print("-"*7)

class Doctor:

    def __init__(self,id,name):
        self.DoctorID = id
        self.DoctorName = name

    def DoctorDetails(self):
        print("Doctor ID: ",self.DoctorID)
        print("Doctor Name: ",self.DoctorName)
        print("-"*7)

    def Treat(self,patient,treatment):
        patient.PatientTreatment = treatment

def hospital_main():

    doc = Doctor("5562","Hammad")
    pat1 = Patient("0321","Sam","Flu")
    doc.Treat(pat1,"Panadol and Rigix")

    pat2 = Patient("6532","Jack","Stomach ache","Take Rizek")

    doc.DoctorDetails()
    pat1.Chart()
    pat2.Chart()

hospital_main()


#QUESTION 3
print("--TASK 3")
class Student:

    def __init__(self,id,name,salary=0):
        self.StudentID = id
        self.StudentName = name
        self.StudentSalary = salary
        self.IssuedBooks = []

    def Student_info(self):
        print("Student ID: ",self.StudentID)
        print("Student Name: ",self.StudentName)
        print("Student Salary: ",self.StudentSalary)
        print("Issued Books: ")
        for i in range (0,len(self.IssuedBooks)):
            self.IssuedBooks[i].BookDetails()


class Library:

    def __init__(self,id,title,author):
        self.BookID = id
        self.BookTitle = title
        self.BookAuthor = author

    def Issuance(self,stu,book):
        stu.IssuedBooks.append(book)

    def BookDetails(self):
        print(self.BookID,"/",self.BookTitle,"/",self.BookAuthor)


def lib_main():
    book1 = Library("5566","Charlie stew","Jhon hopkins")
    book2 = Library("8784","Goldeneye","James bond")

    stu1 = Student("0321","Sam",5000)
    book1.Issuance(stu1,book1)
    book2.Issuance(stu1,book2)
    stu1.Student_info()

lib_main()





