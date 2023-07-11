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