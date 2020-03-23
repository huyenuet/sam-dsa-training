def smallest_positive(in_list):
    smallest_positive_number = None

    for number in in_list:
        if number > 0:
            if smallest_positive_number is None or smallest_positive_number > number:
                smallest_positive_number = number

    return smallest_positive_number


# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None
