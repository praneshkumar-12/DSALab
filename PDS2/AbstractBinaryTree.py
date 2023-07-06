from AbstractTree import AbstractTree
from abc import abstractmethod


class AbstractBinaryTree(AbstractTree):
    @abstractmethod
    def left(self, pos):
        pass

    @abstractmethod
    def right(self, pos):
        pass

    def getChildren(self, pos):
        if pos is None:
            return None
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)

    def sibling(self, pos):
        parent = self.getParent(pos)

        if parent is None:
            return None
        if pos == self.right(parent):
            return self.left(parent)
        else:
            return self.right(parent)
