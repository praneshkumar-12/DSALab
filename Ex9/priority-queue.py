import ctypes
import random


class EmptyQueueError(Exception):
    pass


class PQueue:
    def __init__(self, hp_size, lp_size):
        self.lp_btm = 0
        self.hp_btm = 0
        self.hp_top = 0
        self.lp_top = 0
        self.hp_cap = hp_size
        self.lp_cap = lp_size
        self.hp_queue = self.make_array(hp_size)
        self.lp_queue = self.make_array(lp_size)

    def make_array(self, size):
        temp = (size * ctypes.py_object)()
        return temp

    def resize(self, queue_num, size):
        if queue_num == 0:
            new_queue = self.make_array(size)
            for i in range(self.hp_top):
                new_queue[i] = self.hp_queue[i]
            self.hp_queue = new_queue
            self.hp_cap = size
        if queue_num == 1:
            new_queue = self.make_array(size)
            for i in range(self.lp_top):
                new_queue[i] = self.lp_queue[i]
            self.lp_queue = new_queue
            self.lp_cap = size

    def is_empty(self, queue_num):
        if queue_num == 0:
            if len(self.hp_queue) == 0:
                return True
            else:
                return self.check_all_dash(0)
        elif queue_num == 1:
            if len(self.lp_queue) == 0:
                return True
            else:
                return self.check_all_dash(1)

    def check_all_dash(self, queue_num):
        if queue_num == 0:
            f = False
            for i in range(self.hp_top):
                if self.hp_queue[i] == "-":
                    f = True
                else:
                    f = False
            return f
        elif queue_num == 1:
            f = False
            for i in range(self.lp_top):
                if self.lp_queue[i] == "-":
                    f = True
                else:
                    f = False
            return f

    def __len__(self):
        return len(self.hp_queue)

    def __str__(self):
        queue_as_string = "HPQ:["
        for idx in range(self.hp_top):
            queue_as_string += str(self.hp_queue[idx])
            if idx != self.hp_top - 1:
                queue_as_string += ","
        queue_as_string += "] LPQ:["
        for idx in range(self.lp_top):
            queue_as_string += str(self.lp_queue[idx])
            if idx != self.lp_top - 1:
                queue_as_string += ","
        queue_as_string += "]"
        return queue_as_string

    def peek(self, queue_num):
        if queue_num == 0:
            if self.is_empty(0):
                raise EmptyQueueError("High Priority Queue is empty!")
            return self.hp_queue[0]
        elif queue_num == 1:
            if self.is_empty(1):
                raise EmptyQueueError("High Priority Queue is empty!")
            return self.lp_queue[0]

    def enqueue(self, queue_num, elt):
        if queue_num == 0:
            if self.hp_top == self.hp_cap:
                self.resize(0, 2 * self.hp_cap)
            self.hp_queue[self.hp_top] = elt
            self.hp_top += 1
        elif queue_num == 1:
            if self.lp_top == self.lp_cap:
                self.resize(1, 2 * self.lp_cap)
            self.lp_queue[self.lp_top] = elt
            self.lp_top += 1

    def dequeue(self):
        if not self.is_empty(0):
            del_elt = self.hp_queue[self.hp_btm]
            self.hp_queue[self.hp_btm] = "-"
            self.hp_btm += 1
            return del_elt
        else:
            if self.is_empty(1):
                return
            del_elt = self.lp_queue[self.lp_btm]
            self.lp_queue[self.lp_btm] = "-"
            self.lp_btm += 1
            return del_elt


if __name__ == "__main__":
    q = PQueue(2, 2)

    times = 50

    for _ in range(times):
        queue_n = random.randint(0, 1)
        val = random.randint(0, 100)
        q.enqueue(queue_n, val)
        print(q)

    for _ in range(times):
        q.dequeue()
        print(q)
