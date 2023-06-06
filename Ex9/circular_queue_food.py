class CircularQueue:
    """Circular Queue implementation using a list"""

    def __init__(self, max_orders):
        """
        Initialize the circular queue with a maximum number of orders
        :param max_orders: Maximum number of orders the queue can hold
        """
        self.max_orders = max_orders
        self.queue = [None] * max_orders
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """
        Check if the circular queue is empty
        :return: True if the queue is empty, False otherwise
        """
        return self.front == -1

    def is_full(self):
        """
        Check if the circular queue is full
        :return: True if the queue is full, False otherwise
        """
        return (self.rear + 1) % self.max_orders == self.front

    def enqueue(self, order):
        """
        Add an order to the circular queue
        :param order: Order to be added
        :return: True if the order is successfully added, False if the queue is full
        """
        if self.is_full():
            print("Queue is full. Cannot accept more orders.")
            return False

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.max_orders
        self.queue[self.rear] = order
        print(f"Order {order} added to the queue.")
        return True

    def dequeue(self):
        """
        Serve the next order in the circular queue (FIFO)
        :return: The served order if the queue is not empty, None otherwise
        """
        if self.is_empty():
            print("No orders in the queue.")
            return None

        order = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_orders

        print(f"Order {order} served.")
        return order


# Example usage

# Create a circular queue with a maximum of 5 orders
cq = CircularQueue(5)

# Add orders to the queue
cq.enqueue("Order 1")
cq.enqueue("Order 2")
cq.enqueue("Order 3")
cq.enqueue("Order 4")
cq.enqueue("Order 5")
cq.enqueue("Order 6")  # Queue is full, cannot accept more orders

# Serve orders from the queue
cq.dequeue()  # Order 1 served
cq.dequeue()  # Order 2 served
cq.dequeue()  # Order 3 served
cq.dequeue()  # Order 4 served
cq.dequeue()  # Order 5 served
cq.dequeue()  # No orders in the queue
