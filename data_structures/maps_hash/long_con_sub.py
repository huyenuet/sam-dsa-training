def longest_consecutive_subsequence(input_list):
    """Write longest consecutive subsequence solution"""
    num_set = set()

    # iterate over the list and store element in a suitable data structure
    for number in input_list:
        num_set.add(number)

    max_length = 0
    start_number = None
    # traverse / go over the data structure in a reasonable order to determine the solution
    for number in input_list:
        count = 0
        if (number - 1) not in num_set:
            start_el = number

            while number in num_set:
                number += 1
                count += 1

            if count > max_length:
                max_length = count
                start_number = start_el

    return [element for element in range(start_number, start_number + max_length)]


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)

test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ], [8, 9, 10, 11, 12]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)

test_case_4 = [[0, 1, 2, 3, 4, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4]]
test_function(test_case_4)
