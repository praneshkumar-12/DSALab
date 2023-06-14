import ctypes


class EmptyStackError(Exception):
    """
    Exception raised when attempting to perform an operation on an empty stack.
    """

    pass

class FullStackError(Exception):
    """
    Exception raised when attempting to perform an operation on a full stack.
    """

    pass


class CompactStack:
    """
    A compact stack implementation using a dynamic array.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Stack class.

        Args:
            size (int): The initial capacity of the stack.
        """
        self.cap = size  # Current capacity of the stack
        self.top = 0  # Index of the top element
        self.stack = self.make_array(size)  # Internal array to store the elements

    def make_array(self, size):
        """
        Creates a new array of a given size using the ctypes module.

        Args:
            size (int): The size of the array.

        Returns:
            A ctypes array of the specified size.
        """
        return (size * ctypes.py_object)()


    def push(self, elt):
        """
        Pushes an element onto the top of the stack. If the stack is full, it doubles the capacity.

        Args:
            elt: The element to be pushed.
        """
        if self.top == self.cap:
            raise FullStackError("Stack is full, delete some elements to push")
        self.stack[self.top] = elt
        self.top += 1

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.top == 0

    def pop(self):
        """
        Removes and returns the top element from the stack. If the stack is empty, raises an EmptyStackError.

        Returns:
            The top element of the stack.

        Raises:
            EmptyStackError: If the stack is empty.
        """
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        del_item = self.stack[self.top - 1]
        self.stack[self.top - 1] = None
        self.top -= 1

    def __len__(self):
        """
        Returns the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return self.top

    def top_element(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
            The top element of the stack.

        Raises:
            EmptyStackError: If the stack is empty.
        """
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.stack[self.top - 1]

    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        string = "<"
        for i in range(self.top):
            string += str(self.stack[i]) + ","
        return string + ">"

    def __getitem__(self, idx):
        """
        Returns the element at the specified index.

        Args:
            idx (int): The index of the element to retrieve.

        Returns:
            The element at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if idx >= self.top:
            raise IndexError("Index out of bound")
        return self.stack[idx]

    def __setitem__(self, idx, elt):
        """
        Sets the element at the specified index to a new value.

        Args:
            idx (int): The index of the element to set.
            elt: The new value to assign to the element.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if idx >= self.top:
            raise IndexError("Index out of bound")
        self.stack[idx] = elt
