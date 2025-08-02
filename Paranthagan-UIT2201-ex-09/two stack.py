import ctypes       #Importing the ctypes module

class Exception:    #Creating class for Exception 
    pass

class TwoStack:
    '''
    This class is used for creating the Double Stack
    using the Compact Array Method
    '''
    
    def __init__(self,capacity):
        '''This function is called constructor used for initializing'''
        self.capacity=capacity
        self.top1=0
        self.top2=capacity-1
        self.list=self.makearray(self.capacity)
        
    def makearray(self,capacity):
        '''This function is used for making new array'''
        return (capacity*ctypes.py_object)()
    
    def push(self,stack_no,element):
        '''This function is used for inserting the element'''
        if self.isfull():
            raise Exception("Stack is Full")
        
        else:
            if stack_no == 0:
                self.list[self.top1]=element
                self.top1+=1
            elif stack_no == 1:
                self.list[self.top2]=element
                self.top2-=1
        
    def pop(self,stack_no):
        '''This function is used for deleting the element'''
        if self.isempty():
            raise Exception("Stack is Empty")
  
        if stack_no == 0:
            if self.top1>0:
                del_item=self.list[self.top1-1]
                self.list[self.top1-1]=' '
                self.top1-=1
                return del_item
            else:
                raise Exception("Index out of Range")
            
        elif stack_no == 1:
            if self.top2<self.capacity-1:
                del_item=self.list[self.top2+1]
                self.list[self.top2+1]=' '
                self.top2+=1
                return del_item
            else:
                raise Exception("Index out of Empty")

    def __getitem__(self,index):
        '''This function is used for getting the element'''
        return self.list[index]
    
    def __setitem__(self,index,element):
        '''This function is used for assigning the element'''
        self.list[index]=element

    def isfull(self):
        '''This function checks wheather stack is full'''
        return self.top1>self.top2

    def isempty(self):
        '''This function checks wheather stack is empty'''
        return (self.top2 - self.top1 + 1) == self.capacity

    def __str__(self):
        '''This function dispalys the stack elements'''
        lst=[]
        for element in self:
            if element == None:
                lst.append(" ")
            else:
                lst.append(element)
        return "A "+str(lst)+" B"

def fun():
    '''This function is used for appending and
       deleting the elements from the stack'''
    
    ts=TwoStack(8)                          #Creating the instance for TwoStack

    #appending the elements
    ts.push(0,1)
    ts.push(0,2)
    ts.push(0,3)
    ts.push(0,4)
    ts.push(1,5)
    ts.push(1,6)
    ts.push(1,7)
    ts.push(1,8)
    print("\nThe Double Stack is Full")
    print(ts)
    
    #deleting the elements
    print("\nAn Element is popped from Stack A")
    ts.pop(0)
    print(ts)
    
    #appending the element
    print("\nAn Element is again pushed into the stack B")
    ts.push(1,9)
    print(ts)

fun()                   #Calling the Function
