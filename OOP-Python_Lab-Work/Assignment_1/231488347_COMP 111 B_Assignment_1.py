# QUESTION 1
list1 = [7, 1, 7, 3, 4, 19, 8, 1, 13, 7, 19]
prime_list = []
distinct = []
prime_dic = {}

def primer(lst):
    # Adds all prime numbers from the original list
    ##to a seperate list with just prime numbers.
    for ii in range(0, len(lst)):
        if lst[ii] > 1:
            for i in range(2, lst[ii]):
                if lst[ii] % i == 0:
                    break
            else:
                prime_list.append(lst[ii])

    # Makes a seperate list with only distinct prime numbers
    ##not adding repetitions
    for num in range(0, len(prime_list)):
        if prime_list[num] not in distinct:
            distinct.append(prime_list[num])

    # Adds each prime as a key into the dictionary
    ## and their count as the value
    for elements in prime_list:
        prime_dic[elements] = lst.count(elements)

    # prints each key and value set
    for elements in prime_dic:
        print(elements, ":", prime_dic.get(elements))
primer(list1)

#QUESTION 2
def dupe_words(file):
    infile = open(file, "r")
    dupe_list = []

    #Adds all words from file to a list
    for line in infile:
        a = line
    word_list = a.split()

    #converts all words in list  to lowercase
    for i in range(0, len(word_list)):
        word_list[i] = word_list[i].lower()

    #adds all repeated words from previous list to a new one, and
    ##prints the repeated words
    for elements in word_list:
        if word_list.count(elements) > 1 and elements not in dupe_list:
            dupe_list.append(elements)
    infile.close()

    print(dupe_list)
user_file=input("Please enter a file name : ")
dupe_words(user_file)


# QUESTION 3
list3 = [2, 2, 2, 5, 5, 6, 6, 7, 6, 8, 6, 6, 9]
ex_list = []
counter = 0
a = len(list3)

def dupe_pop(lst):
    global counter
    global a

    #Base case works, when length of the original list reaches 0 and
    ##the counter is equal to the length of the original list - 1.
    ###and the list in printed without duplicate numbers
    if len(lst) == 0 and counter == a - 1:
        print(ex_list)
    else:
        # Does the same work as the lines mentioned below, but when the list
        # is of length 1.
        if len(lst) == 1:
            if len(ex_list) == 0:
                ex_list.append(lst[0])
                lst.pop()
                return dupe_pop(lst)

            if lst[0] == ex_list[len(ex_list) - 1]:
                lst.pop()
                return dupe_pop(lst)
            else:
                ex_list.append(lst[0])
                lst.pop()
                return dupe_pop(lst)
        # if the first and second value are the same in the list
        ## it only removes the duplicate from the orignal list
        if lst[0] == lst[1]:
            lst.remove(lst[0])
            counter += 1
            return dupe_pop(lst)
        # if the first and second value are not the same
        ## adds the value to a seperate list and removes it from
        ### the orignal list
        if lst[0] != lst[1]:
            ex_list.append(lst[0])
            lst.remove(lst[0])
            counter += 1
            return dupe_pop(lst)
dupe_pop(list3)

# QUESTION 4
def palin(st):
    if len(st) == 2:
        if st[0] == st[1]:
            return "TRUE"

    if len(st) == 3:
        if st[0] == st[len(st) - 1]:
            return "TRUE"
    else:
        # compares the first and last letters and if they are the same,
        # calls the function again removing the first and last letters from the string.
        if st[0] == st[len(st) - 1]:
            st = st[1:]
            return palin(st[:len(st) - 1])
        # If the first and last letters are not the same, it is not a plaindrome
        if st[0] != st[len(st) - 1]:
            return "FALSE"
string_4 = input("Please enter a string (Palindrome check) : ")
print(palin(string_4))


# QUESTION 5
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10
         ,11,12,13,14,15,16,17,18,19,20]
num_list = []

def prefix(n, lst):
    #once n reaches zero. it prints the list in reverse
    if n == 0:
        print(num_list[::-1])
    else:
        #Adds numbers from the list, n amount of times to a new list.
        #From the entered n, till 0
        num_list.append(lst[n - 1])
        n -= 1
        return prefix(n, lst)
num_5 = int(input("Please enter a number (prefix) : "))
prefix(num_5, list5)


# QUESTION 6
list_6 = []
n = 0
m = 1
counter_6 = 0

def list_make(st):
    # makes a list out of the characters from the entered string
    for i in range(0, len(st)):
        list_6.append(st[i])
    return list_6

def swap(lst):
    global counter_6
    global n
    global m

    if counter_6 == len(lst) // 2:
        for elements in lst:
            print(elements, end="")
    else:
        # replaces 2 subsequent letters with each other
        a = lst[n]
        lst[n] = lst[m]
        lst[m] = a
        n += 2
        m += 2
        counter_6 += 1
        return swap(lst)


# keeps asking the user to enter a string of even length,
##if the users string is of odd length

string_6 = input("Please enter a string (swap): ")
if len(string_6) % 2 != 0:
    while len(string_6) % 2 != 0:
        print("Please enter a string with even length")
        string_6= input("Please enter a string (swap): ")
        if len(string_6)%2==0:
            swap(list_make(string_6))
else:
    swap(list_make(string_6))
