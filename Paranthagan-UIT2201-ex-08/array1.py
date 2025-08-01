"Importing the modules like ctypes and random"
import ctypes
import random

class array(object):
    """ This class create a dynamic array of capacity"""
    
    def __init__(self,capacity):
        if isinstance(capacity,int):        
            """check wheather the object is int"""  
            self.n=0                            
            self.capacity=capacity              
            self.item1=self.make_array(self.capacity)   
        
        else:  
            """if the object is not int data type 
            we  have to extend the capacity of array double the size"""
            self.n=len(capacity)
            self.capacity=len(capacity)
            self.item1=self.make_array(2*self.capacity)

            for i in range(len(capacity)): 
                self.item1[i]=capacity[i]

    def make_array(self,capacity):
        """Returns a new array with  the given capacity """
        return (capacity*ctypes.py_object)()
        
    def __len__(self):
        """"Return number of elements in the array"""
        return len(self.item1)
    
    def __str__(self):
        """ return the string of array"""
        string=""
        for i in range(self.n):
            string=string+(str(self.item1[i]))

            if i !=(self.n -1):
                string=string+","
        return "["+string+"]"
    
    def __getitem__(self,index):
        """return elements at  the index """
        if index<self.n:
            return self.item1[index]
        
        else:
            raise IndexError ("Index Out of Range")
        
    def __setitem__(self,index,element):
        """place the element at the given index"""
        if index<self.n:
            self.item1[index]=element

        else:
            raise IndexError ("Index Out of Range")
        
    def append(self,element):
        """add element at the end of array"""
        if (self.n==self.capacity):
            self.resize(2*self.capacity) 
        self.item1[self.n]=element
        self.n=self.n+1

    def resize(self,capacity):
        """resize the internal array to the given capacity"""
        self.item2=self.make_array(capacity)
        for i in range(self.n):
            self.item2[i]=self.item1[i]
        self.item1=self.item2
        self.capacity=capacity
    
    def insert(self,index,element):
        """insert the element at the given index"""
        if not(0<index<self.n) :
            raise IndexError ("Index Out of Range")
        
        else:
            if (self.n==self.capacity):
                self.resize(2*self.capacity)

            #move the elements one position towards the right
            for i in range(self.n,index,-1):
                self.item1[i]=self.item1[i-1]

            #inserting the element at the given index
            self.item1[index]=element
            self.n=self.n+1

    def delete(self,index):
        """"delete the element in the array"""
        if not(0<index<self.n) :
            raise IndexError ("Index Out of Range")
        
        else:
            if (self.n==self.capacity):
                self.resize(2*self.capacity)  

            #move the elements one position towards the right
            for i in range(index,self.n-1,1):
                self.item1[i]=self.item1[i+1]
            self.n=self.n-1

            #shrink the capacity of array 
            if self.n<(self.capacity//4):
                self.resize(self.capacity//2)

    def extend(self,elements):
        """add the list to another list"""
        for ele in elements:
            self.append(ele)

    def __contains__(self,element):
        """This function return True if the given element is present in the array else False"""
        for i in range(len(self.item1)):
            if self.item1[i]==element:
                return True
            else:
                return False

    def index(self,element):
        """"This function return the index of the element"""
        for i in range(0,self.n):
            if self.item1[i]==element:
                return "index  of element  {} is {}".format(element,i)
            else :
                return "element not present"
            
    def count(self,element):
        """This function gives the no of occurrence of the given element in the array"""
        count=0
        for index in range(0,self.n):
            if self.item1[index]==element:
                count=count+1
        return "no of occurrence of  element {} is {}".format(element,count)
            

#driver code
if __name__ == "__main__":
    obj = array("20")
    for i in range(5):
        obj.append(random.randint(0, 100))
print("Array")
print(obj)
print("\n")
print("Inserting the element 10 at 2")
obj.insert(2,10)
print(obj)
print("\n")
print("Deleting element at 3")
obj.delete(3)
print(obj)
print("\n")
obj.extend([1,2,3,4,5,6,6,7])
print("Extending the element")
print(obj)
print("\n")
print("a=111 present in array")
a=111 in obj
print(a)
print("\n")
print("Return Index of 2")
b=obj.index(2)
print(b)
print("\n")
print("Return Count of 4")
c=obj.count(6)
print(c)
