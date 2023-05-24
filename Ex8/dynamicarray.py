import ctypes


class DynamicArray:
    """
        A dynamic array implementation that can store various types of values.
    """

    def __init__(self, val):
        """
            Initializes a new DynamicArray instance.

            Args: val: An integer, list, tuple, or string to initialize the array with. - If an integer is provided,
            it sets the initial capacity of the array. - If a list or tuple is provided, it sets the initial capacity
            and populates the array with the values. - If a string is provided, it sets the initial capacity and
            populates the array with individual characters.

            Raises:
                TypeError: If the provided value is not of type int, list, tuple, or string.
        """
        if isinstance(val, int):
            self.n = 0
            self.capacity = val
            self.array = self.make_array(self.capacity)
        elif isinstance(val, list) or isinstance(val, tuple):
            self.n = len(val)
            self.capacity = len(val)
            self.array = val
        elif isinstance(val, str):
            self.n = len(val)
            self.capacity = len(val)
            self.array = [i for i in val]

    def make_array(self, size):
        """
            Creates and returns a new ctypes array of the specified size.

            Args:
                size: The size of the new array.

            Returns:
                A ctypes array of size 'size'.

        """
        temp = (size * ctypes.py_object)()
        return temp

    def append(self, val):
        """
            Appends a value to the end of the dynamic array.

            Args:
                val: The value to be appended.
        """
        if self.n == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.n] = val
        self.n += 1

    def resize(self, size):
        """
            Resizes the dynamic array to the specified size.

            Args:
                size: The new size of the array.

        """
        new_array = self.make_array(size)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = size

    def get_capacity(self):
        """
           Returns the current capacity of the dynamic array.

           Returns:
               The current capacity of the array.
       """
        return self.capacity

    def __str__(self):
        """
            Returns a string representation of the dynamic array.

            Returns:
                A string representation of the dynamic array.
        """
        array_string = '<'
        for i in range(self.n):
            array_string += str(self.array[i])
            if i != self.n - 1:
                array_string += ','
        array_string += '>'
        return array_string

    def __len__(self):
        """
            Returns the number of elements in the dynamic array.

            Returns:
                The number of elements in the array.
        """
        return len(self.array)

    def __getitem__(self, idx):
        """
            Returns the element at the specified index.

            Args:
                idx: The index of the element to retrieve.

            Returns:
                The element at the specified index.

            Raises:
                IndexError: If the index is out of range.
        """
        if idx >= self.n:
            raise IndexError("Index out of range!")
        return self.array[idx]

    def __setitem__(self, idx, value):
        """
            Sets the value at the specified index.

            Args:
                idx: The index of the element to set.
                value: The value to set at the specified index.

            Raises:
                IndexError: If the index is out of range.
        """
        if idx >= self.n:
            raise IndexError("Index out of range!")
        self.array[idx] = value


# driver code
if __name__ == "__main__":
    d1 = DynamicArray(4)
    d1.append(324)
    print(d1)
    d1[0] = 5
    print(d1)
