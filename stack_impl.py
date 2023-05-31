import ctypes

class EmptyStackError(Exception):
    """Exception raised when attempting to perform an operation on an empty stack."""
    pass


class Stack:
    """A stack data structure implementation."""

    def __init__(self, size):
        """
        Initialize a new Stack instance.

        Args:
            size (int): The initial size of the stack.

        """
        self.top = 0
        self.cap = size
        self.stack = self._make_array(size)

    def _make_array(self, size):
        """
        Create and return a new array of the given size.

        Args:
            size (int): The size of the array.

        Returns:
            array: A ctypes array object of the given size.

        """
        temp = (size * ctypes.py_object)()
        return temp

    def isempty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.

        """
        return self.top == 0

    def push(self, elt):
        """
        Push an element onto the top of the stack.

        Args:
            elt: The element to be pushed onto the stack.

        """
        if self.top == self.cap:
            self._resize(2 * self.cap)
        self.stack[self.top] = elt
        self.top += 1

    def pop(self):
        """
        Remove and return the element from the top of the stack.

        Returns:
            The element removed from the top of the stack.

        Raises:
            EmptyStackError: If the stack is empty.

        """
        if self.isempty():
            raise EmptyStackError("Stack is empty.")
        del_item = self.stack[self.top - 1]
        self.stack[self.top - 1] = None
        self.top -= 1
        if self.top < (self.cap // 4):
            self._resize(self.cap // 2)
        return del_item

    def __len__(self):
        """
        Return the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.

        """
        return self.top

    def top_element(self):
        """
        Return the element at the top of the stack without removing it.

        Returns:
            The element at the top of the stack.

        """
        return self.stack[self.top - 1]

    def __str__(self):
        """
        Return a string representation of the stack.

        Returns:
            str: A string representation of the stack.

        """
        stack_as_string = "<"
        for i in range(self.top):
            stack_as_string += str(self.stack[i])
            if i != self.top - 1:
                stack_as_string += ","
        stack_as_string += ">"
        return stack_as_string

    def __getitem__(self, idx):
        """
        Get the element at the given index in the stack.

        Args:
            idx (int): The index of the element to get.

        Returns:
            The element at the given index in the stack.

        Raises:
            IndexError: If the index is out of range.

        """
        if idx >= self.top:
            raise IndexError("Index out of range!")
        return self.stack[idx]

    def __setitem__(self, idx, val):
        """
        Set the element at the given index in the stack to the specified value.

        Args:
            idx (int): The index of the element to set.
            val: The value to set at the given index.

        Raises:
            IndexError: If the index is out of range.

        """
        if idx >= self.top:
            raise IndexError("Index out of range!")
        self.stack[idx] = val


class StackWrapper:
    """
    A wrapper class for a stack implementation using a Python list.
    """

    def __init__(self):
        """
        Initialize a new StackWrapper instance.
        """
        self.stack = []

    def isempty(self):
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
        return str(self.stack)

    def topelement(self):
        """
        Return the element at the top of the stack without removing it.

        Returns:
            The element at the top of the stack.
        """
        return self.stack[-1]


# driver code
if __name__ == "__main__":

    s = Stack(5)
    print(s.isempty())
    print(s)
    s.push(100)
    print(s)
    s.push(-65)
    print(s)
    s.pop()
    print(s)