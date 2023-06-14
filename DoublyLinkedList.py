from SinglyLinkedList import Node

class ElementNotFoundError(Exception):
    pass


class DNode(Node):
    __slots__ = ["item", "next", "prev"]

    def __init__(self, elt=None, next=None, prev=None):
        """
        Initializes a Node object with the given element and reference to the next node.

        Args:
            elt (object): The element to be stored in the node. Default is None.
            next (Node): Reference to the next node. Default is None.
            prev (Node): Reference to the previous node. Default is None.
        """
        super().__init__(elt, next)
        self.prev = prev


class ElementNotFoundError(Exception):
    pass


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0

    def is_empty(self):
        return self.head == self.tail

    def append(self, elt):
        temp = DNode(elt)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.size += 1

    def __str__(self):
        string = '<'
        pos = self.head.next
        while pos is not None:
            string += str(pos.item) + ","
            pos = pos.next
        return string + "]"

    def find(self, elt):
        pos = self.head.next
        count = 0
        while pos is not None:
            count += 1
            if pos.item == elt:
                return count - 1
            pos = pos.next
        return -1

    def insert(self, idx, elt):
        pos = self.head.next
        for i in range(idx - 1):
            pos = pos.next
        temp = Node(elt, pos.next)
        pos.next = temp
        self.size += 1

    def find_prev(self, elt):
        pos = self.head.next
        while pos.next is not None:
            if pos.next.item == elt:
                return pos
            pos = pos.next

        return pos

    def remove(self, elt):
        prev = self.find_prev(elt)
        delnode = prev.next
        try:
            prev.next = delnode.next
        except AttributeError:
            raise ElementNotFoundError("Element is not in list!")
        self.size -= 1
        
    def __len__(self):
        return self.size
    
    def reverse_display(self):
        pos = self.tail
        while pos.prev is not None:
            print(pos.item)
            pos = pos.prev
