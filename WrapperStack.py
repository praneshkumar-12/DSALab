import ctypes


class EmptyStackError(Exception):
    """
    Exception raised when attempting to perform an operation on an empty stack.
    """

    pass


class WrapperStack:
    """
    A stack implementation using a list.
    """

    def __init__(self):
        """
        Initializes a new instance of the Stack class.
        """
        self.stack = []  # Internal list to store the elements

    def push(self, elt):
        """
        Pushes an element onto the top of the stack.

        Args:
            elt: The element to be pushed.
        """
        self.stack.append(elt)

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

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
        del_item = self.stack.pop()
        return del_item

    def __len__(self):
        """
        Returns the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)

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
        return self.stack[-1]

    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        string = "<"
        for i in self.stack:
            string += str(i) + ","
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
        if idx >= len(self.stack):
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
        if idx >= len(self.stack):
            raise IndexError("Index out of bound")
        self.stack[idx] = elt
