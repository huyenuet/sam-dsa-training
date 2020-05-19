# Game Solver
## Introduction
We will implement a solver for a logic game. You will be given a grid of tiles, some of the tiles are filled with either red or blue, and the other tiles are empty.

The goal of the game is to fill the empty tiles in the grid with either red or blue such that the following rules are satisfied:
1. No three consecutive tiles have the same colour.
2. On each row or column of the grid, the number of red tiles equals to the number of blue ones.
3. No two rows or no two columns are the same.

### Input
A two-dimensional array of size n×n, where n is an even number, n>=4. Each element of an array can be either 0, 1, or 2. 0 represents an empty tile, 1 and 2 represent red and blue tiles, respectively.

### Output
A two-dimensional array of size n×n. The non-zero elements of the input must be the same in the output. There are no zeros in the output, and the three rules of the game must be satisfied.

### Example

Input
```
[
  [1, 1, 0, 0],
  [2, 0, 0, 0],
  [0, 0, 0, 2],
  [0, 0, 1, 0],
]
```
Output
```
[
  [1, 1, 2, 2],
  [2, 1, 2, 1],
  [1, 2, 1, 2],
  [2, 2, 1, 1],
]
```

## Explanation
The first row is `[1, 1, 0, 0]`. By the second rule, the last two elements must be 2.
Therefore, the first row is `[1, 1, 2, 2]`.

The last column is `[2, 0, 2, 0]`. By the second rule, the remaining two elements must be 1.

By repeatedly applying the given rules, we can replace zeros in the input array with either 1 or 2 to obtain the output.

