from AbstractBinaryTree import AbstractBinaryTree


class LinkedBinaryTree(AbstractBinaryTree):
    class BTNode:
        def __init__(self, item, left=None, right=None, parent=None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self, item=None, t_left=None, t_right=None):
        self.root = None
        self.size = 0
        self.res = ""

        if item is None and (t_left is not None or t_right is not None):
            raise ValueError("Cannot create tree without a root")
        if item is not None:
            self.addRoot(item)
        if t_left is not None:
            if t_left.root is not None:
                t_left.root.parent = self.root
                self.root.left = t_left.root
                self.size += t_left.size
                t_left.root = None
        if t_right is not None:
            if t_right.root is not None:
                t_right.root.parent = self.root
                self.root.right = t_right.root
                self.size += t_right.size
                t_right.root = None

    def addRoot(self, item):
        if self.getRoot() is not None:
            raise ValueError("Root is already present")
        else:
            self.root = self.BTNode(item=item)
            self.size += 1
            return self.root

    def __len__(self):
        return self.size

    def getParent(self, pos):
        return pos.parent

    def getRoot(self):
        return self.root

    def left(self, pos):
        return pos.left

    def right(self, pos):
        return pos.right

    def getNumChildren(self, pos):
        return len(list(self.getChildren(pos)))

    def addLeft(self, item, pos):
        if self.left(pos) is not None:
            raise ValueError("Left child already exists!")
        else:
            pos.left = self.BTNode(item, parent=pos)
            self.size += 1
            return pos.left

    def addRight(self, item, pos):
        if self.right(pos) is not None:
            raise ValueError("Right child already exists!")
        else:
            pos.right = self.BTNode(item, parent=pos)
            self.size += 1
            return pos.right

    def preorder(self, pos):
        self.res += str(pos.item) + " "
        if self.left(pos) is not None:
            self.preorder(pos.left)
        if self.right(pos) is not None:
            self.preorder(pos.right)

    def inorder(self, pos):
        if self.left(pos) is not None:
            self.inorder(pos.left)
        self.res += str(pos.item) + " "
        if self.right(pos) is not None:
            self.inorder(pos.right)

    def postorder(self, pos):
        if self.left(pos) is not None:
            self.postorder(pos.left)
        if self.right(pos) is not None:
            self.postorder(pos.right)
        self.res += str(pos.item) + " "

    def __str__(self):
        self.res = ""
        self.preorder(self.root)
        return self.res
