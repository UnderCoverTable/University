#TASK 4

import math
class Complex:

    def __init__(self,real=0,img=0):
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
        print("-"*6)

    def Absolute_greater_then_4(self):
        chk=0
        ch=0
        for i in range(0,len(self.NumbersList)):
            a = int(self.NumbersList[i][0])
            b = int(self.NumbersList[i][1][0])
            abs = math.sqrt(a**2+b**2)
            if abs > 4:
                if ch == 0:
                    print("Complex numbers, with Absolute > 4: ")
                ch = 1
                chk=1
                print(self.NumbersList[i][0],"+",self.NumbersList[i][1],"-> Absolute = ",abs)
        if chk == 0:
            print("No complex numbers with Absolute value greater then 4")

    def Addition(self,real,img):
        sum_real = self.Real + real
        sum_img = self.Imaginary + img
        print("(",self.Real,"+",self.Imaginary,"i",")"," + ","(",real,"+",img,"i",")")
        print("= ",sum_real,"+",sum_img,"i")
        print("-"*6)

    def Subtraction(self,real,img):
        sum_real = self.Real - real
        sum_img = self.Imaginary - img
        print("(",self.Real,"+",self.Imaginary,"i",")"," - ","(",real,"+",img,"i",")")
        print("= ",abs(sum_real),"+",sum_img,"i")
        print("-" * 6)

    def Multiplication(self,real,img):
        a1 = self.Real * real
        a2 = self.Real * img

        b1 = self.Imaginary * real
        b2 = self.Imaginary * img

        if img<0 :
            final_real = a1 + abs(b2)
            final_img = a2 + b1
            print("(",self.Real,"+",self.Imaginary,"i",")"," * ","(",real,"+",img,"i",")")
            print("= ",final_real, "+", final_img, "i")

        else:
            final_real = a1 - b2
            final_img = a2 + b1
            print("(", self.Real, "+", self.Imaginary, "i", ")", " * ","(", real, "+", img, "i", ")")
            print("= ",final_real, "+", final_img, "i")
        print("-"*6)


    def div_help(self,real,img):
        a1 = self.Real * real
        a2 = self.Real * img

        b1 = self.Imaginary * real
        b2 = self.Imaginary * img

        if img <0:
            final_real = a1 + abs(b2)
            final_img = a2 + b1
            aa = str(final_real)
            bb = str(final_img)
            return aa+"+"+bb+"i"
        else:
            final_real = a1 - b2
            final_img = a2 + b1
            aa = str(final_real)
            bb = str(final_img)
            return aa + "+" + bb+"i"

    def Division(self,real,img):
         d = Complex(real,img)
         print("(",self.Real,"+",self.Imaginary,"i",")"," / ","(",real,"+",img,"i",")")

         if img<0:
             nume = self.div_help(real,abs(img))
             denom = d.div_help(real,abs(img))
             print("=",nume,"/",denom)
         else:
             nume = self.div_help(real,-img)
             denom = d.div_help(real, -img)
             print("=",nume, "/", denom)
         print("-"*6)

def complex_main():
    test = Complex()
    test.User_ComplexNumbers()
    test.Absolute_greater_then_4()

    n = Complex(2,3)
    n.Addition(5,-6)
    n.Subtraction(-6,5)
    n.Multiplication(4,-6)
    n.Division(7,-1)

#complex_main()





