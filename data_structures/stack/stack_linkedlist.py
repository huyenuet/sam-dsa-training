from data_structures.linked_lists.node import Node


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            # place the new node at the head of the linked list (top)
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        """
            Check if the stack is empty and, if it is, return None
            Get the value from the head node and put it in a local variable
            Move the head so that it refers to the next item in the list
            Return the value we got earlier
        """
        if self.is_empty():
            return None

        top_value = self.head.value
        if self.size() == 1:
            self.head = None
        else:
            self.head = self.head.next

        self.num_elements -= 1
        return top_value

    def top(self):
        if self.head is None:
            return None
        return self.head.value


def test():
    # Setup
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    # Test size
    print("Pass" if (stack.size() == 5) else "Fail")

    # Test pop
    print("Pass" if (stack.pop() == 50) else "Fail")

    # Test push
    stack.push(60)
    print("Pass" if (stack.pop() == 60) else "Fail")
    print("Pass" if (stack.pop() == 40) else "Fail")
    print("Pass" if (stack.pop() == 30) else "Fail")
    stack.push(50)
    print("Pass" if (stack.size() == 3) else "Fail")


# test()
