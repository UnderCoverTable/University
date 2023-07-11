def HeapSort(A, n):
    print("RAW: " ,A) # Prints raw data

    BuildHeap(A,n) # --------> nlog4n
    print("BUILT MIN HEAP: " ,A) # Prints after building initial heap

    m = n
    #Swaps root and last node
    while  m >= 1:
        temp = A[0]
        A[0] = A[m]
        A[m] = temp

        m -= 1
        
        # Prints the array and the seperated/sorted elements
        print(A[0:m+1]," -|- ", A[len(A[0:m+1]):])
        if m==0:
            print("Sorted: ",A)

        # Fixes heap
        Heapify(A,0,m) # --------> mlog4n

def Heapify(A, i, m): # --------> log4n
    #Assigns the 4 children to each parent
    if i == 0:
        left = i+1
        middleL = i+2
        middleR = i+3
        right = i+4
        min = i
    else:
        left = 4*i + 1
        middleL = 4*i + 2
        middleR = 4*i + 3
        right = 4*i + 4
        min = i

    #Finds the smallest element and stores its index in min
    if (left <= m) and (A[left] < A[min]):
        min = left
    if (middleL <= m) and (A[middleL] < A[min]):
        min = middleL
    if (middleR <= m) and (A[middleR] < A[min]):
        min = middleR
    if (right <= m) and (A[right] < A[min]):
        min = right
    
    #if min is a different index then where it started, it swaps
    if (min != i):

        temp = A[i]
        A[i] = A[min]
        A[min] = temp

        Heapify(A, min, m)

# Builds heap
def BuildHeap(A, n): # --------> nlog4n
    for i in range(n,-1,-1):
        Heapify(A, i, n)



l = [3, 1, 9, 18, 77, 55, 23, 92, 2, 33, 22, 66, 55, 11, 37, 33, 19]
HeapSort(l,len(l)-1)
