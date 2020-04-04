class Stack:
    def __init__(self):
        self.arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        if self.next_index == len(self.arr) - 1:
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        old_array = self.arr
        new_size = len(old_array) * 2
        new_array = [0 for _ in range(new_size)]
        for i, value in enumerate(old_array):
            new_array[i] = value
        self.arr = new_array

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return self.next_index == 0

    def pop(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]


# 1. Create and initialize the `Stack` class
def test_init():
    foo = Stack()
    print(foo.arr)
    print("Pass" if foo.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else "Fail")


# 2. Add push method
def test_push():
    foo = Stack()
    foo.push("Test!")
    print(foo.arr)
    print("Pass" if foo.arr[0] == "Test!" else "Fail")


# 3. Handle full capacity
def test_handle_full_capacity():
    foo = Stack()
    foo.push(1)
    foo.push(2)
    foo.push(3)
    foo.push(4)
    foo.push(5)
    foo.push(6)
    foo.push(7)
    foo.push(8)
    foo.push(9)
    foo.push(10)  # The array is now at capacity!
    foo.push(11)  # This one should cause the array to increase in size
    print(foo.arr)  # Let's see what the array looks like now!
    print("Pass" if len(foo.arr) == 20 else "Fail")  # If we successfully doubled the array size, it should now be 20.


# 4. Add the size and is_empty methods
def test_size_and_empty():
    foo = Stack()
    print(foo.size())  # Should return 0
    print(foo.is_empty())  # Should return True
    foo.push("Test")  # Let's push an item onto the stack and check again
    print(foo.size())  # Should return 1
    print(foo.is_empty())  # Should return False


# 5. Add pop method
def test_pop():
    foo = Stack()
    foo.push("Test")  # We first have to push an item so that we'll have something to pop
    print(foo.pop())  # Should return the popped item, which is "Test"
    print(foo.pop())  # Should return None, since there's nothing left in the stack


test_init()
test_push()
test_handle_full_capacity()
test_size_and_empty()
test_pop()
