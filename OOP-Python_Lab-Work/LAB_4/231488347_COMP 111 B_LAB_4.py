#Q1
def isLucky(n):
    if n[len(n) - 1] == "8":
        return "Lucky!!"
    if len(n) == 1:
        if n != 8:
            return "Not lucky :("
    else:
        return isLucky(n[:-1])

user_num=input("Enter number for lucky number check:")
print(isLucky(user_num))
print()

#Q2
nums_list = [8, 5, 6, 2, 1, 4, 3]
print(nums_list)
count=0
def even_count(list1):
    global count
    if len(list1) == 0:
        return count
    else:
        if list1[len(list1) - 1] % 2 == 0:
            count+=1
            list1.pop()
            return even_count(list1)

        if list1[len(list1) - 1] % 2 != 0:
            list1.pop()
            return even_count(list1)
print("the number of even numbers in the list are: ",even_count(nums_list))
print()

#Q3
def find(text, str1):

    if text[:len(str1)] == str1:
        return "YES"
    if len(text) == len(str1):
        if text == str1:
            return "YES"
        else:
            return "NO"
    else:
        return find(text[1:], str1)
user_t=input("Enter the text: ")
user_s=input("Enter the str you want to be compared: ")
print("Does your text contain the string? ",find(user_t, user_s))
print()

#Q4
aux = [0, 1, 1, 2]
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n < len(aux):
        return aux[n - 1]
    else:
        fibs = fib(n - 1) + fib(n - 2)

    if fibs not in aux:
        aux.append(fibs)
    return fibs

user_n=int(input("Enter the nth term in the Fibonacci seq you require: "))
print(fib(user_n))
print("The Fibonacci sequence till the nth term: ",aux)
# with the auxiliry list we can find a much larger nth term in the fibonacci sequnce
## compared to a normal fibonacci function.

