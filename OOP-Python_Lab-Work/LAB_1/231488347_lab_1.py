#Q1
user_str=input("Please enter your string:")

def con_count(strr):
    counter=0
    for i in range(0,len(strr)):
        if strr[i]=="a" or strr[i]=="e" or strr[i]=="i" or strr[i]=="o" or strr[i]=="u":
            counter+=1
    print(len(strr)-counter)
con_count(user_str)


#Q2
user_strr=input("Please enter your word:")
def str_check(strr):
    check=0
    list_word=[]
    for i in range(0,len(strr)):
        list_word.append(strr[i])#[a,b,c]
    for i in range(0,len(list_word)):
        if list_word.count(list_word[i])>1:
            check="1"
    if check=="1":
        print("Word is not unique")
    else:print("Word is unique")
            
str_check(user_strr)

#Q3
def lucky_number():
    counter=0
    while counter<5:
        lucky_num="9"
        user_guess=input("Guess the number:")
        counter+=1
        if user_guess==lucky_num:
            print("YOU WIN")
            break
        elif counter==5:
            print("YOU LOSE")
        else: print("Try again")
lucky_number()


#Q4
def strong_pass(passwd):
    counter=0
    if len(passwd)>=6:
        counter+=1
    for i in range(0,len(passwd)):
        if passwd[i].isupper():
            counter+=1
            break
    for i in range(0,len(passwd)):
        if passwd[i].islower():
            counter+=1
            break
    if counter==3:
        return True
print(strong_pass("I<3scs108"))
         
















