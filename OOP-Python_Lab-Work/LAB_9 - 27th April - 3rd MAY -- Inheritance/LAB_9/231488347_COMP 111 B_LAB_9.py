#TASK1

class Cards:

    def __init__(self,num,name,address,exp):
        self.CardNumber = num
        self.CardOwner = name
        self.CardAddress = address
        self.CardExpiry = exp
    def CardInfo(self):
        print("Card Number: ",self.CardNumber)
        print("Card Owner: ",self.CardOwner)
        print("Owner Address: ",self.CardAddress)
        print("Expiry Date: ",self.CardExpiry)

class CallingCard (Cards):

    def __init__(self,num,name,address,exp,amt,com,pin):
        super().__init__(num,name,address,exp)
        self.CardAmount = amt
        self.CardCompany = com
        self.CardPin = pin
    def DisplayInfo(self):
        print("Card Type: Calling card")
        super().CardInfo()
        print("Card Amount: $",self.CardAmount)
        print("Company Name: ",self.CardCompany)
        print("PIN: ",self.CardPin)
        print("_"*6)

class IDCard (Cards):

    def __init__(self,num,name,address,exp,ssn,age):
        super().__init__(num,name,address,exp)
        self.SocialSec = ssn
        self.Age = age
    def DisplayInfo(self):
        print("Card Type: ID card")
        super().CardInfo()
        print("Social Security Number: ",self.SocialSec)
        print("Age: ",self.Age)
        print("_" * 6)

class DrivingLicense (Cards):

    def __init__(self,num,name,address,exp,vehicle,city):
        super().__init__(num,name,address,exp)
        self.VehicleType = vehicle
        self.City = city

    def DisplayInfo(self):
        print("Card Type: Driving License")
        super().CardInfo()
        print("Driving License Type: ",self.VehicleType)
        print("Issued City: ",self.City)
        print("_" * 6)

def task1_main():
    print(" TASK 1","\n","-"*7)

    a = CallingCard("03525","Sam","25/K","25/8/2025","500","JAZZ",525)
    b = IDCard(55326, "Jon", "965/P", "25/05/2025", 5622321001, 56)
    c = DrivingLicense(69567, "Rio", "569/U","31/08/2236","Bike", "Lahore")

    crds = [a,b,c]
    for i in range(len(crds)):
        crds[i].DisplayInfo()

    print()
task1_main()


#TASK 2

class Date:

    def __init__(self,day,month,year):
        self.Day = day
        self.Month = month
        self.Year = year

    def DisplayDate(self):
        print(self.Day,"/",self.Month,"/",self.Year)

class PersonType:

    def __init__(self,fname,lname):
        self.FirstName = fname
        self.LastName = lname

    def SetName(self,fname,lname):
        self.FirstName = fname
        self.LastName = lname

    def DisplayName(self):
        print(self.FirstName,self.LastName)

class Doctor (PersonType):

    def __init__(self,fname,lname,spec):
        super().__init__(fname,lname)
        self.DoctorSpecialisation = spec

    def SetDocName(self,fname,lname):
        self.FirstName = fname
        self.LastName = lname

    def SetSpeciality(self,spec):
        self.DoctorSpecialisation = spec

    def DoctorInfo(self):
        print("Dcotor: ",end=""),super().DisplayName()
        print("Doctor Specialisation: ",self.DoctorSpecialisation)
        print("-"*6)

class Patient (PersonType):

    def __init__(self,fname,lname,idd,age,d1,m1,y1,d2,m2,y2,d3,m3,y3,docName):
        super().__init__(fname,lname)
        self.PateintID = idd
        self.PateintAge = age
        self.PateintDOB = Date(d1,m1,y1)
        self.PateintAdmit = Date(d2,m2,y2)
        self.PateintDischarge = Date(d3,m3,y3)
        self.DocIncharge = docName

    def SetPatientID(self,iden):
        self.PateintID = iden
    def SetPatientAge(self,age):
        self.PateintAge = age
    def SetPatientDoctor(self,d):
        self.DocIncharge = d

    def SetPatientDOB(self,d,m,y):
        self.PateintDOB = Date(d,m,y)
    def SetPatientAdmittance(self,d,m,y):
        self.PateintAdmit = Date(d,m,y)
    def SetPatientDischarge(self,d,m,y):
        self.PateintDischarge = Date(d,m,y)

    def GetPatientID(self):
        print(self.PateintID)
    def GetPatientAge(self):
        print(self.PateintAge)
    def GetPatientDoctor(self):
        print(self.DocIncharge)

    def GetPatientDOB(self):
        print(self.PateintDOB)
    def GetPatientAdmittance(self):
        print(self.PateintAdmit)
    def GetPatientDischarge(self):
        print(self.PateintDischarge)


    def PatientInfo(self):

        print("Pateint Name: ",end=""),super().DisplayName()
        print("Patient ID: ",self.PateintID)
        print("Patient Age: ",self.PateintAge)
        print("Patient Date of birth: ",end=""),self.PateintDOB.DisplayDate()
        print("Patient Admittance: ",end=""),self.PateintAdmit.DisplayDate()
        print("Patient Discharge: ",end=""),self.PateintDischarge.DisplayDate()
        print("-")
        print("Patient is being treated by: ")
        self.DocIncharge.DoctorInfo()


def task2_main():
    print(" TASK 2", "\n", "-" * 7)

    d1 = Doctor("Zia","Haq","Cardiology")
    d2 = Doctor("Samuel","Lam","Neurology")
    p1 = Patient("sam", "jon", 5264, 24, 12, 4, 1995, 24, 5, 2012, 30, 6, 2012, d2)

    d1.DoctorInfo()
    p1.PatientInfo()

task2_main()