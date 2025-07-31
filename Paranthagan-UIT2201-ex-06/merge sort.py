import timeit
import random

'''
Importing the random module to generate random numbers 
and timeit module to find the time taken by the program
'''

#initialize
start = timeit.default_timer()      
compare=0

def sep(lst):                   #function for seperating the list
    if len(lst)<2:
        return lst
    else:
        mid=len(lst)//2
        return merge(sep(lst[:mid]),sep(lst[mid:]))

def merge(A,B):                 #function for merging the list

    #initialize
    global compare
    i=0
    j=0
    m=len(A)
    n=len(B)
    sort_list=[]                #creating the empty list

    while i<m and j<n:          #iterating the loop
        
        if A[i]<=B[j]:
            compare+=1
            sort_list.append(A[i])  
            i+=1

        elif B[j]<=A[i]:
            compare+=1   
            sort_list.append(B[j])
            j+=1    
    
    if i<m:
        sort_list.extend(A[i:])
    elif j<n:
        sort_list.extend(B[j:])
    return sort_list            #this will print the sorted list

time = timeit.default_timer() - start   

lst=[]                          #creating the unsorted list
n=int(input("Enter Number of Terms: "))
for i in range(n):
    a=random.randint(1,100)
    lst.append(a)
print("Unsort: ",lst)
print("\n")
print("Merge Sort: ", sep(lst))     #calling the function
print("Compare: ",compare)
print("Time: ",time)
