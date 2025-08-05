from AbtractBinaryTree import AbstractBinaryTree        #importing the AbtractBinaryTree class from AbtractBinaryTree file


class LinkedBinaryTree(AbstractBinaryTree):
    """
       This class is used for creating the LinkedBinaryTree,
       and it contains below methods.
    """

    class BTNode:
        """This class creates a node for LinkedBinaryTree"""
        __slots__ = ["item", "left", "right", "parent"]

        def __init__(self, item, left=None, right=None, parent=None):
            """Initializing the Constructor"""
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent

        def getitem(self):
            """Return the item stored in the node"""
            return self.item

        def setitem(self, item):
            """Set the item stored in the node"""
            self.item = item

    __slots__ = ["root", "size"]

    def __init__(self, item=None, t_left=None, t_right=None):
        """Initializing the Constructor"""
        self.root = None                    #Initialize the root node
        self.size = 0                       #Initialize the size of the tree
        self.string = ""                    #Initialize an empty string
        if item is not None:
            self.root = self.addRoot(item)  #Create the root node with the given item
        if t_left is not None:
            if t_left.root is not None:
                t_left.root.parent = self.root  #Set the parent of the left subtree to the root
                self.root.left = t_left.root    #Set the left subtree of the root
                self.size += t_left.size        #Update the size of the tree
                t_left.root = None              #Clear the root of the left subtree
        if t_right is not None:
            if t_right.root is not None:
                t_right.root.parent = self.root     #Set the parent of the right subtree to the root
                self.root.right = t_right.root      #Set the right subtree of the root
                self.size += t_right.size           #Update the size of the tree
                t_right.root = None                 #Clear the root of the right subtree

    def addRoot(self, item):
        """Adds a root node with the given item to the tree"""
        if self.root is not None:
            raise ValueError("Root already exists")
        else:
            self.root = self.BTNode(item)
            self.size += 1
            return self.root

    def __len__(self):
        """Returns the number of nodes in the tree"""
        return self.size

    def getParent(self, pos):
        """Returns the parent position of the given position"""
        return pos.parent

    def getLeft(self, pos):
        """Returns the left child position of the given position"""
        return pos.left

    def getRight(self, pos):
        """Returns the right child position of the given position"""
        return pos.right

    def getRoot(self):
        """Returns the root position of the tree"""
        return self.root

    def getSize(self):
        """Returns the number of nodes in the tree"""
        return self.size

    def getNum_children(self, pos):
        """Returns the number of children of the given position"""
        if pos is None:
            return 0
        else:
            return 1 + self.getNum_children(pos.left) + self.getNum_children(pos.right)

    def addLeft(self, item, pos=None):
        """Adds a left child node with the given item to the specified position 'pos' or the root if 'pos' is None"""
        if pos is None:
            pos = self.root
        if self.getLeft(pos) is not None:
            raise ValueError("Left child already exists")
        else:
            pos.left = self.BTNode(item, parent=pos)
            self.size += 1
            return pos.left

    def addRight(self, item, pos=None):
        """Adds a right child node with the given item to the specified position 'pos' or the root if 'pos' is None"""
        if pos is None:
            pos = self.root
        if self.getRight(pos) is not None:
            raise ValueError("Right child already exists")
        else:
            pos.right = self.BTNode(item, parent=pos)
            self.size += 1
            return pos.right

    def preorder(self, pos):
        """Performs a preorder traversal starting from the given position"""
        res=f"[{str(pos.item)} "
        if pos.left is not None:
            res+=self.preorder(pos.left)
        if pos.right is not None:
            res+=self.preorder(pos.right)
        res+=']'
        return res

    def postorder(self, pos):
        """Performs a postorder traversal starting from the given position"""
        if pos.left is not None:
            self.postorder(pos.left)
        if pos.right is not None:
            self.postorder(pos.right)
        self.string += str(pos.item) + ","

    def inorder(self, pos):
        """Performs an inorder traversal starting from the given position"""
        if pos.left is not None:
            self.inorder(pos.left)
        self.string += str(pos.item) + ","
        if pos.right is not None:
            self.inorder(pos.right)

    def __str__(self):
        """Returns a string representation of the tree by performing preorder traversal"""
        
        return self.preorder(self.root)
       
    