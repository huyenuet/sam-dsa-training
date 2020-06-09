# sam_tech_training
technical training for Automation QA Engineer

## Time Complexity
- approximate
- best case, average case, worst case
- [Big-O Cheatsheet](https://www.bigocheatsheet.com/)
- [Python Complexities](https://wiki.python.org/moin/TimeComplexity)

## Data structure
### List
- Have an order (so you can say things like "give me the 3rd item in the list")
- Have no fixed length (you can add or remove elements)
### Arrays
- accessing to an array is great, but insertion, deletion are massive
- When an array is created, it is always given some initial size
  + the number of elements it should be able to hold
  + all of the elements are 1) next to one another and 2) the same size
- Python lists are essentially arrays, but also include additional high-level functionality
### Linked List

### Stack
#### Time complexity of stacks using linked lists
- Notice that if we pop or push an element with this stack, there's no traversal. We simply add or remove the item from the head of the linked list, and update the `head` reference. So with our linked list implementaion, `pop` and `push` have a time complexity of O(1).

- With a linked list, the nodes do not need to be **contiguous**. They can be scattered in different locations of memory, an that works just fine. We can simply append as many nodes as we like. Using that as the underlying data structure for our stack means that we never run out of capacity, so pushing and popping items will always have a time complexity of O(1).

#### Time complexity of stacks using array
- When we pop or push a element with this stack, there's no traversal, too.
We simply assign new value to current pointer, then increase or decrease the pointer's index
So with array implementation, `pop` and `push` have a time complexity of O(1)
- Until we ran out of space. Then we would have to create an entirely new (larger) array and copy over all of the references from the old array. So `push` can reach a time complexity of O(n)
- That happened because, with an array, we had to specify some initial size (in other words, we had to set aside a contiguous block of memory in advance)

### Queue
Pros and Cons between using array and linked list implementation is same with Stack
#### Time complexity of stacks using linked lists
`enqueue` and `dequeue`: O(1)

### Hash map
Don't use prime number that len(array) divided by prime number produces remainder = 1
ex:
```
len(array) = 10, prime number = 31, coefficient = 1
```

Comparision function:

```
current_coefficient *= prime_number` (1 *= 31)
current_coefficient = current_coefficient % len(array) (31 % 10 = 1)
```

If keys are permutations of n string characters, the bucket_index always be the same value

for example: keys = "abcd", "bcad"

# Basic algorithm
## Sort
### Bubble sort

Approach:
- iterate through the list, if `ls[i] > ls[j] and i < j` => swap them.
Biggest element will be moved to the end of the list
- Do the same thing with the rest

Efficiency
- time complexity: O(n^2)
- space complexity: O(1)

### Merge sort

Approach:
- partition: device the list into halves until list become a single element
- merge: consider 1-element-list is sorted, compare 2 lists and merge them together

Efficiency
- time complexity: O(nlogn)
- space complexity: O(n)

### Quick sort
Efficiency
- time complexity: O(n^2) in the worst case, O(nlogn) in best and average case
- space complexity: O(1)

### Heap sort
Efficiency
- time complexity:
    - heapify: O(logn)
    - createAndBuildHeap: O(n)
    - overall: O(nlogn)
- space complexity: O(1)