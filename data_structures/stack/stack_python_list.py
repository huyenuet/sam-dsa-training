class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return None

        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


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
