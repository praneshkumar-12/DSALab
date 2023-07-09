import ctypes


class EmptyCircularQueue(Exception):
    pass


class FullCircularQueue(Exception):
    pass


class CircularQueue:
    def __init__(self, size):
        """
        Initializes a CircularQueue object with the given size.

        Args:
            size (int): The maximum number of elements the circular queue can hold.
        """
        self.cap = size
        self.front = self.rear = 0
        self.circular_queue = self.make_array(size)

    def make_array(self, size):
        """
        Creates and returns a new array with the given size using ctypes.

        Args:
            size (int): The size of the array to be created.

        Returns:
            array: A new array with the given size.
        """
        return (size * ctypes.py_object)()

    def next(self, pos):
        """
        Returns the next position in the circular queue.

        Args:
            pos (int): The current position.

        Returns:
            int: The next position in the circular queue.
        """
        return (pos + 1) % self.cap

    def is_empty(self):
        """
        Checks if the circular queue is empty.

        Returns:
            bool: True if the circular queue is empty, False otherwise.
        """
        return self.front == self.rear

    def is_full(self):
        """
        Checks if the circular queue is full.

        Returns:
            bool: True if the circular queue is full, False otherwise.
        """
        return self.next(self.rear) == self.front

    def enqueue(self, elt):
        """
        Adds an element to the rear of the circular queue.

        Args:
            elt (object): The element to be added to the circular queue.

        Raises:
            FullCircularQueue: If the circular queue is full.
        """
        if self.is_full():
            raise FullCircularQueue("Circular Queue is full")
        else:
            self.circular_queue[self.rear] = elt
            self.rear = self.next(self.rear)

    def dequeue(self):
        """
        Removes and returns the element from the front of the circular queue.

        Returns:
            object: The element removed from the front of the circular queue.

        Raises:
            EmptyCircularQueue: If the circular queue is empty.
        """
        if self.is_empty():
            raise EmptyCircularQueue("Circular Queue is empty")
        else:
            del_item = self.circular_queue[self.front]
            self.front = self.next(self.front)
            return del_item

    def __str__(self):
        """
        Returns a string representation of the circular queue.

        Returns:
            str: A string representation of the circular queue.
        """
        string = "<"
        idx = self.front
        while (
            idx != self.next(self.rear) - 1
            and self.front != self.rear
            and idx != self.rear
        ):
            string += str(self.circular_queue[idx]) + ","
            if idx >= self.cap - 1:
                idx = 0
            else:
                idx += 1
        return string + ">"

    def __len__(self):
        """
        Returns the number of elements in the circular queue.

        Returns:
            int: The number of elements in the circular queue.
        """
        count = 0
        idx = self.front
        while (
            idx != self.next(self.rear) - 1
            and self.front != self.rear
            and idx != self.rear
        ):
            count += 1
            if idx >= self.cap - 1:
                idx = 0
            else:
                idx += 1
        return count

    def find(self, elt):
        """
        Searches for the given element in the circular queue and returns its index.

        Args:
            elt (object): The element to be searched in the circular queue.

        Returns:
            int: The index of the element if found, -1 otherwise.
        """
        idx = self.front
        while (
            idx != self.next(self.rear) - 1
            and self.front != self.rear
            and idx != self.rear
        ):
            if self.circular_queue[idx] == elt:
                return idx
            if idx >= self.cap - 1:
                idx = 0
            else:
                idx += 1
        return -1

    def peek(self):
        """
        Returns the element at the front of the circular queue without removing it.

        Returns:
            object: The element at the front of the circular queue.

        Raises:
            EmptyCircularQueue: If the circular queue is empty.
        """
        if self.is_empty():
            raise EmptyCircularQueue("Circular Queue is empty")
        else:
            return self.circular_queue[self.front]