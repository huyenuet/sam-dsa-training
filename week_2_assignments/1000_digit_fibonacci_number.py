"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def find_1000_digit_fibonacci_numbers(threshold):
    fibo_1 = 1
    fibo_2 = 1
    index = 2
    while True:
        fibo_3 = fibo_1 + fibo_2
        index += 1
        if fibo_3 >= threshold:
            return index
        fibo_1, fibo_2 = fibo_2, fibo_3


print(find_1000_digit_fibonacci_numbers(pow(10, 2)))
print(find_1000_digit_fibonacci_numbers(pow(10, 1000-1)))
