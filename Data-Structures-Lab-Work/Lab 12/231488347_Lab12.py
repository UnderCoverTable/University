
def insertion_sort(A):

    for k in range(1,len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur

import math
def merge(src, result, start, inc):

    end1 = start + inc
    end2 = min(start + 2*inc, len(src))

    x,y,z = start, start+inc, start
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]; x += 1

        else:
            result[z] = src[y]; y += 1
        z += 1

    if x < end1:
        result[z: end2] = src[x: end1]
    elif y < end2:
        result[z: end2] = src[y: end2]

def merge_sort(S):

    n = len(S)
    logn = math.ceil(math.log(n,2))
    src, dest = S, [None] * n
    for i in (2**k for k in range(logn)):
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)
        src, dest = dest, src
    if S is not src:
        S[0:n] = src[0:n]

def inpalce_quick_sort(S, a, b):

    if a >= b: return
    pivot = S[b]
    left = a
    right = b - 1
    while left <= right:

        while left <= right and S[left] < pivot:
            left += 1

        while left <= right and pivot < S[right]:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]

    inpalce_quick_sort(S, a, left-1)
    inpalce_quick_sort(S, left+1, b)


def task4(S):
    n = len(S)
    logn = math.ceil(math.log(n, 2))
    src, dest = S, [None] * n
    for i in (2 ** k for k in range(logn)):
        for j in range(0, n, 2 * i):
            if len(S) > 50:
                merge(src, dest, j, i)
            else:
                insertion_sort(S)
        src, dest = dest, src
    if S is not src:
        S[0:n] = src[0:n]


def task5(S, a, b):

    if a >= b: return
    pivot = S[b]
    left = a
    right = b - 1
    while left <= right:

        while left <= right and S[left] < pivot:
            left += 1

        while left <= right and pivot < S[right]:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]


    if len(S) < 50:
        inpalce_quick_sort(S, a, left - 1)
        inpalce_quick_sort(S, left + 1, b)
    else:
        insertion_sort(S)





from time import time
from random import randrange
def test():

    times = []

    for func in range(1,6):
        test_list = [randrange(1, 10000, 1) for i in range(10000)]

        if func == 1:
            st = time()
            insertion_sort(test_list)
            et = time()
            times.append(et-st)
        if func == 2:
            st = time()
            merge_sort(test_list)
            et = time()
            times.append(et - st)
        if func == 3:
            st = time()
            inpalce_quick_sort(test_list,0,len(test_list)-1)
            et = time()
            times.append(et - st)
        if func == 4:
            st = time()
            task4(test_list)
            et = time()
            times.append(et - st)
        if func == 5:
            st = time()
            task5(test_list,0,len(test_list)-1)
            et = time()
            times.append(et - st)

    for i in range(len(times)):
        print("Task ",i+1,": ",times[i])


test()















