import timeit
import random

'''
Importing the random module to generate random numbers 
and timeit module to find the time taken by the program
'''

#initialize
start = timeit.default_timer()
compare = 0

def partition(lst, begin, end):         #this function is for partition

    #initialize
    global compare
    median(lst,begin,end)
    pivot = lst[end]
    i = begin
    j = end - 1

    while i<=j:                         #iterating the loop
        compare += 1
        while lst[i] < pivot and i<=end:
            compare += 2
            i += 1
        while lst[j] > pivot and j>=begin:
            compare += 2
            j -= 1
        compare += 1
        if i<j:
            lst[i],lst[j] = lst[j],lst[i]
            i += 1
            j -= 1
    
    compare += 1
    if i < pivot:
        lst[i],lst[end] = lst[end],lst[i]
    return i

def quick_sort(lst, begin, end):        #this function is for sorting
    global compare
    compare += 1
    if begin < end:
        p = partition(lst, begin, end-1)
        quick_sort(lst, begin, p-1)
        quick_sort(lst, p+1, end)

def median(lst, begin, end):            #this function is for more efficient sorting
    global compare
    mid = (begin+end)//2
    compare += 3
    if lst[mid] > lst[begin]:
        lst[mid],lst[begin] = lst[begin],lst[mid]
    if lst[mid] < lst[end]:
        lst[mid],lst[end] = lst[end],lst[mid]
    if lst[begin] > lst[end]:
        lst[begin],lst[end] = lst[end],lst[begin]
    lst[mid],lst[end]=lst[end],lst[mid]
    
end = timeit.default_timer()
time = end-start

#driver code
if __name__ == "__main__":
    for i in [10,100,500,1000,5000,1000]:
        lst = [random.uniform(-100.00,100.00) for _ in range(i)]
        begin=0
        end=len(lst)
        quick_sort(lst,begin,end)           #function calling
        print(lst)
        print("Compare: ",compare)
        print("Time: ",time)
        