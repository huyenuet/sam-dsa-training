correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

correct2 = [1]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               

# Define a function check_sudoku() here:
def check_sudoku(square_list):
    sudoku_len = len(square_list)

    # square_list has 1 row, 1 column
    if sudoku_len == 1:
        if square_list[0] == 1:
            return True
        else:
            return False

    # check for rows
    for row in square_list:
        for num in row:
            # number is out of range -> return False
            if num not in range(1, sudoku_len+1):
                return False

            # number in row appears more than 1 time -> return False
            if row.count(num) > 1:
                return False

    # check for columns
    for col_idx in range(sudoku_len):
        col = []
        for row_idx in range(sudoku_len):
            col.append(square_list[row_idx][col_idx])

        for num in col:
            # number is out of range -> return False
            if num not in range(1, sudoku_len+1):
                return False

            # number in column appears more than 1 time -> return False
            if col.count(num) > 1:
                return False

    return True
    

print(check_sudoku(correct))
#>>> True

print(check_sudoku(correct2))
#>>> True

print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False


