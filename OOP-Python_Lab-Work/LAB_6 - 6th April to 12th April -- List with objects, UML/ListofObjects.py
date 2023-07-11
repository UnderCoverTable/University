class Student:

    def __init__(self,rollno, name,cgpa):
        self._rollNo = rollno
        self._name = name
        self._cgpa = cgpa
        self.course = []
    ##add setters and getters for all instance variable
    def addcourse (self, coursecode):
        self.course.append(coursecode)
    def display(self):
        print(self._rollNo)
        print(self._name)
        print(self._cgpa)
        for i in self.course:
            print(i)

def main():

    stdlist = []
    ch = 'y'

    while ch != 'n':
        rollno = input("enter rollno")
        name = input("enter name")
        cgpa = input("enter cgpa")
        stdobj = Student(rollno,name,cgpa)
        stdobj.addcourse("Comp111")
        stdobj.addcourse("Math111")
        stdlist.append(stdobj)
        
        ch = input("Do you want to continue")

    for i in stdlist:
        i.display()
        
    for i in range(len(stdlist)):
        stdlist[i].display()


main()
