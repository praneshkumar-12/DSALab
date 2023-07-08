from LinkedBinaryTree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, item=None, t_left=None, t_right=None):
        super().__init__(item, t_left, t_right)
    
    def insert(self, item, pos=None):
        if pos is None:
            if self.isEmpty():
                self.addRoot(item)
                return None
            else:
                pos = self.getRoot()
        
        if item < pos.item:
            if self.left(pos) is None:
                self.addLeft(item, pos)
            else:
                return self.insert(item, pos.left)
        
        if item > pos.item:
            if self.right(pos) is None:
                self.addRight(item, pos)
            else:
                return self.insert(item , pos.right)
        
        if item == pos.item:
            return None
        
    def search(self, item, pos=None):
        if pos == None:
            pos = self.getRoot()
        if pos.item == item:
            return pos
        elif item < pos.item and pos.left is not None:
            return self.search(item, pos.left)
        elif item > pos.item and pos.right is not None:
            return self.search(item, pos.right)
    
    def findmin(self, pos=None):
        if pos is None:
            pos = self.root
        if pos.left is not None:
            return self.findmin(pos.left)
        if pos.left is None:
            return pos
    
    def findmax(self, pos=None):
        if pos is None:
            pos = self.root
        if pos.right is not None:
            return self.findmax(pos.right)
        if pos.right is None:
            return pos
        
    def delete(self, ele, pos=None):
        if pos == None:
            pos = self.getRoot()

        if ele < pos.item:
            self.delete(ele, self.left(pos))
        elif ele > pos.item:
            self.delete(ele, self.right(pos))
        else:
            if self.isLeaf(pos):  # no child
                if pos == self.getRoot():
                    self.root = None
                else:
                    parent = self.getParent(pos)
                    if self.left(parent) == pos:
                        parent.left = None
                    else:
                        parent.right = None
            elif self.left(pos) is None or self.right(pos) is None: # one child
                if self.left(pos) is None:
                    child = self.right(pos)
                else:
                    child = self.left(pos)
                if pos == self.getRoot():
                    self.root = child
                else:
                    parent = self.getParent(pos)
                    if self.left(parent) == pos:
                        parent.left = child
                    else:
                        parent.right = child
            else:  
                min_node = self.findmin(pos.right)
                pos.item = min_node.item
                self.delete(min_node.item, pos.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(38)
    bst.insert(90)
    bst.insert(75)
    bst.insert(42)
    bst.insert(77)
    bst.insert(88)
    bst.insert(44)
    bst.insert(87)
    bst.insert(12)
    bst.insert(41)
    print(bst)
    bst.delete(38)
    print(bst)
    
    bst.delete(88)
    print(bst)
    
    bst.delete(90)
    print(bst)

    print(bst.findmax().item)
    print(bst.findmin().item)