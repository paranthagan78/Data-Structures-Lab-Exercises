from LinkedBinarytree import LinkedBinaryTree               #importing the LinkedBinarytree class from LinkedBinarytree file
class mirrortree(LinkedBinaryTree):
    """
       This class is used for creating the mirrortree,
       and it contains below methods.
    """
    def __init__(self, item=None, t_left=None, t_right=None):
        "Initializing the Constructor"
        super().__init__(item, t_left, t_right)             #using the super()
    
    def Mirror(self,pos):
        """mirror function swaps the children of a node"""
        if pos is None:
            return None
        else:
            pos.left, pos.right = pos.right, pos.left           #Simultaneous Swappimg
            self.Mirror(pos.left)
            self.Mirror(pos.right)
    
    
    
#Driver Code
if __name__ == "__main__":
    t1=LinkedBinaryTree(11)
    t2=LinkedBinaryTree(22)
    t3=LinkedBinaryTree(1,t1,t2)

    x1=LinkedBinaryTree(1)
    x2=LinkedBinaryTree(2)
    x3=LinkedBinaryTree(10,x1,x2)
    
    y=LinkedBinaryTree(2,x3,t3)
    print("Orginal Tree")
    print(y)
    
    M=mirrortree()
    M.Mirror(y.root)
    print("Mirror Tree")
    print(y)