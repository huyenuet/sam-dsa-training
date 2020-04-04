from data_structures.stack.stack_linkedlist import Stack


def get_minimum_bracket_reversals(input_string):
    if len(input_string) % 2 == 1:
        return -1

    stack = Stack()
    count = 0
    for bracket in input_string:
        if bracket == "{":
            stack.push(bracket)
        else:
            if stack.top() == "{":
                stack.pop()
            else:
                stack.push(bracket)

    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        if first == '}' and second == '}':
            count += 1
        # '{}' in linked_list means '}{' in a list, because push() method add value to the head
        elif first == '{' and second == '}':
            count += 2
        elif first == '{' and second == '{':
            count += 1
    return count


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = get_minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["{}", 0]
test_function(test_case_1)

test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_3)

test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_4)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_5)
