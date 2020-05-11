def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        return None, None

    first_number = 0
    second_number = 0

    input_list = merge_sort(input_list)

    i = len(input_list) - 1
    while i >= 0:
        first_number = first_number * 10 + input_list[i]
        i -= 1
        if i >= 0:
            second_number = second_number * 10 + input_list[i]
            i -= 1

    return first_number, second_number


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merge_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1

    merge_list += left[i:]
    merge_list += right[j:]

    return merge_list


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

print(rearrange_digits([1, 2, 9, 4, 5, 6]))  # should print (952, 641)
print(rearrange_digits([1]))  # should print (None, None)
print(rearrange_digits([]))  # should print (None, None)
