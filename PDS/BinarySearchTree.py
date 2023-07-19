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
        
    def delete(self, item, position=None):
        # If position is not provided, start the search from the root
        if position is None:
            position = self.root

        # Search for the position of the item to be deleted
        pos = self.search(item, position)
        if pos is None:
            raise ValueError("No such element in Tree")

        parent = pos.parent

        if pos.left is None and pos.right is None:
            # Case 1: Deleting a leaf node
            if parent is None:
                # If the node is the root and has no children
                self.root = None
            elif parent.left == pos:
                # If the node is the left child of its parent
                parent.left = None
            else:
                # If the node is the right child of its parent
                parent.right = None
        elif pos.left is not None and pos.right is None:
            # Case 2: Deleting a node with only a left child
            if parent is None:
                # If the node is the root and has only a left child
                self.root = pos.left
                self.root.parent = None
            elif parent.left == pos:
                # If the node is the left child of its parent
                parent.left = pos.left
                pos.left.parent = parent
            else:
                # If the node is the right child of its parent
                parent.right = pos.left
                pos.left.parent = parent
        elif pos.left is None and pos.right is not None:
            # Case 3: Deleting a node with only a right child
            if parent is None:
                # If the node is the root and has only a right child
                self.root = pos.right
                self.root.parent = None
            elif parent.left == pos:
                # If the node is the left child of its parent
                parent.left = pos.right
                pos.right.parent = parent
            else:
                # If the node is the right child of its parent
                parent.right = pos.right
                pos.right.parent = parent
        else:
            # Case 4: Deleting a node with both left and right children
            smallest_node = self.findmin(pos.right)  # Find the smallest node in the right subtree
            pos.item = smallest_node.item  # Replace the item of the node to be deleted with the smallest node's item
            self.delete(smallest_node.item, pos.right)  # Delete the smallest node recursively

        self.size -= 1  # Update the size of the tree

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
