import ctypes

class EmptyQueueError(Exception):
    pass

class WrapperQueue:
    """
    A compact queue implementation using a dynamic array.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Queue class with a specified initial capacity.

        Args:
            size (int): The initial capacity of the queue.
        """
        self.queue = []

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def __len__(self):
        """
        Returns the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self.queue)

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            str: A string representation of the queue.
        """
        string = "<"
        for i in self.queue:
            string += str(i) + ","
        return string + ">"

    def peek(self):
        """
        Returns the element at the front of the queue without removing it. If the queue is empty, raises an EmptyQueueError.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueError: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.queue[0]

    def enqueue(self, elt):
        """
        Adds an element to the rear of the queue.

        Args:
            elt: The element to be added to the queue.
        """
        self.queue.append(elt)

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue. If the queue is empty, raises an EmptyQueueError.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueError: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        del_elt = self.queue.pop(0)
        return del_elt
