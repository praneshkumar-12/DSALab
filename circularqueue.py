import ctypes

class EmptyCircularQueueError(Exception):
    pass

class FullCircularQueueError(Exception):
    pass
class CircularQueue:
    def __init__(self, cap):
        self.cap = cap
        self.queue = self.make_array(cap)
        self.front = self.rear = 0

    def make_array(self, size):
        return (size * ctypes.py_object)()

    def next(self, pos):
        return (pos + 1) % self.cap

    def is_empty(self):
        return self.front ==  self.rear

    def is_full(self):
        return self.front == self.next(self.rear)

    def enqueue(self, elt):
        if self.is_full():
            raise FullCircularQueueError("Circular Queue is full!")
        else:
            self.queue[self.rear] = elt
            self.rear = self.next(self.rear)

    def dequeue(self):
        if self.is_empty():
            raise EmptyCircularQueueError("Circular Queue is empty!")
        else:
            del_item = self.queue[self.front]
            self.front = self.next(self.front)

    def __str__(self):
        # return str(self.queue)
        circular_queue_as_string = "CQ:["
        # for i in self.queue._objectsvalue:
        #     circular_queue_as_string += str(i) + ","
        # return circular_queue_as_string + "]"

        for idx in range(self.front, self.rear):
            circular_queue_as_string += str(self.queue._objects[str(idx)]) + ","
        return circular_queue_as_string + "]"

cq = CircularQueue(5)
cq.enqueue(5)
cq.enqueue(10)
cq.enqueue(15)
cq.enqueue(20)
print(cq)
cq.dequeue()
print(cq)
cq.dequeue()
print(cq)
cq.enqueue(25)
print(cq)
cq.enqueue(30)
print(cq)
