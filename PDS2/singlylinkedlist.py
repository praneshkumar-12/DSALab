class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0

    def is_empty(self):
        return self.head == self.tail

    def append(self, item):
        temp = Node(item)
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def __str__(self):
        string = "<"
        pos = self.head.next
        while pos is not None:
            string += str(pos.item) + ","
            pos = pos.next
        return string + ">"

    def find(self, item):
        pos = self.head.next
        count = 0
        while pos is not None:
            if pos.item == item:
                count += 1
                return count
            else:
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

    def insert(self, idx, item):
        pos = self.head
        for _ in range(idx):
            try:
                pos = pos.next
            except AttributeError:
                raise IndexError("Index out of range")
        if pos is None:
            raise IndexError("Index out of range")
        temp = Node(item, pos.next)
        pos.next = temp
        self.size += 1

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
            raise ValueError("No such value in list")
        else:
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
        pos.next = delnode.next
        self.size -= 1

    def __len__(self):
        return self.size


if __name__ == "__main__":
    sll = SinglyLinkedList()
    print(sll)
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.append(50)
    print(sll)
    sll.insert(3, 40)
    print(sll)
    sll.remove(50)
    print(sll)
    sll.delete(3)
    print(sll)
