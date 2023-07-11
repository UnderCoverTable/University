class Person:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
    def Displayinfo(self):
        print(self.name)
        print(self.dob)
        
    
    
class student(Person):
    def __init__(self,name,dob,major):
        super().__init__(name,dob)
        self.major = major
    #1 accessors and 1 mutators
    def Display(self):
        self.Displayinfo()
        print(self.major)


class instructor(Person):
    def __init__(self,name,dob,salary):
        super().__init__(name,dob)
        self.salary = salary
      #1 accessors and 1 mutators
    def Display(self):
        super().Displayinfo()
        print(self.salary)


stdObj = student("Ali", "03-03-1999","CS")
instrObj = instructor("Samia", "04-04-1983",123456)
stdObj.Display()
instrObj.Display()

