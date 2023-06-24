class EmptyQueueError(Exception):
    """
    Exception raised when an operation is performed on an empty queue.
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


class LinkedQueue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front is None

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args:
            item: The item to be added to the queue.
        """
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        """
        Remove and return the item from the front of the queue.

        Returns:
            The item removed from the front of the queue.

        Raises:
            EmptyQueueError: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        removed_item = self.front.item
        self.front = self.front.next
        self._size -= 1

        if self.front is None:
            self.rear = None

        return removed_item

    def peek(self):
        """
        Return the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            EmptyQueueError: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        return self.front.item

    def __len__(self):
        """
        Return the number of items in the queue.

        Returns:
            The number of items in the queue.
        """
        return self._size

    def __str__(self):
        """
        Return a string representation of the queue.

        Returns:
            A string representation of the queue.
        """
        if self.is_empty():
            return "Queue: []"

        queue_items = []
        current = self.front
        while current is not None:
            queue_items.append(str(current.item))
            current = current.next

        return "Queue: [" + ", ".join(queue_items) + "]"


if __name__ == "__main__":
    queue = LinkedQueue()

    print("Is the queue empty?", queue.is_empty())  # Output: True

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Is the queue empty?", queue.is_empty())  # Output: False

    print("Front item of the queue:", queue.peek())  # Output: 10

    item = queue.dequeue()
    print("Dequeued item:", item)  # Output: 10

    print("Length of the queue:", len(queue))  # Output: 2

    print(queue)  # Output: Queue: [20, 30]
