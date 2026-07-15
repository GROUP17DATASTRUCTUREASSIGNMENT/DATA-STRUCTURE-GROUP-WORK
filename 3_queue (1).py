class Queue:

    def __init__(self):
        self.items = []

    # Add an element to the rear
    def enqueue(self, value):
        self.items.append(value)

    # Remove an element from the front
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    # View the front element
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.items) == 0


# Queue demonstration
queue = Queue()

print("Initial Queue:")
print(queue.items)

queue.enqueue("Student A")
print("\nAfter Enqueue Student A:")
print(queue.items)

queue.enqueue("Student B")
print("\nAfter Enqueue Student B:")
print(queue.items)

queue.enqueue("Student C")
print("\nAfter Enqueue Student C:")
print(queue.items)

print("\nFront:", queue.peek())

print("\nRemoved:", queue.dequeue())
print(queue.items)

queue.enqueue("Student D")
print("\nAfter Enqueue Student D:")
print(queue.items)

print("\nRemoved:", queue.dequeue())
print(queue.items)

# Time Complexity
# Enqueue - O(1)
# Dequeue - O(n)
# Peek - O(1)