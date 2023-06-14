import ctypes

class ListFullError(Exception):
    pass

class CompactList:
    """
    A compact array implementation of a list.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the List class.

        Args:
            size (int): The initial capacity of the list.
        """
        self.n = 0  # Current number of elements in the list
        self.cap = size  # Current capacity of the list
        self.list = self.make_array(size)  # Internal array to store the elements

    def make_array(self, size):
        """
        Creates a new array of a given size using the ctypes module.

        Args:
            size (int): The size of the array.

        Returns:
            A ctypes array of the specified size.
        """
        return (size * ctypes.py_object)()

    def append(self, elt):
        """
        Adds an element to the end of the list. If the list is full, it doubles the capacity.

        Args:
            elt: The element to be appended.
        """
        if self.n == self.cap:
            raise ListFullError("List is full, delete some elements to append")
        self.list[self.n] = elt
        self.n += 1

    def __len__(self):
        """
        Returns the number of elements in the list.

        Returns:
            int: The number of elements in the list.
        """
        return self.n

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
        if idx >= self.n:
            raise IndexError("List index out of bound")
        return self.list[idx]

    def __setitem__(self, idx, elt):
        """
        Sets the element at the specified index to a new value.

        Args:
            idx (int): The index of the element to set.
            elt: The new value to assign to the element.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if idx >= self.n:
            raise IndexError("List index out of bound")
        self.list[idx] = elt

    def insert(self, idx, elt):
        """
        Inserts an element at the specified index, shifting the existing elements if necessary.

        Args:
            idx (int): The index at which to insert the element.
            elt: The element to be inserted.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not 0 <= idx <= self.n:
            raise IndexError("List index out of bound")
        if self.n == self.cap:
            raise ListFullError("List is full, delete some elements to append")
        for i in range(self.n, idx, -1):
            self.list[i] = self.list[i - 1]  # Shift elements to the right
        self.list[idx] = elt
        self.n += 1

    def delete(self, idx):
        """
        Deletes the element at the specified index, shifting the remaining elements if necessary.

        Args:
            idx (int): The index of the element to delete.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not 0 <= idx < self.n:
            raise IndexError("List index out of bound")
        for i in range(idx, self.n - 1):
            self.list[i] = self.list[i + 1]  # Shift elements to the left
        self.n -= 1

    def extend(self, seq):
        """
        Extends the list by appending all elements from a given sequence.

        Args:
            seq (sequence): The sequence of elements to append.
        """
        for elt in seq:
            self.append(elt)

    def __contains__(self, elt):
        """
        Checks if the list contains a specific element.

        Args:
            elt: The element to check for.

        Returns:
            bool: True if the element is found, False otherwise.
        """
        for idx in range(self.n):
            if self.list[idx] == elt:
                return True
        return False

    def index(self, elt):
        """
        Returns the index of the first occurrence of an element in the list.

        Args:
            elt: The element to find the index of.

        Returns:
            int: The index of the element, or -1 if it is not found.
        """
        for idx in range(self.n):
            if self.list[idx] == elt:
                return idx
        return -1

    def count(self, elt):
        """
        Returns the number of occurrences of an element in the list.

        Args:
            elt: The element to count.

        Returns:
            int: The number of occurrences of the element.
        """
        count = 0
        for idx in range(self.n):
            if self.list[idx] == elt:
                count += 1
        return count

    def get_capacity(self):
        """
        Returns the current capacity of the list.

        Returns:
            int: The current capacity of the list.
        """
        return self.cap

    def is_empty(self):
        """
        Checks if the list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.n == 0

    def __str__(self):
        """
        Returns a string representation of the list.

        Returns:
            str: A string representation of the list.
        """
        string = "<"
        for idx in range(self.n):
            string += str(self.list[idx]) + ","
        return string + ">"
