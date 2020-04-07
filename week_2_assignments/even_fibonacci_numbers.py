threshold = 4000000000


def find_sum_of_even_fibonacci_numbers():
    fibo_1 = 1
    fibo_2 = 1
    even_sum = 0
    while True:
        fibo_3 = fibo_1 + fibo_2
        if fibo_3 > threshold:
            break
        if fibo_3 % 2 == 0:
            even_sum += fibo_3
        fibo_1, fibo_2 = fibo_2, fibo_3

    return even_sum


print(
    "By considering the terms in the Fibonacci sequence whose values do not exceed four million, the sum of the even-valued terms is:"
)
print(find_sum_of_even_fibonacci_numbers())

# expected value
# 1485607536
