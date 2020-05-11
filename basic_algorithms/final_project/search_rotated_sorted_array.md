### Approach
If the pivot point is found, I can decide to find 
the target number in which sub-array
- from 0th  to pivot_index element
- or from pivot_index + 1 to the last element

From there, I would continue to use binary search to
traverse through sub-array, and find the target value


### Efficiency
- Time complexity:
    - find pivot index: `O(m)` where m = pivot index, 
    in the worst case, it will be `O(n)`
    - find target value's index: O(logn)
- Space complexity: O(1)
