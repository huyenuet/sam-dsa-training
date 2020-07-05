def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

    print()


board = [
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 2, 0],
]

solved_board = [
    [1, 2, 2, 1, 1, 2],
    [2, 1, 2, 1, 2, 1],
    [2, 2, 1, 2, 1, 1],
    [1, 2, 1, 2, 1, 2],
    [1, 1, 2, 1, 2, 2],
    [2, 1, 1, 2, 2, 1],
]


def apply_all_rows(f):
    def wrapper(board):
        for index, row in enumerate(board):
            board[index] = f(row)
        return board

    return wrapper


def transpose(board):
    new_board = []
    for i in range(len(board)):
        new_board.append([])
    for row_index, row in enumerate(board):
        for i in range(len(row)):
            new_board[i].append(row[i])
    return new_board


def rotate_and_apply(f):
    def wrapper(board):
        board = f(board)
        board = transpose(board)

        board = f(board)
        board = transpose(board)

        return board

    return wrapper


@rotate_and_apply
@apply_all_rows
def rule_1(row):
    """
    No three consecutive tiles have the same colour.
    [0, 0, 0, 1, 1, 0] -> [0, 0, 2, 1, 1, 2]
    """
    # check row
    row_len = len(row)
    indices_of_2 = []
    indices_of_1 = []
    for index, num in enumerate(row):
        if num == 1:
            indices_of_1.append(index)
        elif num == 2:
            indices_of_2.append(index)
    i = 0
    while i < len(indices_of_2) and i + 1 < len(indices_of_2):
        # 1. if there are 2 tiles distributed like 2, 0, 2 => 0 should be replaced by 1
        if indices_of_2[i + 1] == indices_of_2[i] + 2:
            row[indices_of_2[i] + 1] = 1

        # 2. if there are 2 consecutive tiles have the same color(2),
        # the next and previous tiles should be the other color(1)
        elif indices_of_2[i + 1] == indices_of_2[i] + 1:
            if indices_of_2[i] + 2 < row_len:
                row[indices_of_2[i] + 2] = 1
            if indices_of_2[i] >= 1:
                row[indices_of_2[i] - 1] = 1
        i += 1

    i = 0
    while i < len(indices_of_1) and i + 1 < len(indices_of_1):
        if indices_of_1[i + 1] == indices_of_1[i] + 2:
            row[indices_of_1[i] + 1] = 2
        elif indices_of_1[i + 1] == indices_of_1[i] + 1:
            if indices_of_1[i] + 2 < row_len:
                row[indices_of_1[i] + 2] = 2
            if indices_of_1[i] >= 1:
                row[indices_of_1[i] - 1] = 2
        i += 1

    return row


@rotate_and_apply
@apply_all_rows
def rule_2(row):
    """
    On each row or column of the grid, the number of red tiles equals to the number of blue ones.
    """
    row_len = len(row)

    # check row
    total_1_tiles = row.count(1)
    total_2_tiles = row.count(2)

    if total_1_tiles == (row_len / 2):
        row = [2 if num == 0 else num for num in row]
    elif total_2_tiles == (row_len / 2):
        row = [1 if num == 0 else num for num in row]
    return row


@rotate_and_apply
def rule_3(board):
    """
    No two rows or columns are the same.
    """
    arr_size = len(board)
    for row_idx in range(0, arr_size - 1):
        for next_row_idx in range(row_idx + 1, arr_size):
            different_tile_indices = []
            for col_idx in range(0, arr_size):
                if (
                    board[row_idx][col_idx] == board[next_row_idx][col_idx] == 0 or
                    board[row_idx][col_idx] != board[next_row_idx][col_idx] != 0
                ):
                    different_tile_indices = []
                    break
                if (
                    (board[row_idx][col_idx] == 0 or board[next_row_idx][col_idx] == 0)
                    and (board[row_idx][col_idx] != board[next_row_idx][col_idx])
                ):
                    different_tile_indices.append((col_idx, row_idx, next_row_idx))

            # 2 rows are the same except 2 cells
            if len(different_tile_indices) == 2:
                for col_idx, i, j in different_tile_indices:
                    if board[i][col_idx] != 0 and board[j][col_idx] == 0:
                        tiles = [1, 2]
                        tiles.pop(tiles.index(board[i][col_idx]))
                        board[j][col_idx] = tiles[0]
                    elif board[j][col_idx] != 0 and board[i][col_idx] == 0:
                        tiles = [1, 2]
                        tiles.pop(tiles.index(board[j][col_idx]))
                        board[i][col_idx] = tiles[0]
    return board


def is_game_solved(input_arr):
    for row in input_arr:
        for num in row:
            if num == 0:
                return False
    return True


def solve_game(board):
    while not is_game_solved(board):
        board = rule_1(board)
        board = rule_2(board)
        board = rule_3(board)
    return board


print("original board: ")
print_board(board)
print("Solved board:")
print_board(solve_game(board))
print("pass" if solve_game(board) == solved_board else "fail")
