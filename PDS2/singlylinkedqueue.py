class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        delnode = self.front
        self.front = delnode.next
        self.size -= 1

        if self.front == None:
            self.rear = None

        return delnode.item

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.front.item

    def __len__(self):
        return self.size

    def __str__(self):
        pos = self.front
        string = "<"
        while pos is not None:
            string += str(pos.item) + ","
            pos = pos.next

        return string + ">"

    def __getitem__(self, idx):
        pos = self.front
        for _ in range(idx):
            try:
                pos = pos.next
            except AttributeError:
                raise IndexError("Index out of range")
        if pos is None:
            raise IndexError("Index out of range")
        return pos.item


slq = SinglyLinkedQueue()
slq.enqueue(10)
print(slq)
slq.enqueue(20)
print(slq)
slq.enqueue(30)
print(slq)
slq.enqueue(40)
print(slq)
slq.enqueue(50)
print(slq)
print(slq[0])
print(slq[1])
print(slq[2])
print(slq[3])
print(slq[4])
print(slq[6])
slq.dequeue()
print(slq)
slq.dequeue()
print(slq)
slq.dequeue()
print(slq)
slq.dequeue()
print(slq)
