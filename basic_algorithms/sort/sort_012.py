def sort_012(input_list):
    """
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions
    """
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1
    current_idx = 0

    while current_idx <= next_pos_2:
        current_el = input_list[current_idx]

        # if current element is 0, swap them to move 0 to the front of the list
        if current_el == 0:
            input_list[current_idx] = input_list[next_pos_0]
            input_list[next_pos_0] = current_el
            next_pos_0 += 1
            current_idx += 1

        # if current element is 2, swap them to move 2 to the back of the list
        elif current_el == 2:
            input_list[current_idx] = input_list[next_pos_2]
            input_list[next_pos_2] = current_el
            next_pos_2 -= 1

        # if current element is 1, just increase the current index
        else:
            current_idx += 1


def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [0, 1, 2]
test_function(test_case)

test_case = [0, 2, 1, 1]
test_function(test_case)

test_case = [0, 0, 1, 1, 1, 2, 0, 2]
test_function(test_case)
