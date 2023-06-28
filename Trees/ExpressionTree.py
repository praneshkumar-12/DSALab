from LinkedBinaryTree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, item=None, t_left=None, t_right=None):
        super().__init__(item, t_left, t_right)

    def construct(self, string):
        """
        Constructs an expression tree from a postfix expression string.

        Args:
            string: A string representing a postfix expression.

        Returns:
            The root position of the constructed expression tree.
        """
        s = []
        for ch in string:
            if ch in "+-*/":
                r_child = s.pop()
                l_child = s.pop()
                s.append(ExpressionTree(ch, l_child, r_child))
            else:
                s.append(ExpressionTree(ch))

        self.root = s.pop().getRoot()
        return self.root


if __name__ == "__main__":
    E = ExpressionTree()
    E.construct("ab-c/f*d+")  # ab+a*cd-e+/afg-*h+-
    print(E)
