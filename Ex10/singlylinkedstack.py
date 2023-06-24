class EmptyStackError(Exception):
    """
    Exception raised when an operation is performed on an empty stack.
    """
    pass


class Node:
    __slots__ = ["item", "next"]

    def __init__(self, item=None, next=None):
        """
        Initialize a Node with an item and next pointer.

        Args:
            item: The item to be stored in the node.
            next: The reference to the next node.
        """
        self.item = item
        self.next = next


class LinkedStack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.top = None
        self._size = 0

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top is None

    def push(self, item):
        """
        Push an item onto the stack.

        Args:
            item: The item to be pushed onto the stack.
        """
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """
        Pop an item from the stack.

        Returns:
            The item that is popped from the stack.

        Raises:
            EmptyStackError: If the stack is empty.
        """
        if self.is_empty():
            raise EmptyStackError("Stack is empty")

        popped_item = self.top.item
        self.top = self.top.next
        self._size -= 1

        return popped_item

    def peek(self):
        """
        Return the top item of the stack without removing it.

        Returns:
            The top item of the stack.

        Raises:
            EmptyStackError: If the stack is empty.
        """
        if self.is_empty():
            raise EmptyStackError("Stack is empty")

        return self.top.item

    def __len__(self):
        """
        Return the number of items in the stack.

        Returns:
            The number of items in the stack.
        """
        return self._size

    def __getitem__(self, index):
        """
        Get the item at the specified index.

        Args:
            index: The index of the item to retrieve.

        Returns:
            The item at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        current = self.top
        for _ in range(index):
            current = current.next

        return current.item

    def __str__(self):
        """
        Return a string representation of the stack.

        Returns:
            A string representation of the stack.
        """
        if self.is_empty():
            return "Stack: []"

        stack_items = []
        current = self.top
        while current is not None:
            stack_items.append(str(current.item))
            current = current.next

        return "Stack: [" + ", ".join(stack_items) + "]"


if __name__ == "__main__":
    stack = LinkedStack()

    print("Is the stack empty?", stack.is_empty())  # Output: True

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Is the stack empty?", stack.is_empty())  # Output: False

    print("Top item of the stack:", stack.peek())  # Output: 30

    item = stack.pop()
    print("Popped item:", item)  # Output: 30

    print("Length of the stack:", len(stack))  # Output: 2

    print("Item at index 0:", stack[0])  # Output: 20
    print("Item at index 1:", stack[1])  # Output: 10

    print(stack)  # Output: Stack: [20, 10]
