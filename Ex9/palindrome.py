class EmptyStackError(Exception):
    """Exception raised when attempting to access or manipulate an empty stack."""
    pass


class EmptyQueueError(Exception):
    """Exception raised when attempting to access or manipulate an empty queue."""
    pass


class StackWrapper:
    """
    A wrapper class for a stack implementation using a Python list.
    """

    def __init__(self):
        """
        Initialize a new StackWrapper instance.
        """
        self.stack = []

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def push(self, elt):
        """
        Push an element onto the top of the stack.

        Args:
            elt: The element to be pushed onto the stack.
        """
        self.stack.append(elt)

    def pop(self):
        """
        Remove and return the element from the top of the stack.

        Returns:
            The element removed from the top of the stack.
        """
        if self.is_empty():
            raise EmptyStackError("Stack is empty!")
        return self.stack.pop()

    def __len__(self):
        """
        Return the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)

    def __str__(self):
        """
        Return a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return f"S:{str(self.stack)}"

    def top_element(self):
        """
        Return the element at the top of the stack without removing it.

        Returns:
            The element at the top of the stack.
        """
        if self.is_empty():
            raise EmptyStackError("Stack is empty!")
        return self.stack[-1]


class QueueWrapper:
    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, value):
        """Add an item to the end of the queue.

        Args:
            value: The item to be added to the queue.
        """
        self.queue.append(value)

    def dequeue(self):
        """Remove and return the item at the front of the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            EmptyQueueError: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueError("Queue is empty!")
        return self.queue.pop(0)

    def is_empty(self):
        """Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def __len__(self):
        """Return the number of items in the queue.

        Returns:
            The number of items in the queue.
        """
        return len(self.queue)

    def __str__(self):
        """Return a string representation of the queue.

        Returns:
            A string representation of the queue.
        """
        return f"Q:{str(self.queue)}"

    def peek(self):
        """Return the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            EmptyQueueError: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueError("Queue is empty!")
        return self.queue[0]
