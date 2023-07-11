class Date:
    def __init__(self,y,m,d):
        self.year = y
        self.month = m
        self.day = d
    def displaydate(self):
        print(self.year)
        print(self.month)
        print(self.day)


class student:
    def __init__(self,id,cgpa,year,mon,day,ayear,amon,aday):
        self.id = id
        self.cgpa = cgpa
        self.dob = Date(year,mon,day)
        self.admissiondate = Date(ayear,amon,aday)
    def display(self):
        print(self.id,self.cgpa)
        self.dob.displaydate()
        self.admissiondate.displaydate()
        
class faculty:
    def __init__(self,id,salary,year,mon,day):
        self.id = id
        self.salary = salary
        self.dob = Date(year,mon,day)
class admin:
    def __init__(self,id,rank,year,mon,day):
        self.id = id
        self.salary = rank
        self.dob = Date(year,mon,day)
