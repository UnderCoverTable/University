from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

def main():
         Slist = []
         
         for i in range(3):
                  s = input("enter shape type")
                  if s == "c":
                           Slist.append(Circle(int(input("enter radius"))))
                  else:
                           Slist.append(Square(int(input("enter length"))))

         for i in range(3):
                  display(Slist[i])

def display(Sobj):
         print(Sobj.fact())
         print(Sobj.area())
               
main()

