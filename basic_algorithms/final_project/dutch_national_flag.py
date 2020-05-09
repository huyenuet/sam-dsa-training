def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    Return:
        input_list(list): sorted list
    """
    index_0 = 0
    index_2 = len(input_list) - 1
    i = 0
    while i <= index_2:
        current_element = input_list[i]
        if current_element == 0:
            # swap to move 0 to the position of index_0
            input_list[i] = input_list[index_0]
            input_list[index_0] = current_element
            index_0 += 1
            i += 1
        elif current_element == 2:
            # swap to move 2 to the position of index_2
            input_list[i] = input_list[index_2]
            input_list[index_2] = current_element
            index_2 -= 1
        else:
            i += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Given an input array consisting on only 0, 1, and 2
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
