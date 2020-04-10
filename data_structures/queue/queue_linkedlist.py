from data_structures.linked_lists.node import Node


class Queue:

    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value  # copy the value to a local variable
        self.head = self.head.next  # shift the head (i.e., the front of the queue)
        return value

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print(q.head.value)

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print(q.head.value)
