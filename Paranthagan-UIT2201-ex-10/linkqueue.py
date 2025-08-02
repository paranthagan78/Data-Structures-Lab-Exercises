class Node:
    '''This class is used for creating the Node'''

    __slots__=["item","next"]

    def __init__(self,item=None,next=None):         #Initializing the Constructor
        self.item=item
        self.next=next

class LinkQueue:
    '''This class is used for creating the  linked queue'''

    def __init__(self):                             #Initializing the Constructor
        self.front=Node()
        self.rear=Node()
        self.size=0
    
    def isempty(self):                              #Check wheather the linked queue is empty
        return self.size==0
    
    def enqueue(self,ele):                          #For Adding the element in the end to the linked queue
        temp=Node(ele)
        if self.isempty():
            self.front = temp
            self.rear = temp
        else:
            self.rear.next=temp
            self.rear=temp
        self.size+=1

    def dequeue(self):                               #To Delete the element from the link queue
        if self.isempty():
            return IndexError("Index Out of Range")
        else:
            del_node=self.front.next
            self.front.next=del_node.next
        self.size-=1
    
    def display(self):                               #For Displaying the linked queue
        pos=self.front
        string=""
        while (pos is not None):
            string=string+str(pos.item)
            pos=pos.next
            string=string+","
        return "["+string+"]"
    
#Driver Code

q=LinkQueue()                                        #Creating the Object to Class LinkQueue
print("Checking Empty Condition At Beginning")
print(q.isempty())
print("Adding the Elements")
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
print(q.display())
print("Poping the Elements")
q.dequeue()
q.dequeue()
print(q.display())
