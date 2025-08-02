class Stack:
    '''
    This class is used for creating the Simple Stack
    using the Wrapper class
    '''

    def __init__(self):
        '''This function is called constructor used for initializing'''
        self.list=[]

    def isempty(self):
        '''This function is to check wheather stack is empty'''
        return len(self.list)==0
    
    def insert(self,ele):
        '''This function is used for inserting the element'''
        return self.list.append(ele)
    
    def delete(self):
        '''This function is used for deleting the element'''
        return self.list.pop()
    
    def __len__(self):
        '''This function gives us the length of Stack'''
        return len(self.list)
    
    def str(self):
        '''This function displays the Stack'''
        return str(self.list)

class Queue:
    '''
    This class is used for creating the Simple Queue
    using the Wrapper class
    '''

    def __init__(self):
        '''This function is called constructor used for initializing'''
        self.list=[]
        self.front=0
        self.rear=0

    def isempty(self):
        '''This function is to check wheather Queue is empty'''
        return self.front==self.rear
    
    def enqueue(self,ele):
        '''This function is used for inserting the element'''
        return self.list.append(ele)
    
    def dequeue(self):
        '''This function is used for deleting the element'''
        return self.list.pop(0)
    
    def __len__(self):
        '''This function gives us the length of Queue'''
        return self.rear-self.front
    
    def str(self):
        '''This function displays the Queue'''
        return str(self.list)
    
def palindrome():
    '''This function tells the number is palindrome or not'''

    num=int(input("Enter Number: "))        #getting the number from user
    stack=Stack()                           #Creating instance for Stack
    queue=Queue()                           #Creating instance for Queue
    string=str(num)

    for i in string:
        stack.insert(i)                     #inserting element in the stack
        queue.enqueue(i)                    #inserting element in the queue

    result=0
    result=1
    for i in range(len(stack)):             #iterating the element
        if stack.delete()==queue.dequeue(): #checking the palindrome condition    
            result=0
        else:
            result=1
    
    if result==0:
        print(f"The {num} is Palindrome")

    else:
        print(f"The {num} is Not Palindrome")

palindrome()                                #calling the function
