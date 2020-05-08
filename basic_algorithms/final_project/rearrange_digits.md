### Approach
#### 1. Finding the pattern

From highest to lowest, each number in the list will be allocated to number_1 and number_2 

Given numbers: 1, 2, 3, 4, 5, 6

2 numbers have maximum sum are: 642, 531

#### 2. sort the list
Because solution must have time complexity equal to O(nlogn),
I choose Merge Sort (heap sort is an other solution)


### Efficiency
- Time complexity: O(nlogn)
- Space complexity: O(1)
