def staircase(n, num_dict):
    return _staircase_faster(n, num_dict)


def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output = staircase_faster(n - 1, num_dict)

        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)

        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)

        output = first_output + second_output + third_output

    num_dict[n] = output
    return output


# my solution
def _staircase_faster(n, num_dict):
    if n == 1:
        num_dict[1] = 1
    elif n == 2:
        num_dict[2] = 2
    elif n == 3:
        num_dict[3] = 4
    else:
        if (n-1) in num_dict:
            output_1 = _staircase_faster(n - 1, num_dict)
            num_dict[n] = output_1 + num_dict[n-2] + num_dict[n-3]
        else:
            output_1 = _staircase_faster(n - 1, num_dict)
            output_2 = _staircase_faster(n - 2, num_dict)
            output_3 = _staircase_faster(n - 3, num_dict)
            num_dict[n] = output_1 + output_2 + output_3
    return num_dict[n]


initial_num_dict = dict({})


def test_function(test_case):
    answer = staircase(test_case[0], initial_num_dict)
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [3, 4]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)

test_case = [6, 24]
test_function(test_case)

test_case = [18, 35890]
test_function(test_case)
