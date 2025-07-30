#importing the random and time module
import random
import timeit
import math

def bubble_sort(lst):
    start_time = timeit.default_timer()
    '''
    This function can sort the given list by swapping the adjacent elements.
    '''
    no_comp=0
    no_swap=0
    n=len(lst)                                           #To find the length of list
    for i in range(0,n-1):                              
        for j in range(0,n-i-1):
            no_comp+=1
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]         #Simultaneous Swapping
                no_swap+=1
    print("Bubble Sort: ",lst)
    print("Number of Comparsion: ",no_comp)
    print("Number of Swap: ",no_swap)
    print("Ratio Analysis for n: ",no_comp/n)
    print("Ratio Analysis for n2: ",no_comp/(n**2))
    print("Ratio Analysis for n3: ",no_comp/(n**3))
    print("Ratio Analysis for log n: ",no_comp/(math.log(n)))
    time = timeit.default_timer() - start_time
    print("Exact Time: ",time)                   
    return lst

def selection_sort(lst1):
    start_time = timeit.default_timer()
    '''
    This function can sort the given list by finding the minimum value in list.
    And 
    '''
    no_comp=0
    no_swap=0
    n=len(lst1)                                                  #To find the length of list
    for i in range(0,n):
        min_ind=i
        for j in range(i+1,n):
            no_comp+=1
            if lst1[j]<min_ind:
                min_ind=j
        no_comp+=1
        if i!=min_ind:
            lst1[j],lst1[min_ind]=lst1[min_ind],lst1[j]        #Simultaneous Swapping
            no_swap+=1
    print("Selection Sort: ",lst1)
    print("Number of Comparsion: ",no_comp)
    print("Number of Swap: ",no_swap)
    print("Ratio Analysis for n: ",no_comp/n)
    print("Ratio Analysis for n2: ",no_comp/(n**2))
    print("Ratio Analysis for n3: ",no_comp/(n**3))
    print("Ratio Analysis for log n: ",no_comp/(math.log(n)))
    time = timeit.default_timer() - start_time 
    print("Exact Time: ",time)
    return lst1

def insertion_sort(lst):
    start_time = timeit.default_timer()
    '''
    This function sorts the given sequence in ascending order and return the sorted list.
    '''

    no_comp = 0
    no_swap = 0
    n=len(lst)                                               #To find the length of list
    for i in range(1, len(lst)):
        val = lst[i]
        j = i-1
        while j >= 0 and lst[j] > val:
            no_comp += 1
            lst[j+1] = lst[j]                                 #Simultaneous Swapping
            no_swap += 1
            j -= 1
        lst[j+1] = val
    print("Insertion Sort: ",lst)
    print("Number of Comparsion: ",no_comp)
    print("Number of Swap: ",no_swap)
    print("Ratio Analysis for n: ",no_comp/n)
    print("Ratio Analysis for n2: ",no_comp/(n**2))
    print("Ratio Analysis for n3: ",no_comp/(n**3))
    print("Ratio Analysis for log n: ",no_comp/(math.log(n)))
    time = timeit.default_timer() - start_time
    print("Exact Time: ",time)
    return lst1

#Creating a list 
lst=[]
num=int(input("Enter Number of Elements: "))
last=int(input("Enter Last Number: "))
for i in range(num):
    a=random.randint(1,last)
    lst.append(a)                                       #adding the elements in the list
print("Orginal List: ",lst)

#Cloning
lst1=lst.copy()

#Function Calling
bubble_sort(lst)
selection_sort(lst)
insertion_sort(lst)
