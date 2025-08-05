from LinkedBinarytree import LinkedBinaryTree


class AVLnode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.pos = None
    
    def insert(self, item):
        self.pos = self._insert(self.pos, item)
    
    def _insert(self, pos, item):
        if pos is None:
            return AVLnode(item)
        elif item < pos.item:
            pos.left = self._insert(pos.left, item)
        else:
            pos.right = self._insert(pos.right, item)
        
        pos.height = 1 + max(self._get_height(pos.left), self._get_height(pos.right))
        balance_factor = self._get_balance_factor(pos)
        
        if balance_factor > 1:  # Left subtree is heavier
            if item < pos.left.item:
                return self._rotate_right(pos)
            else:
                pos.left = self._rotate_left(pos.left)
                return self._rotate_right(pos)
        if balance_factor < -1:  # Right subtree is heavier
            if item > pos.right.item:
                return self._rotate_left(pos)
            else:
                pos.right = self._rotate_right(pos.right)
                return self._rotate_left(pos)
        
        return pos
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def display(self):
        self._display(self.pos)
    
    def _display(self, pos):
        if pos is not None:
            self._display(pos.left)
            print(pos.item, end=' ')
            self._display(pos.right)


#Driver Code
avl_tree = AVLTree()
print("Inserting the Elements")
avl_tree.insert(90)
avl_tree.insert(80)
avl_tree.insert(70)
avl_tree.insert(60)
avl_tree.insert(50)
avl_tree.insert(45)
avl_tree.display()
