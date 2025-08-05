from LinkedBinarytree import LinkedBinaryTree                #importing the LinkedBinaryTree class from LinkedBinaryTree file

class ExpressionTree(LinkedBinaryTree):
    """
       This class is used for creating the expressiontree,
       and it contains below methods.
    """

    def __init__(self, item=None, t_left=None, t_right=None):
        super().__init__(item, t_left, t_right)

    def construct(self, string):
        """Constructs an expression tree from a postfix expression string"""
        s = []
        for character in string:
            if character in "+-*/":
                r_child = s.pop()
                l_child = s.pop()
                s.append(ExpressionTree(character, l_child, r_child))
            else:
                s.append(ExpressionTree(character))

        self.root = s.pop().getRoot()
        return self.root

#Driver Code
if __name__ == "__main__":
    E = ExpressionTree()
    E.construct("ab-c/f*d+") 
    print(E)
