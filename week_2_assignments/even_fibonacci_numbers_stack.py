from data_structures.stack.stack_linkedlist import Stack

threshold = 4000000000


def find_sum_of_even_fibonacci_numbers():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    even_sum = 0
    while True:
        second = stack.pop()
        first = stack.pop()
        if second > threshold:
            break
        if second % 2 == 0:
            even_sum += second
        third = first + second
        stack.push(second)
        stack.push(third)
    return even_sum


print(
    "By considering the terms in the Fibonacci sequence whose values do not exceed four million, the sum of the even-valued terms is:"
)
print(find_sum_of_even_fibonacci_numbers())

# expected value
# 1485607536
