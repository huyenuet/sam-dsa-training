"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def is_prime_number(number):
    if number == 2:
        return True
    elif number < 2:
        return False
    else:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False
        return True


def find_nth_prime_number(position):
    count = 0
    number = 2
    while True:
        if is_prime_number(number):
            count += 1
        if count == position:
            return number
        number += 1


print(find_nth_prime_number(4))
print(find_nth_prime_number(6))
print(find_nth_prime_number(10001))


# 104743
