class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at head
    def insert_head(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at tail
    def insert_tail(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Delete by value
    def delete(self, value):

        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:

            if current.next.data == value:
                current.next = current.next.next
                return

            current = current.next

    # Traverse and print
    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Linked List demonstration
ll = LinkedList()

ll.insert_head(30)
ll.insert_head(20)
ll.insert_head(10)

print("After inserting at head:")
ll.display()

ll.insert_tail(40)
ll.insert_tail(50)

print("\nAfter inserting at tail:")
ll.display()

ll.delete(20)

print("\nAfter deleting 20:")
ll.display()

ll.delete(50)

print("\nAfter deleting 50:")
ll.display()

# Time Complexity
# Insert at Head - O(1)
# Insert at Tail - O(n)
# Delete by Value - O(n)
# Traverse - O(n)