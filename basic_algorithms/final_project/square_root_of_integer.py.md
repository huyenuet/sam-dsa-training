### Approach
Time complexity must be O(log(n)), so I think of dividing integer list into halves, 
to search for floored square root number

Since I can consider I'm looking for a right number
in a sorted list from 0 to the given number.
I decided to apply binary search here

### Efficiency
Every time I want to search next number, I just need to pick the middle number,
then compare
- If this isn't the right number, I pick next number, 
which is the middle number of left/ right half
- Keep going on, I don't need to traverse all elements that are smaller than the given number
- Time Complexity: O(log(n))
- Space complexity: O(log(n)) since every recursion, I need to store value to `mid` variable
