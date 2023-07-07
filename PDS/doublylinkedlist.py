class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0

    def is_empty(self):
        return self.head == self.tail

    def append(self, item):
        temp = Node(item)

        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.size += 1

    def __str__(self):
        string = "<"
        pos = self.head.next
        while pos is not None:
            string += str(pos.item) + ","
            pos = pos.next
        return string + ">"

    def insert(self, idx, item):
        pos = self.head
        for _ in range(idx):
            try:
                pos = pos.next
            except AttributeError:
                raise IndexError("Index out of range!")
        if pos is None:
            raise IndexError("Index out of range")
        temp = Node(item)
        temp.next = pos.next
        temp.prev = pos
        pos.next = temp
        self.size += 1

    def find(self, item):
        pos = self.head.next
        count = 0
        while pos is not None:
            if pos.item == item:
                count += 1
                return count
            count += 1
        return -1

    def search(self, item):
        pos = self.head.next
        while pos is not None:
            if pos.item == item:
                return True
        return False

    def count(self, item):
        pos = self.head.next
        count = 0
        while pos is not None:
            if pos.item == item:
                count += 1
        return count

    def find_prev(self, item):
        pos = self.head
        while pos.next is not None:
            if pos.next.item == item:
                return pos
            pos = pos.next
        return pos

    def remove(self, item):
        prev = self.find_prev(item)
        delnode = prev.next

        if delnode is None:
            raise ValueError("No such item in list")
        else:
            if delnode.next is not None:
                delnode.next.prev = prev
            if delnode.next is None:
                self.tail = prev
            prev.next = delnode.next
            self.size -= 1

    def delete(self, idx):
        pos = self.head
        for _ in range(idx):
            try:
                pos = pos.next
            except AttributeError:
                raise IndexError("Index out of range")
        if pos is None:
            raise IndexError("Index out of range")
        delnode = pos.next
        if delnode.next is not None:
            delnode.next.prev = pos
        if delnode.next is None:
            self.tail = delnode
        pos.next = delnode.next
        self.size -= 1

    def __len__(self):
        return self.size

    def reverse_traversal(self):
        string = "<"
        pos = self.tail
        while pos.prev is not None:
            string += str(pos.item) + ","
            pos = pos.prev
        return string + ">"


dll = DoublyLinkedList()
dll.append(5)
dll.append(10)
dll.append(15)
dll.insert(2, 20)
print(dll)
dll.remove(15)
print(dll)
print(dll.reverse_traversal())
