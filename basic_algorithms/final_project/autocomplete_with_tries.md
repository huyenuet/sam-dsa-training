### Approach
Given a prefix, I need to find all possible suffixes.
First, find the node of the prefix, from there, 
for each child, recursive down the tree and collect respective suffix

base case: suffix is not empty and it's a word
when a suffix is found, add it to a suffix_list


### Efficiency
 - Time complexity:
    - Creating a tree: O(W*L) where `W` is the number of words,
 `L` is average length of the word
    - find: O(L)
    - find all suffixes: O(W*L) where `W` is the number
     of suffixes
 - Space complexity: 