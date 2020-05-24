example_1 = [[1, 1, 0, 0],
             [2, 0, 0, 0],
             [0, 0, 0, 2],
             [0, 0, 1, 0]]

example_2 = [
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 2, 0],
]


def solve_game(input_arr):
    arr_size = len(input_arr)

    if arr_size % 2 != 0:
        raise Exception("Array size must be an even number")

    if arr_size < 4:
        raise Exception("Array size must be greater than or equal to 4")

    temp_arr = apply_rule_1(input_arr)

    while not is_game_solved(input_arr):
        temp_arr = apply_rule_2(temp_arr)
        temp_arr = apply_rule_3(temp_arr)
        temp_arr = apply_rule_1(temp_arr)

    return temp_arr


def apply_rule_1(input_arr):
    """
    No three consecutive tiles have the same colour.
    """
    arr_size = len(input_arr)

    # check row
    for row in input_arr:
        indices_of_2 = []
        indices_of_1 = []
        for index, num in enumerate(row):
            if num == 1:
                indices_of_1.append(index)
            elif num == 2:
                indices_of_2.append(index)
        i = 0
        while i < len(indices_of_2) and i + 1 < len(indices_of_2):

            # 1. if there are 2 consecutive tiles have the same color,
            # the next and previous tiles should be a the other color
            if indices_of_2[i + 1] == indices_of_2[i] + 2:
                row[indices_of_2[i] + 1] = 1

            # 2. if there are 2 tiles distributed like 2, 0, 2 => 0 should be replaced by 1
            elif indices_of_2[i + 1] == indices_of_2[i] + 1:
                if indices_of_2[i] + 2 < arr_size:
                    row[indices_of_2[i] + 2] = 1
                if indices_of_2[i] >= 1:
                    row[indices_of_2[i] - 1] = 1
            i += 1

        i = 0
        while i < len(indices_of_1) and i + 1 < len(indices_of_1):
            if indices_of_1[i + 1] == indices_of_1[i] + 2:
                row[indices_of_1[i] + 1] = 2
            elif indices_of_1[i + 1] == indices_of_1[i] + 1:
                if indices_of_1[i] + 2 < arr_size:
                    row[indices_of_1[i] + 2] = 2
                if indices_of_1[i] >= 1:
                    row[indices_of_1[i] - 1] = 2
            i += 1

    # check column
    for col_idx in range(0, arr_size):
        indices_of_2 = []
        indices_of_1 = []
        for row_idx in range(0, arr_size):
            if input_arr[row_idx][col_idx] == 1:
                indices_of_1.append(row_idx)
            if input_arr[row_idx][col_idx] == 2:
                indices_of_2.append(row_idx)
        i = 0
        while i < len(indices_of_2) and i + 1 < len(indices_of_2):
            if indices_of_2[i + 1] == indices_of_2[i] + 2:
                input_arr[indices_of_2[i] + 1][col_idx] = 1
            elif indices_of_2[i + 1] == indices_of_2[i] + 1:
                if indices_of_2[i] + 2 < arr_size:
                    input_arr[indices_of_2[i] + 2][col_idx] = 1
                if indices_of_2[i] >= 1:
                    input_arr[indices_of_2[i] - 1][col_idx] = 1
            i += 1

        i = 0
        while i < len(indices_of_1) and i + 1 < len(indices_of_1):
            if indices_of_1[i + 1] == indices_of_1[i] + 2:
                input_arr[indices_of_1[i] + 1][col_idx] = 2
            elif indices_of_1[i + 1] == indices_of_1[i] + 1:
                if indices_of_1[i] + 2 < arr_size:
                    input_arr[indices_of_1[i] + 2][col_idx] = 2
                if indices_of_1[i] >= 1:
                    input_arr[indices_of_1[i] - 1][col_idx] = 2
            i += 1

    return input_arr


def apply_rule_2(input_arr):
    """
    On each row or column of the grid, the number of red tiles equals to the number of blue ones.
    """

    # check row
    for row_idx, row in enumerate(input_arr):
        total_1 = row.count(1)
        total_2 = row.count(2)

        if total_1 == (len(input_arr) / 2):
            input_arr[row_idx] = [2 if num == 0 else num for num in row]
        elif total_2 == (len(input_arr) / 2):
            input_arr[row_idx] = [1 if num == 0 else num for num in row]

    # check column
    arr_size = len(input_arr)
    for i in range(0, arr_size):
        total_1 = 0
        total_2 = 0
        for j in range(0, arr_size):
            if input_arr[j][i] == 1:
                total_1 += 1
            elif input_arr[j][i] == 2:
                total_2 += 1
        if total_1 == arr_size / 2:
            for j in range(0, arr_size):
                if input_arr[j][i] == 0:
                    input_arr[j][i] = 2
        elif total_2 == arr_size / 2:
            for j in range(0, arr_size):
                if input_arr[j][i] == 0:
                    input_arr[j][i] = 1

    return input_arr


def apply_rule_3(input_arr):
    """
    No two rows or no two columns are the same.
    """
    arr_size = len(input_arr)

    # check column
    for col_idx in range(0, arr_size - 1):
        for next_col_idx in range(col_idx + 1, arr_size):
            different_positions = []
            for row_idx in range(0, arr_size):
                if input_arr[row_idx][col_idx] == input_arr[row_idx][next_col_idx] == 0:
                    different_positions = []
                    break
                if (
                    (input_arr[row_idx][col_idx] == 0 or input_arr[row_idx][next_col_idx] == 0)
                    and (input_arr[row_idx][col_idx] != input_arr[row_idx][next_col_idx])
                ):
                    different_positions.append((row_idx, col_idx, next_col_idx))

            # 2 columns are the same except 2 cells
            if len(different_positions) == 2:
                for row_idx, i, j in different_positions:
                    if input_arr[row_idx][i] != 0 and input_arr[row_idx][j] == 0:
                        tiles = [1, 2]
                        tiles.pop(tiles.index(input_arr[row_idx][i]))
                        input_arr[row_idx][j] = tiles[0]
                    elif input_arr[row_idx][j] != 0 and input_arr[row_idx][i] == 0:
                        tiles = [1, 2]
                        tiles.pop(tiles.index(input_arr[row_idx][j]))
                        input_arr[row_idx][i] = tiles[0]

    # check row
    for row_idx in range(0, arr_size - 1):
        for next_row_idx in range(row_idx + 1, arr_size):
            different_positions = []
            for col_idx in range(0, arr_size):
                if input_arr[row_idx][col_idx] == input_arr[next_row_idx][col_idx] == 0:
                    different_positions = []
                    break
                if (
                    (input_arr[row_idx][col_idx] == 0 or input_arr[next_row_idx][col_idx] == 0)
                    and (input_arr[row_idx][col_idx] != input_arr[next_row_idx][col_idx])
                ):
                    different_positions.append((col_idx, row_idx, next_row_idx))

            # 2 rows are the same except 2 cells
            if len(different_positions) == 2:
                for col_idx, i, j in different_positions:
                    if input_arr[i][col_idx] != 0 and input_arr[j][col_idx] == 0:
                        tiles = [1, 2]
                        tiles.pop(tiles.index(input_arr[i][col_idx]))
                        input_arr[j][col_idx] = tiles[0]
                    elif input_arr[j][col_idx] != 0 and input_arr[i][col_idx] == 0:
                        tiles = [1, 2]
                        tiles.pop(tiles.index(input_arr[j][col_idx]))
                        input_arr[i][col_idx] = tiles[0]

    return input_arr


def print_two_dimensional_arr(arr):
    for row in arr:
        print(row)
    print("\n")


def is_game_solved(input_arr):
    for row in input_arr:
        for num in row:
            if num == 0:
                return False
    return True


print_two_dimensional_arr(solve_game(example_1))
print_two_dimensional_arr(solve_game(example_2))

ex_1_result = [[1, 1, 2, 2],
               [2, 1, 2, 1],
               [1, 2, 1, 2],
               [2, 2, 1, 1]]

ex_2_result = [[1, 1, 2, 1, 1, 2],
               [1, 1, 2, 1, 2, 1],
               [2, 2, 1, 2, 1, 1],
               [1, 2, 1, 2, 1, 2],
               [1, 1, 2, 1, 2, 2],
               [2, 2, 1, 2, 2, 1]]

print("pass" if solve_game(example_1) == ex_1_result else "fail")
print("pass" if solve_game(example_2) == ex_2_result else "fail")
