import random as rd

# need to address the issue of repeating numbers in columns (likely use a for loop)


def create_board(game_board):
    """Creates a board with random #s to build new board every game"""

    randomizer = rd.random()

    for row in game_board:
        if randomizer < .33:
            row[rd.randint(0, 2)] = (rd.randint(1, 9))
        randomizer = rd.random()

    for row in game_board:
        if randomizer < .33:
            row[rd.randint(3, 5)] = (rd.randint(1, 9))
        randomizer = rd.random()

    for row in game_board:
        if randomizer < .33:
            row[rd.randint(6, 8)] = (rd.randint(1, 9))
        randomizer = rd.random()

    for row in game_board:
        print(row)

    print('\n')


# need to build function to begin inputting moves

cols = ['  ', 1, 2, 3, 4, 5, 6, 7, 8, 9]

row_a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_b = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_c = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_d = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_e = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_f = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_g = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_h = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_i = [0, 0, 0, 0, 0, 0, 0, 0, 0]

board = [row_a, row_b, row_c, row_d,
         row_e, row_f, row_g, row_h, row_i]

create_board(board)

row_a = ['1', row_a]
row_b = ['2', row_b]
row_c = ['3', row_c]
row_d = ['4', row_d]
row_e = ['5', row_e]
row_f = ['6', row_f]
row_g = ['7', row_g]
row_h = ['8', row_h]
row_i = ['9', row_i]

board = [cols, row_a, row_b, row_c, row_d,
         row_e, row_f, row_g, row_h, row_i]

for row in board:
    print(row)
