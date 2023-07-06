class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class LinkedCircularQueue:
    def __init__(self):
        self.front = self.rear = Node()
        self.front.next = self.front
        self.size = 0

    def is_empty(self):
        return self.front.next == self.front

    def enqueue(self, item):
        temp = Node(item, self.rear.next)
        self.rear.next = temp
        self.rear = temp
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        else:
            delnode = self.front.next
            self.front.next = delnode.next
            self.size -= 1
            return delnode.item

    def __str__(self):
        string = "<"
        pos = self.front.next
        while pos is not self.front:
            string += str(pos.item) + ","
            pos = pos.next
        return string + ">"


lcq = LinkedCircularQueue()
lcq.enqueue(5)
lcq.enqueue(10)
lcq.enqueue(15)

print(lcq)
print(lcq.dequeue())
print(lcq)
print(lcq.dequeue())
print(lcq)
print(lcq.dequeue())
print(lcq)
print(lcq.dequeue())
