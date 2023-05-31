import ctypes
import random


class EmptyQueueError(Exception):
    pass


class PQueue:
    def __init__(self, hp_size, lp_size):
        """
        Initialize a PQueue object with separate arrays for high priority and low priority queues.

        Args:
            hp_size (int): Size of the high priority queue.
            lp_size (int): Size of the low priority queue.
        """
        self.lp_btm = 0
        self.hp_btm = 0
        self.hp_top = 0
        self.lp_top = 0
        self.hp_cap = hp_size
        self.lp_cap = lp_size
        self.hp_queue = self.make_array(hp_size)
        self.lp_queue = self.make_array(lp_size)

    def make_array(self, size):
        """
        Create and return a new array of the specified size.

        Args:
            size (int): Size of the array.

        Returns:
            ctypes.Array: A new array of the specified size.
        """
        temp = (size * ctypes.py_object)()
        return temp

    def resize(self, queue_num, size):
        """
        Resize the specified queue to the given size.

        Args:
            queue_num (int): Queue number (0 for high priority, 1 for low priority).
            size (int): New size of the queue.
        """
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
        """
        Check if the specified queue is empty.

        Args:
            queue_num (int): Queue number (0 for high priority, 1 for low priority).

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
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
        """
        Check if all elements in the specified queue are dashes ("-").

        Args:
            queue_num (int): Queue number (0 for high priority, 1 for low priority).

        Returns:
            bool: True if all elements in the queue are dashes, False otherwise.
        """
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
        """
        Return the total number of elements in the PQueue.

        Returns:
            int: Total number of elements in the PQueue.
        """
        return len(self.hp_queue)

    def __str__(self):
        """
        Return a string representation of the PQueue.

        Returns:
            str: String representation of the PQueue.
        """
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
        """
        Return the element at the front of the specified queue without removing it.

        Args:
            queue_num (int): Queue number (0 for high priority, 1 for low priority).

        Returns:
            object: The element at the front of the queue.

        Raises:
            EmptyQueueError: If the specified queue is empty.
        """
        if queue_num == 0:
            if self.is_empty(0):
                raise EmptyQueueError("High Priority Queue is empty!")
            return self.hp_queue[0]
        elif queue_num == 1:
            if self.is_empty(1):
                raise EmptyQueueError("Low Priority Queue is empty!")
            return self.lp_queue[0]

    def enqueue(self, queue_num, elt):
        """
        Enqueue the element to the specified queue.

        Args:
            queue_num (int): Queue number (0 for high priority, 1 for low priority).
            elt (object): Element to be enqueued.
        """
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
        """
        Dequeue and return the element from the high priority queue.
        If the high priority queue is empty, dequeue from the low priority queue.

        Returns:
            object: The dequeued element.

        Raises:
            EmptyQueueError: If both high priority and low priority queues are empty.
        """
        if not self.is_empty(0):
            del_elt = self.hp_queue[self.hp_btm]
            self.hp_queue[self.hp_btm] = "-"
            self.hp_btm += 1
            return del_elt
        else:
            if self.is_empty(1):
                raise EmptyQueueError("Both High Priority and Low Priority Queues are empty!")
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
