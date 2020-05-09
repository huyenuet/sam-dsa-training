def rotated_array_search(input_list, target):
    input_length = len(input_list)

    # input list is empty
    if input_length == 0:
        return -1

    # find pivot point
    pivot_index = 0
    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i + 1]:
            pivot_index = i
            break

    if target == input_list[0]:
        return 0
    elif target > input_list[0]:
        return binary_search(input_list, target, 0, pivot_index)
    else:
        return binary_search(input_list, target, pivot_index + 1, len(input_list))


def binary_search(input_list, target, left, right):
    mid = (left + right) // 2
    if left > right:
        return -1
    if input_list[mid] == target:
        return mid
    elif input_list[mid] > target:
        return binary_search(input_list, target, left, mid - 1)
    else:
        return binary_search(input_list, target, mid + 1, right)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([[1], 10])
