def down_heapify(arr, n, i):
    # Using i as the index of the current node
    # find the 2 child nodes (if the array were a binary tree) and find the largest value.
    # If one of the children is larger swap the values and recurse into that subtree

    # consider current index as largest
    largest_index = i
    left_node_index = 2 * i + 1
    right_node_index = 2 * i + 2

    # compare with left child
    if left_node_index < n and arr[i] < arr[left_node_index]:
        largest_index = left_node_index

    # compare with right child
    if right_node_index < n and arr[largest_index] < arr[right_node_index]:
        largest_index = right_node_index

    # if either of left / right child is the largest node
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        down_heapify(arr, n, largest_index)


def heap_sort(arr):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end   
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(arr)

    # Build a maxheap. heapify from the last node to the first node
    for i in range(n, -1, -1):
        down_heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        down_heapify(arr, i, 0)


def test_function(test_case):
    heap_sort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
