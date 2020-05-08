import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    smallest_num = ints[0]
    largest_num = ints[0]

    for num in ints:
        if num < smallest_num:
            smallest_num = num
        elif num > largest_num:
            largest_num = num

    return smallest_num, largest_num


def test_function(test_case):
    min_num, max_num = get_min_max(test_case)
    print("min: {}, max: {}".format(min_num, max_num))
    if min_num == min(test_case) and max_num == max(test_case):
        print("Pass")
    else:
        print("Fail")


test_list = [i for i in range(0, 10)]
random.shuffle(test_list)
test_function(test_list)

test_function([3, 4, 8, 5, 9, 3, 9])

test_function([0])
