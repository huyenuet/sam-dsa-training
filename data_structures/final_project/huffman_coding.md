## why did you use that data structure?
huffman algorithm's idea is: instead of using ascii code to represent string, we encode the string with our own code.
which compresses string to smaller size and information lossless


## The efficiency (time and space) of your solution.
- build huffman tree: O(n)
- get_sorted_char_frequency_list: O(n^2)
- _encode_recursion: O(n)
- _decode_recursion: O(n)
- encoding: O(n^2)
- decoding: O(n)