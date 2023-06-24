class ElementNotFoundError(Exception):
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


class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty Singly Linked List.
        """
        self.head = self.tail = Node()
        self.size = 0

    def is_empty(self):
        """
        Check if the linked list is empty.

        Returns:
            True if the linked list is empty, False otherwise.
        """
        return self.head == self.tail

    def display(self):
        """
        Display the items in the linked list.
        """
        if self.is_empty():
            print("LinkedList is empty.")
        else:
            current = self.head.next
            while current is not None:
                print(current.item, end=" ")
                current = current.next
            print()

    def find(self, item):
        """
        Find the index of a given item in the linked list.

        Args:
            item: The item to be searched in the linked list.

        Returns:
            The index of the item if found, -1 otherwise.
        """
        current = self.head.next
        index = 0
        while current is not None:
            if current.item == item:
                return index
            current = current.next
            index += 1
        return -1

    def append(self, item):
        """
        Append a new node with the specified item to the end of the linked list.

        Args:
            item: The item to be appended.
        """
        new_node = Node(item)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def insert(self, pos, item):
        """
        Insert a new node with the specified item at the given position in the linked list.

        Args:
            pos: The position at which the item should be inserted.
            item: The item to be inserted.

        Raises:
            IndexError: If the position is out of range.
        """
        if pos < 0 or pos > self.size:
            raise IndexError("Index out of range")

        if pos == self.size:
            self.append(item)
            return

        current = self.head
        for _ in range(pos):
            current = current.next

        new_node = Node(item, current.next)
        current.next = new_node
        self.size += 1

    def delete(self, pos):
        """
        Delete the node at the specified position in the linked list.

        Args:
            pos: The position of the node to be deleted.

        Raises:
            IndexError: If the position is out of range.
        """
        if pos < 0 or pos >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(pos):
            current = current.next

        del_node = current.next
        current.next = del_node.next
        if current.next is None:
            self.tail = current
        del del_node
        self.size -= 1

    def insert_by_value(self, prev_value, item):
        """
        Insert a new node with the specified item after the node containing the previous value.

        Args:
            prev_value: The previous value after which the new node should be inserted.
            item: The item to be inserted.

        Raises:
            ElementNotFoundError: If the previous value is not found in the linked list.
        """
        prev = self.find_prev(prev_value)
        if prev is None:
            raise ElementNotFoundError("Previous value not found")

        new_node = Node(item, prev.next)
        prev.next = new_node
        if prev == self.tail:
            self.tail = new_node
        self.size += 1

    def delete_by_value(self, prev_value):
        """
        Delete the node following the node containing the previous value.

        Args:
            prev_value: The previous value whose next node should be deleted.

        Raises:
            ElementNotFoundError: If the previous value is not found in the linked list.
        """
        prev = self.find_prev(prev_value)
        if prev is None or prev.next is None:
            raise ElementNotFoundError("Previous value not found")

        del_node = prev.next
        prev.next = del_node.next
        if prev.next is None:
            self.tail = prev
        del del_node
        self.size -= 1

    def find_prev(self, item):
        """
        Find the node preceding the node containing the specified item.

        Args:
            item: The item whose preceding node should be found.

        Returns:
            The preceding node if found, None otherwise.
        """
        current = self.head
        while current.next is not None:
            if current.next.item == item:
                return current
            current = current.next
        return None


if __name__ == "__main__":
    # Create a new SinglyLinkedList
    linked_list = SinglyLinkedList()

    # Append elements to the linked list
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    # Display the linked list
    print("Linked List:")
    linked_list.display()  # Output: 10 20 30

    # Find an item in the linked list
    index = linked_list.find(20)
    if index != -1:
        print("Found at index:", index)  # Output: Found at index: 1
    else:
        print("Item not found")

    # Insert an item at a specific position
    linked_list.insert(1, 15)
    print("After Insertion:")
    linked_list.display()  # Output: 10 15 20 30

    # Delete an item at a specific position
    linked_list.delete(2)
    print("After Deletion:")
    linked_list.display()  # Output: 10 15 30

    # Insert an item by specifying the previous value
    try:
        linked_list.insert_by_value(15, 25)
        print("After Insertion by Value:")
        linked_list.display()  # Output: 10 15 25 30
    except ElementNotFoundError:
        print("Previous value not found")

    # Delete an item by specifying the previous value
    try:
        linked_list.delete_by_value(15)
        print("After Deletion by Value:")
        linked_list.display()  # Output: 10 25 30
    except ElementNotFoundError:
        print("Previous value not found")
