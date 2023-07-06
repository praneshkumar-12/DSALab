class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedStack:
    def __init__(self):
        self.top = Node()
        self.size = 0

    def is_empty(self):
        return self.top.next is None

    def top_element(self):
        return self.top.item

    def push(self, item):
        temp = Node(item)
        temp.next = self.top.next
        self.top.next = temp
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")

        delnode = self.top.next
        self.top.next = delnode.next
        self.size -= 1
        return delnode.item

    def __str__(self):
        string = "<"
        pos = self.top
        while pos is not None:
            if pos.item is not None:
                string += str(pos.item) + ","
            pos = pos.next
        return string + ">"

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        pos = self.top.next
        for _ in range(idx):
            try:
                pos = pos.next
            except AttributeError:
                raise IndexError("Index out of range")
        if pos is None:
            raise IndexError("Index out of range")
        return pos.item


sls = SinglyLinkedStack()
sls.push(10)
sls.push(20)
sls.push(30)
print(sls)
print(sls[0])
print(sls[1])
print(sls[2])

print(sls.pop())
print(sls)
print(sls.pop())
print(sls)
print(sls.pop())
