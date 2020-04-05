# Here is our Stack Class
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    """
    Need 2 stacks: one for `enqueue`, one for `dequeue`
    1. For `enqueue`: push in stack 1
    2. For `dequeue`:
        a. Check if stack 2 is empty:
         - transfer elements from stack 1 into stack 2
         - pop(stack 2)
        b. Check if stack 2 is not empty:
        - pop(stack 2)
    """

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def size(self):
        return self.stack_2.size() + self.stack_1.size()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        if self.stack_2.is_empty():
            while self.stack_1.items:
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()
    
    def is_empty(self):
        return self.stack_1.is_empty() and self.stack_2.is_empty()


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print("Pass" if (q.size() == 1) else "Fail")
