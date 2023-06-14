class ElementNotFoundError(Exception):
    pass
class Node:
    __slots__ = ["item", "next"]
    def __init__(self, elt = None, next = None):
        self.item = elt
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0

    def is_empty(self):
        return self.head == self.tail

    def append(self, elt):
        temp = Node(elt)
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def __str__(self):
        string = '<'
        pos = self.head.next
        while pos is not None:
            string += str(pos.item) + ","
            pos = pos.next
        return string + ">"

    def find(self, elt):
        pos = self.head
        count = 0
        while pos is not None:
            count += 1
            if pos.item == elt:
                return count - 1
            pos = pos.next
        return -1

    def insert(self, idx, elt):
        pos = self.head
        for i in range(idx):
            pos = pos.next
        temp = Node(elt, pos.next)
        pos.next = temp
        self.size += 1

    def find_prev(self, elt):
        pos = self.head
        while pos.next is not None:
            if pos.next.item == elt:
                return pos
            pos = pos.next

        return pos

    def remove(self, elt):
        prev = self.find_prev(elt)
        delnode = prev.next

        if delnode is None:
            raise ElementNotFoundError("Element is not in list!")
        prev.next = delnode.next
            
        self.size -= 1
        
    def __len__(self):
        return self.size
