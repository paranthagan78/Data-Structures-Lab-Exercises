class Node:
    '''This class is used for creating the Node'''

    __slots__=["item","next"]

    def __init__(self,item=None,next=None):         #Initializing the Constructor
        self.item=item
        self.next=next
    
class LinkStack:
    '''This class is used for creating the  linked stack'''

    def __init__(self):                             #Initializing the Constructor
        self.top=Node()
        self.size=0
    
    def isempty(self):                              #Check wheather the linked stack is empty
        return self.top.next is None
    
    def peek(self):                                 #It gives the peek value of linked stack
        return self.top.item
    
    def push(self,ele):                             #For Adding the element in the end to the linked stack
        temp=Node(ele)
        temp.next=self.top.next
        self.top.next=temp
        self.size+=1
    
    def pop(self):                                  #For Deleting the element in the end to the linked stack
        if self.isempty():
            return IndexError("Index Out of Range")
        
        else:
            del_node=self.top.next
            self.top.next=del_node.next
            self.size-=1
        
    def display(self):                              #To Display the linked stack
        pos=self.top.next
        string=""
        while (pos is not None):
            string=string+str(pos.item)
            pos=pos.next
            string=string+","
        return "["+string+"]"
    
#Driver Code

s=LinkStack()                                       #Creating the object to Class LinkStack

print("Checking Empty Condition At Beginning")
print(s.isempty())
print("Adding the Elements")
s.push(10)
s.push(12)
s.push(14)
s.push(16)
s.push(18)
print(s.display())
print("Finding the Peek Value")
print(s.peek())
print("Poping the Elements")
s.pop()
s.pop()
print(s.display())
