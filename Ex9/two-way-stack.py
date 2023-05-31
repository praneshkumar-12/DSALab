import ctypes


class StackFullError(Exception):
    """Exception raised when attempting to push an item to a full stack."""
    pass


class TwoWayStack:
    def __init__(self, size):
        """Initialize a two-way stack with the given size.

        Args:
            size (int): The maximum number of elements that can be stored in the stack.
        """
        self.cap = size
        self.stack = self.make_array(size)
        self.top1 = 0
        self.top2 = size - 1

    def make_array(self, size):
        """Create and return a new array with the given size.

        Args:
            size (int): The size of the array to be created.

        Returns:
            ctypes.py_object: The created array.
        """
        temp = (size * ctypes.py_object)()
        return temp

    def push(self, stack_num, item):
        """Push an item onto the specified stack.

        Args:
            stack_num (int): The number of the stack to push the item to.
            item: The item to be pushed.

        Raises:
            StackFullError: If the specified stack is full.
        """
        if self.is_full():
            raise StackFullError("Stack is full!")

        if stack_num == 0:
            self.stack[self.top1] = item
            self.top1 += 1
        elif stack_num == 1:
            self.stack[self.top2] = item
            self.top2 -= 1

    def pop(self, stack_num):
        """Pop and return the top item from the specified stack.

        Args:
            stack_num (int): The number of the stack to pop the item from.

        Returns:
            The popped item from the specified stack.
        """
        if stack_num == 0:
            del_item = self.stack[self.top1]
            self.stack[self.top1] = "-"
            self.top1 -= 1
            return del_item
        if stack_num == 1:
            del_item = self.stack[self.top2]
            self.stack[self.top2] = "-"
            self.top2 += 1
            return del_item

    def is_full(self):
        """Check if the two-way stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return self.top1 > self.top2

    def __getitem__(self, idx):
        """Get the item at the specified index in the stack.

        Args:
            idx (int): The index of the item to get.

        Returns:
            The item at the specified index in the stack.

        Raises:
            IndexError: If the index is out of range.
        """
        if idx > self.top2:
            raise IndexError("Index out of range!")
        return self.stack[idx]

    def is_empty(self, stack_num):
        """Check if the specified stack is empty.

        Args:
            stack_num (int): The number of the stack to check.

        Returns:
            bool: True if the specified stack is empty, False otherwise.
        """
        if stack_num == 0:
            return self.top1 == -1
        if stack_num == 1:
            return self.top2 == self.cap

    def __str__(self):
        """Return a string representation of the two-way stack.

        Returns:
            str: A string representation of the two-way stack.
        """
        string = "2WS:["
        for idx in range(self.cap):
            try:
                string += str(self.stack[idx])
            except ValueError:
                string += "-"
                continue
            finally:
                if not idx == self.cap - 1:
                    string += ","
        string += "]"
        return string


# driver code
if __name__ == "__main__":
    import random

    tws = TwoWayStack(10)

    for _ in range(10):
        stack_n = random.randint(0, 1)
        num = random.randint(0, 100)
        tws.push(stack_n, num)
        print(tws)

    while True:
        stack_n = random.randint(0, 1)
        if tws.is_empty(stack_n):
            continue
        tws.pop(stack_n)
        print(tws)
        if tws.is_empty(0) and tws.is_empty(1):
            break
