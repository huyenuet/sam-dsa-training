def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2
    while left < right:
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid
            mid = (left + right) // 2
        else:
            if left + 1 == right:
                mid = right
                continue
            left = mid
            mid = (left + right) // 2
    return -1


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


# test case 1
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)

# test case 2
array = []
target = 6
index = -1
test_case = [array, target, index]
test_function(test_case)

# test case 3
array = [1, 2]
target = 1
index = 0
test_case = [array, target, index]
test_function(test_case)
