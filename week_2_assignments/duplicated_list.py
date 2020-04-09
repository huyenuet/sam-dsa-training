"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all
the duplicates. The order should remain the same.
"""


def remove_duplicated_numbers(ls: list):
    new_list = []
    for number in ls:
        if number not in new_list:
            new_list.append(number)
    return new_list


print(remove_duplicated_numbers([1, 2, 4, 1, 6]))
print(remove_duplicated_numbers([1, 1, 2, 4, 1, 6, 6, 2]))
