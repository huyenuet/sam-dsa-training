def count_inversions(arr):
    # A temp_arr is created to store sorted array in merge function
    temp_arr = [None for _ in range(len(arr))]
    return _count_inversions(arr, temp_arr, 0, len(arr) - 1)


# This Function will use MergeSort to count inversions

def _count_inversions(arr, temp_arr, left, right):
    # A variable inv_count is used to store
    # inversion counts in each recursive call

    inv_count = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:
        # mid is calculated to divide the array into two sub-arrays
        # Floor division is must in case of python

        mid = (left + right) // 2

        # It will calculate inversion counts in the left subarray

        inv_count += _count_inversions(arr, temp_arr, left, mid)

        # It will calculate inversion counts in right subarray

        inv_count += _count_inversions(arr, temp_arr, mid + 1, right)

        # It will merge two sub-arrays in a sorted sub-array

        inv_count += merge_and_count_inversions(arr, temp_arr, left, mid, right)

    return inv_count


# This function will merge two sub-arrays in a single sorted sub-array
def merge_and_count_inversions(arr, temp_arr, left, mid, right):
    i = left  # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")


arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [9, 6, 8, 4]
solution = 5
test_case = [arr, solution]
test_function(test_case)

arr = [1, 20, 6, 4, 5]
solution = 5
test_case = [arr, solution]
test_function(test_case)