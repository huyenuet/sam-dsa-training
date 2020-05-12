### Approach
A Blockchain is a sequential chain of records, similar to a linked list.

Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

# Efficiency
- Time complexity: O(n) for `find` and `append` methods
- Space complexity: O(n) to store each block in a node of the linked list
