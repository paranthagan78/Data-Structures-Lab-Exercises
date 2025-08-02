class Node:
    '''This class is used for creating the Node'''

    __slots__=["item","next"]

    def __init__(self,item=None,next=None):     #Initializing the Constructor
        self.item=item
        self.next=next

class SingleList:
    '''This class is used for creating the  linked list'''

    def __init__(self):                          #Initializing the Constructor
        self.head=self.tail=Node()

    def isempty(self):                           #Check wheather the linked list is empty
        return self.head==self.tail
    
    def append(self,ele):                        #For Adding the element in the end to the linked list
        temp=Node(ele)
        self.tail.next=temp
        self.tail=temp
    
    def display(self):                           #For Displaying the linked list 
        pos=self.head.next
        while (pos is not None):
            print(pos.item,end=",")
            pos=pos.next
    
    def find(self,ele):                          #To Find the element from linked list
        pos=self.head.next
        while (pos is not None):
            if (pos.item==ele):
                return pos
            pos=pos.next
        return -1
    
    def insert(self,ele,position):               #To Insert the element in any position of linked list
        pos=self.head.next
        for i in range(position-1):
            pos=pos.next
        temp=Node(ele)
        temp.next=pos.next
        pos.next=temp
    
    def prev_ele_find(self,data):                #It is used to find the previous element's position
        pos=self.head.next
        while (pos is not None):
            if (pos.next.item==data):
                return pos 
            pos=pos.next
        return -1
    
    def delete(self,data):                        #To Delete the element from the link list
        prev_ele=self.prev_ele_find(data)
        del_ele=prev_ele.next
        prev_ele.next=del_ele.next
    
#Driver Code

s=SingleList()                                    #Creating the Object to Class SingleList
print("Checking Empty Condition At Beginning")
print(s.isempty())
print("Adding the Elements")
s.append(1)
s.append(2)
s.append(3)
print(s.display())
print("Checking Empty Condition")
print(s.isempty())
print("Finding the Element 2")
print(s.find(2))
print("Inserting the Element 10 at index 2")
s.insert(10,2)
print(s.display())
print("Inserting the Element 12 at index 1")
s.insert(12,1)
print(s.display())
print("Deleting the Element 12")
s.delete(12)
print(s.display())
