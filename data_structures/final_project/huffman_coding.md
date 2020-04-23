## why did you use that data structure?
huffman algorithm's idea is: instead of using ascii code to represent string, we encode the string with our own code.
which compresses string to smaller size and information lossless


## The efficiency (time and space) of your solution.
- get_sorted_char_frequency_list: O(nlogn)
    + for char in text: O(n)
    + for key, value in char_frequency_dict.items(): O(n)
    + sorted(): nlogn
- build_huffman_tree: O(nlogn)
    + for, while: O(n)
    + get_sorted_char_frequency_list: O(nlogn)
- encoding: O(nlogn)
    + build_huffman_tree: O(nlogn)
    + trim_huffman_tree: O(n) (recursion)
    + _encode_recursion: O(n)
    + for: O(n)
- decoding: O(n)