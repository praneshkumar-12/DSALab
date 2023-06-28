from AbstractBinaryTree import AbstractBinaryTree


class LinkedBinaryTree(AbstractBinaryTree):
    class BTNode:
        __slots__ = ["item", "left", "right", "parent"]

        def __init__(self, item, left=None, right=None, parent=None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent

        def getitem(self):
            return self.item

        def setitem(self, item):
            self.item = item

    __slots__ = ["root", "size"]

    def __init__(self, item=None, t_left=None, t_right=None, parent=None):
        self.root = None
        self.size = 0
        self.string = ""
        self.parent = parent
        if item is not None:
            self.root = self.addRoot(item)
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
        if self.root is not None:
            raise ValueError("Root already exists")
        else:
            self.root = self.BTNode(item)
            self.size += 1
            return self.root

    def __len__(self):
        return self.size

    def getParent(self, pos):
        return pos.parent

    def getLeft(self, pos):
        return pos.left

    def getRight(self, pos):
        return pos.right

    def getRoot(self):
        return self.root

    def getSize(self):
        return self.size

    def getNum_children(self, pos):
        if pos is None:
            return 0
        else:
            return 1 + self.getNum_children(pos.left) + self.getNum_children(pos.right)

    def addLeft(self, item, pos=None):
        if pos is None:
            pos = self.root
        if self.getLeft(pos) is not None:
            raise ValueError("Left child already exists")
        else:
            pos.left = self.BTNode(item, parent=pos)
            self.size += 1
            return pos.left

    def addRight(self, item, pos=None):
        if pos is None:
            pos = self.root
        if self.getRight(pos) is not None:
            raise ValueError("Right child already exists")
        else:
            pos.right = self.BTNode(item, parent=pos)
            self.size += 1
            return pos.right

    def preorder(self, pos):
        self.string += str(pos.item) + ","
        if pos.left is not None:
            self.preorder(pos.left)
        if pos.right is not None:
            self.preorder(pos.right)

    def postorder(self, pos):
        if pos.left is not None:
            self.preorder(pos.left)
        if pos.right is not None:
            self.preorder(pos.right)
        self.string += str(pos.item) + ","

    def inorder(self, pos):
        if pos.left is not None:
            self.preorder(pos.left)
        self.string += str(pos.item) + ","
        if pos.right is not None:
            self.preorder(pos.right)

    def __str__(self):
        self.string = "Preorder: "
        self.preorder(self.root)
        self.string += "|Inorder: "
        self.inorder(self.root)
        self.string += "|Postorder: "
        self.postorder(self.root)
        self.string += "|"
        return self.string
