import ctypes


class EmptyQueueError(Exception):
    """
    Exception raised when attempting to perform an operation on an empty queue.
    """

    pass

class FullQueueError(Exception):
    """
    Exception raised when attempting to perform an operation on a full queue.
    """

    pass

class CompactQueue:
    """
    A compact queue implementation using a dynamic array.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Queue class with a specified initial capacity.

        Args:
            size (int): The initial capacity of the queue.
        """
        self.cap = size  # Capacity of the queue
        self.rear = 0  # Index of the next available position in the queue
        self.queue = self.make_array(self.cap)  # Internal array to store the elements

    def make_array(self, size):
        """
        Creates a new dynamic array with the specified size.

        Args:
            size (int): The size of the array.

        Returns:
            A dynamic array with the specified size.
        """
        return (size * ctypes.py_object)()


    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.rear == 0

    def __len__(self):
        """
        Returns the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return self.rear

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            str: A string representation of the queue.
        """
        string = "<"
        for i in range(self.rear):
            string += str(self.queue[i]) + ","
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
        if self.rear == self.cap:
            raise FullQueueError("Queue is full, delete some elements to enqueue")
        self.queue[self.rear] = elt
        self.rear += 1

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
        del_elt = self.queue[0]
        for i in range(self.rear - 1):
            self.queue[i] = self.queue[i + 1]
        self.rear -= 1

        return del_elt
