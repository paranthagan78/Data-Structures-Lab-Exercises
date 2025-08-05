from AbstractTree import AbstractTree           #importing the class AbstractTree from AbstractTree
from abc import abstractmethod                  #importing the abstract method from abc module

class AbstractBinaryTree(AbstractTree):
    """
       This class is used for creating the abstract binary tree,
       and it contains below methods.
    """

    @abstractmethod
    def getLeft(self, pos):
        """Return the left child of the given position"""
        pass

    @abstractmethod
    def getRight(self, pos):
        """Return the right child of the given position"""
        pass

    def getChildren(self, pos):
        """Return the children of the given position"""
        if pos is None:
            return None
        if self.getLeft(pos) is not None:
            yield self.getLeft(pos)
        if self.getRight(pos) is not None:
            yield self.getRight(pos)

    def sibling(self, pos):
        """Return the sibling of the given position"""
        parent = self.getParent(pos)
        if parent is None:
            return None
        if pos == self.getRight(parent):
            return self.getLeft(parent)
        else:
            return self.getRight(parent)
