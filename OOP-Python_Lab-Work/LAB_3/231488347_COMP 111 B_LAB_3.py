#Q1
li=[6,9,3,2]
def sum_list_backwards(list1):
    if len(list1)==1:
        return list1[0]
    else:
        last_n=list1[len(list1)-1]
        list1.pop()
        return sum_list_backwards(list1)+last_n
print("The sum is:",sum_list_backwards(li))

#Q2
strr="AppLeSoL"
def capitals(st):
    cap_letters=""
    if st=="":
        return st
    else:
        if st[len(st)-1].isupper():
            cap_letters=cap_letters+st[len(st)-1]
        return cap_letters+capitals(st[:-1])
print("The capital letters in the given string are:",capitals(strr))

#Q3
num=5
def harmonic_sum(n):
    if n==1:
        return 1
    else:
        return 1/n+harmonic_sum((n-1))
print("The harmonic sum is:","%0.2f" % harmonic_sum(num))



#Q5
num=5
counter=0
def hailstone(n):
    global counter
    if n==1:
        return 1

    else:
        counter+=1
        if counter==1 and n%2==0:
            return hailstone(n/2)
        if counter==1 and n%2!=0:
            return hailstone(3*n+1)


        if n%2==0:
            print("%d" % n)
            return hailstone(n/2)

        elif n%2!=0:
            print("%d" % n)
            return hailstone(3*n+1)

print(hailstone(num))

