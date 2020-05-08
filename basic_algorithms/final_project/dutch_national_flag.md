### Approach

If I divide the list into 3 parts: 0, 1, 2.

By keeping track of element 0's index and 2's index, 
I can make sure 0's indexes always stay at the left side of the list. 
Similar with 2's index, it should always stay at the right side of the list.

In a single traversal
- when I meet a 0, I will swap it 
with the element at the position of 0's index, increase index_0 and current index by 1
- when I meet a 1, I don't do anything but increase the current index by 1. Because when all 0s and 2s 
in the right places, 1s will be auto in the right places, too.
- when I meet a 2, wap it with the element at the position of 2's index, decrease index_2 by 1


### Efficiency
- Time complexity: O(n) in the worst case when there's no 2 in the list
- Space complexity: O(1)
