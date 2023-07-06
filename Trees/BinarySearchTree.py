from LinkedBinaryTree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, item=None, t_left=None, t_right=None):
        super().__init__(item, t_left, t_right)

    def insert(self, item, pos=None):
        if pos is None:
            if self.root is None:
                self.addRoot(item)
                return None
            else:
                pos = self.root
        if item < pos.item:
            if pos.left is None:
                pos.left = self.addLeft(item, pos)
            else:
                return self.insert(item, pos.left)
        elif item > pos.item:
            if pos.right is None:
                pos.right = self.addRight(item, pos)
            else:
                return self.insert(item, pos.right)
        elif item == pos.item:
            return None

    def search(self,item, pos=None):
        if pos is None:
            pos = self.root
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

    def delete(self, item):
        pos = self.search(item)
        if pos is None:
            raise ValueError("No such element in Tree")
        
        parent = pos.parent

        if pos.left is None and pos.right is None:
            if parent.left == pos:
                parent.left = None
                self.size -= 1
            if parent.right == pos:
                parent.right = None
                self.size -= 1
        elif pos.left is not None and pos.right is None:
            parent.left = pos.left
            self.size -= 1
            del pos
        elif pos.left is None and pos.right is not None:
            parent.right = pos.right
            self.size -= 1
            pos.left = pos.right = pos.item = None
        else:
            smallest_node = self.findmin(pos.right)
            pos.item = smallest_node.item
            smallest_node.item = 100000
            self.delete(smallest_node.item)
            

if __name__ == "__main__":
    import random
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
    bst.string = ""
    bst.inorder(bst.root)
    print(bst.string)
    print(bst.findmax().item)
    print(bst.findmin().item)
    bst.delete(88)
    
    print(bst)
    bst.string = ""
    bst.inorder(bst.root)
    print(bst.string)