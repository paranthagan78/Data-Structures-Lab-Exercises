import timeit
import random


start = timeit.default_timer()

compare = 0
def binear_search(lst, find, low, high):
    global compare
    mid = (high + low) // 2
    compare += 2

    if low > high:
        return -1
    
    if lst[mid] == find:
        return mid
    elif lst[mid] > find:
        compare += 1
        return binear_search(lst, find , low, mid-1)
    else:
        return binear_search(lst, find , mid+1, high)

time = timeit.default_timer() - start
        
if __name__ == "__main__":
    for i in [10,100,1000,1000]:
        lst = [random.uniform(-100.00,100.00) for _ in range(i)]
        lst.sort()
        find_idx = random.randint(0,len(lst)-1)
        find = lst[find_idx]
        print(binear_search(lst, find, 0, len(lst)))
        print("Compare:",compare)
        print("Time: ",time)
    
