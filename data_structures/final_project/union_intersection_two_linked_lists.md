## why did you use that data structure?
- union of l1 and l2: elements that are in l1 or in l2
- intersection of l1 and l2: elements that are both in l1 and l2

Each element should appear only once in Union or Intersection set

Using a set to eliminate the frequency of each element

Beside, there's already an intersection method implemented in Python Set

## The efficiency (time and space) of your solution.
Time complexity:
- traverse through the linked list, get all elements then add to a set: O(n)
- union is adding all elements in 1 set: O(1)
- intersection is traversal through the shorter set, collect all elements that also appear on the other set: 
 O(min(len(set1), len(set2))