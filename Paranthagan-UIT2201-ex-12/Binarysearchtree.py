from LinkedBinarytree import LinkedBinaryTree
class Binarysearchtree(LinkedBinaryTree):
    def __init__(self,item=None,t_left=None,t_right=None):
        super().__init__(item,t_left,t_right)
    
    def Construct(self,item,pos):
        if pos is None:
            self.addRoot(item)

        elif item < pos.item :
            if pos.left is  None :
                pos.left = self.addLeft(item,pos) 
            else:
                self.Construct(item,pos.left)
        
        elif item > pos.item:
            if pos.right is None:
                pos.right = self.addRight(item,pos)
            else:
                self.Construct(item,pos.right)
    
    def search(self,item,pos):
        if pos is None:
            return None
        if item < pos.item :
            return self.search(item,pos.left)
        if item > pos.item :
            return self.search(item,pos.right)
        if item ==pos.item :
            return pos
        
    def findmax(self,pos):
        if pos is None:
            return None
        if pos.right is not None:
            return self.findmax(pos.right)
        else:
            return pos
            

    def findmin(self,pos):
        if pos is None:
            return None
        if pos.left is not None:
            return self.findmin(pos.left)
        else:
            return pos
        
    def delete(self,item,pos):
        if pos is None:
            return None
        if item < pos.item:
            pos.left =self.delete(item,pos.left)
        elif item > pos.item :
            pos.right =self.delete(item,pos.right)
        else:
            if pos.left is None:
                temp = pos.right
                pos = None
                return temp
            elif pos.right is None:
                temp = pos.left
                pos = None
                return temp
            else:
                temp = self.findmin(pos.right)
                pos.item = temp.item
                pos.right = self.delete(temp.item,pos.right )
        return pos
    

b=Binarysearchtree(40)
b.Construct(50,b.root)
b.Construct(60,b.root)
b.Construct(70,b.root)
b.Construct(80,b.root)
b.Construct(90,b.root)
b.Construct(30,b.root)
b.Construct(20,b.root)
b.Construct(10,b.root)
print("Binary Search Tree")
print(b)
print("Search")
print(b.search(70,b.root))
print("Deleting")
b.delete(90,b.root)
print(b)
