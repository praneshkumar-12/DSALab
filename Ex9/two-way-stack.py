import ctypes


class StackFullError(Exception):
    pass


class TwoWayStack:
    def __init__(self, size):
        self.cap = size
        self.stack = self.make_array(size)
        self.top1 = 0
        self.top2 = size - 1

    def make_array(self, size):
        temp = (size * ctypes.py_object)()
        return temp

    def push(self, stack_num, item):
        if self.is_full():
            raise StackFullError("Stack is full!")

        if stack_num == 0:
            self.stack[self.top1] = item
            self.top1 += 1
        elif stack_num == 1:
            self.stack[self.top2] = item
            self.top2 -= 1

    def pop(self, stack_num):
        if stack_num == 0:
            del_item = self.stack[self.top1]
            self.stack[self.top1] = "-"
            self.top1 -= 1
            return del_item
        if stack_num == 1:
            del_item = self.stack[self.top2]
            self.stack[self.top2] = "-"
            self.top2 += 1
            return del_item

    def is_full(self):
        return self.top1 > self.top2

    def __getitem__(self, idx):
        if idx > self.top2:
            raise IndexError("Index out of range!")
        return self.stack[idx]

    def __setitem__(self, key, value):
        ...

    def is_empty(self, stack_num):
        if stack_num == 0:
            return self.top1 == -1
        if stack_num == 1:
            return self.top2 == self.cap

    def __str__(self):
        string = "2WS:["
        for idx in range(self.cap):
            try:
                string += str(self.stack[idx])
            except ValueError:
                string += "-"
                continue
            finally:
                if not idx == self.cap - 1:
                    string += ","
        string += "]"
        return string


tws = TwoWayStack(10)
import random

for _ in range(10):
    stack_n = random.randint(0, 1)
    num = random.randint(0, 100)
    tws.push(stack_n, num)
    print(tws)

while True:
    stack_n = random.randint(0, 1)
    if tws.is_empty(stack_n):
        continue
    tws.pop(stack_n)
    print(tws)
    if tws.is_empty(0) and tws.is_empty(1):
        break
