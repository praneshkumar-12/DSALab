from abc import ABC
from abc import abstractmethod


class AbstractTree(ABC):
    @abstractmethod
    def getRoot(self):
        pass

    @abstractmethod
    def getParent(self, pos):
        pass

    @abstractmethod
    def getChildren(self, pos):
        pass

    @abstractmethod
    def getNumChildren(self, pos):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def isRoot(self, pos):
        return pos == self.getRoot()

    def isLeaf(self, pos):
        return self.getNumChildren(pos) == 0

    def isEmpty(self):
        return len(self) == 0

    def depthN(self, pos):
        if self.isRoot(pos):
            return 0
        else:
            return 1 + self.depthN(self.getParent(pos))

    def heightN(self, pos):
        if self.isLeaf(pos):
            return 0
        return 1 + max([self.heightN(child) for child in self.getChildren(pos)])

    def depth(self):
        return 0

    def height(self):
        return self.heightN(self.getRoot())
