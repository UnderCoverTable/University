##TASK1

# Prefix Average 1

def prefix_average1(S):
    n = len(S)
    A = [0] * n

    for j in range(n):
        total = 0

        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)

    return A


# Prefix Average 2

def prefix_average2(S):
    n = len(S)
    A = [0] * n
    
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)
        
    return A


# Prefix Average 3

def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    
    for j in range(n):
        total += S[j]
        A[j] = total / (j+1)
        
    return A

from time import time

input_list = []
len_list = []
time_list1 = []
time_list2 = []
time_list3 = []


for i in range(0,150):
    
    input_list.append(i)
    len_list.append(len(input_list))
    

#Running time of prefix average 1
    start_time1 = time()

    print(prefix_average1(input_list))

    end_time1 = time()

    time_list1.append(end_time1 - start_time1)

    
#Running time of prefix average 2
    start_time2 = time()

    print(prefix_average2(input_list))

    end_time2 = time()

    time_list2.append(end_time2 - start_time2)


#Running time of prefix average 3
    start_time3 = time()

    print(prefix_average3(input_list))

    end_time3 = time()

    time_list3.append(end_time3 - start_time3)



import matplotlib.pyplot as plt

plt.yscale("log")
plt.ylabel("Running Time")
plt.xscale("log")
plt.xlabel("Size of input")

plt.plot(len_list,time_list1, color = "Blue")
plt.plot(len_list,time_list2, color = "Red")
plt.plot(len_list,time_list3, color = "Green")
plt.show()


##TASK2


in_list = []
ti_list = []
len_n = []

for i in range(0,500):
    len_n.append(len(in_list))
    in_list.append(i)

    st_time = time()
    in_list = sorted(in_list)
    print(in_list)
    en_time = time()

    elapsed_time = en_time - st_time
    ti_list.append(elapsed_time)


   
import matplotlib.pyplot as plt2

plt2.xticks(len_n)
plt2.plot(len_n,ti_list)
plt2.show()


##TASK3 

def unique1(S): 

    for j in range(len(S)):
        for k in range(j+1,len(S)):
            if S[j] == S[k]:
                return False
    return True

def unique2(S): 

    temp = sorted(S)
    for j in range(1,len(temp)):
        if S[j-1] == S[j]:
            return False
    return True

def unique3(S,start,stop):
    if stop - start <= 1: return True
    elif not unique3(S, start, stop - 1): return False
    elif not unique3(S, start+1, stop): return False
    else: return S[start] != S[stop-1]



elapsed = 0
counter = 25000
input_list = list(range(1,25000)) # Adjusted counter and input_list size according
                                    ## to each algorithms speed.
while elapsed <= 60:

    start_time = time()

    print(unique1(input_list)) ## n = 25k
    #print(unique2(input_list)) ## n = 7+E7 , 20s. Gives memory error due to list size.
    #print(unique3(input_list,0,len(input_list)))## n = 28

    end_time = time()
    
    for i in range(100): # Adjusted the range of the increment in n according to each algorithm. 
        counter += 1
        input_list.append(counter)
    
    elapsed = end_time - start_time
    print(elapsed)

print("Max input : ",len(input_list), "Time taken:",elapsed,"s")



    

