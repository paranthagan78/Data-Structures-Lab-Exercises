from abc import ABC,abstractmethod          #importing the abstract method from abc module

class AbstractTree(ABC):
    """
       This class is used for creating the abstract tree,
       and it contains below methods.
    """

    @abstractmethod
    def getRoot(self):
        """Return Position of Root in the Tree"""
        pass

    @abstractmethod
    def getParent(self, pos):
        """Return the parent position of the Root"""
        pass

    @abstractmethod
    def getNum_children(self, pos):
        """Return the number of children of the given position"""
        pass

    @abstractmethod
    def getChildren(self, pos):
        """Return children position of the given position"""
        pass

    @abstractmethod
    def __len__(self):
        """Return the total number of position in the tree"""
        pass

    def isRoot(self, pos):
        """Return True if 'pos'=root, otherwise False"""
        return self.getRoot() == pos

    def isLeaf(self, pos):
        """Return True if 'pos' is a leaf node, otherwise False"""
        return self.getNum_children(pos) == 0

    def isEmpty(self):
        """Returns True if the tree is empty, otherwise False"""
        return len(self) == 0

    def depthN(self, pos):
        """Returns the depth of the position 'pos' in the tree"""
        if self.isRoot(pos):
            return 0
        return 1 + self.depthN(self.getParent(pos))

    def heightN(self, pos):
        """Returns the height of the position 'pos' in the tree"""
        if self.isLeaf(pos):
            return 0
        return 1 + max([self.heightN(child) for child in self.getChildren(pos)])

    def height(self):
        """Returns the height of the tree"""
        return self.heightN(self.getRoot())
