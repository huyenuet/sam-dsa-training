## why did you use that data structure?
The concept of problem is "least recently used", that makes me immediately think about Queue.

But queue is most efficient for "least recently added" structure, not "used"
=> Not a good solution

Let think about "least recently added" data structure like a list of items.
- Item used the most should stand firstly 
- Item used the least should stand lastly 

Because the operation get() and set() should have time complexity = O(1), then I think of hash map.
Use a dictionary to store key - value pairs, I can access to each item with time complexity = O(1)


### `set()` 
I need to add new item and remove "least recently used" item when cache is full
- I need an other data structure to keep the "least recently used" item always stands at an easy position to remove from the Cache.
- Also, adding new item should be O(1)

### `get()`
I need to do 2 things 
- access the key - value (use dictionary)
- make it "most recently used" by removing it from current position, then add it to the "most recently used" position

for removing and adding an item to the head and tail of a list, I can use double linked list 

But for removing an item from any position, double linked list take O(k) to find the position. The deletion/insertion takes O(1)

If I can save an exact node of the linked list that needed to be deleted, the deletion/insertion will only take O(1)
 
So instead of storing key - value pairs inside dictionary, I'll store key - node (value is stored in node)

## The efficiency (time and space) of your solution.

get(): 
- get key in dictionary: O(1)
- get the respective node: O(1)
- delete that node from current position: O(1)
- add that node to the head of linked list (to make it most recently used): O(1)

set():
- if cache is full
    - remove least recently used node from linked list: O(1)
    - remove respective key-node from dictionary: O(1)
    
- else:
    - add new node to the head of linked list: O(1)
    - add new key-node pairs to dictionary: O(1)

In conclusion
- Time complexity is O(1)
- Space complexity is O(n) (no compression)