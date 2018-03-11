#Sodoku
import time
import numpy as np

t0 = time.time()

sudoku = np.array([[0, 0, 0, 6, 0, 0, 2, 8, 7],
                  [0, 0, 0, 0, 3, 0, 5, 0, 1],
                  [0, 0, 0, 8, 0, 5, 6, 0, 4],
                  [5, 9, 0, 0, 0, 0, 4, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 3],
                  [0, 0, 4, 0, 0, 0, 0, 7, 5],
                  [6, 0, 8, 1, 0, 2, 0, 0, 0],
                  [3, 0, 7, 0, 4, 0, 0, 0, 0],
                  [2, 4, 0, 0, 0, 3, 0, 1, 0]
                   ])

# sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 9],
#           [1, 2, 3, 4, 5, 6, 7, 8, 0],
#           ]


def sudoku_solver(sudoku):
    temp_sudoku = sudoku.copy()
    possible_array_str = np.zeros((len(temp_sudoku[0]), len(temp_sudoku)))
    for y in range(0, 9):
        for x in range(0, 9):
            if temp_sudoku[y][x] == 0:
                possible_values = possible_values_checker(temp_sudoku, x, y)
                if len(possible_values) == 0:
                    print("impossible")
                    return temp_sudoku
                if len(possible_values) == 1:
                    temp_sudoku[y][x] = possible_values[0]

                possible_values_str = ''.join(map(str, possible_values))
                possible_array_str[y][x] = possible_values_str

    print(possible_array_str.astype(int))   # To be removed later

    # Now traverse all nodes using depth first search
    for y in range(0, 1):
        for x in range(0, 9):
            j = 0
            k = 0
            if sudoku[y][x] == 0:           # If not a set integer in the sudoku...
                if temp_sudoku[y][x] == 0:  # If not changed the value before start at 0
                    new_index = 0
                    numb_to_add = int(str(possible_array_str[y][x])[new_index])
                    index = get_index(numb_to_add, ''.join(map(str, possible_values_checker(temp_sudoku, x, y))))
                    if index != -1:
                        temp_sudoku[y][x] = numb_to_add
                    else:
                        # If all values are exhasted go back and recurse
                        try:
                            while index == -1 and new_index <= len(str(possible_array_str[y][x])):
                                new_index = new_index + 1
                                numb_to_add = int(str(possible_array_str[y][x])[new_index])
                                index = get_index(numb_to_add,
                                                  ''.join(map(str, possible_values_checker(temp_sudoku, x, y))))
                                if index != -1:
                                    print("adding", numb_to_add, x, y)
                                    temp_sudoku[y][x] = numb_to_add
                        except:
                            # print("EXCEPTION")
                            new_index = -1
                            count = 0
                            j = y
                            k = x
                            while new_index == -1:
                                j = backtrack(j, k)[0]
                                k = backtrack(j, k)[1]
                                count = count + 1

                                # If we pass the first square then it must be unsolvable
                                if j == -1 or k == -1:
                                    # print("Invalid")
                                    return temp_sudoku
                                # print(k, j)
                                # Checks if laps if so try previous
                                try:
                                    while index == -1 and new_index <= len(str(possible_array_str[j][k])):
                                        new_index = new_index + 1
                                        numb_to_add = int(str(possible_array_str[j][k])[new_index])
                                        index = get_index(numb_to_add,
                                                          ''.join(map(str, possible_values_checker(temp_sudoku, k, j))))
                                        temp_sudoku = safe_to_add(index, numb_to_add, n, m, temp_sudoku)
                                except:
                                    new_index = -1
                            if count != 0:
                                # print("Moving Forwards")
                                m = j  # y
                                n = k  # x
                                for count in range(0, count):
                                    m = fortrack(m, n)[0]
                                    n = fortrack(m, n)[1]
                                    index = -1
                                    new_index = -1
                                    # print(n, m)
                                    while index == -1 and new_index <= len(str(possible_array_str[m][n])) and sudoku[m][n] == 0:
                                        new_index = new_index + 1
                                        print(str(possible_array_str[m][n]), new_index)
                                        numb_to_add = int(str(possible_array_str[m][n])[new_index])
                                        index = get_index(numb_to_add,
                                                          ''.join(map(str, possible_values_checker(temp_sudoku, n, m))))
                                        temp_sudoku = safe_to_add(index, numb_to_add, n, m, temp_sudoku)

                else:
                    new_index = get_index(temp_sudoku[y+j][x+k], possible_array_str[y+j][x+k]) + 1  # gets current index

    solved_sudoku = temp_sudoku.copy()
    return solved_sudoku


def safe_to_add(index,numb_to_add, n, m, temp_sudoku):
    if index != -1:
        temp_sudoku[m][n] = numb_to_add
    return temp_sudoku


def fortrack(y, x):
    if x <= 7:
        x = x + 1
    else:
        x = 0
        if y <= 7:
            y = y + 1
        else:
            return [-1, -1]
    return [y, x]


def backtrack(y, x):
    if x >= 1:
        x = x - 1
    else:
        x = 8
        if y >= 1:
            y = y - 1
        else:
            return [-1, -1]
    return [y, x]


def possible_values_checker(temp_sudoku, x, y):
    # check for all possible values (create a tree)
    possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_values = row_checker(temp_sudoku[y], possible_values)  # check the row
    possible_values = col_checker(column(temp_sudoku, x), possible_values)  # check the col
    # print("C", possible_values)
    possible_values = unit_checker(unit_square_builder(y, x), possible_values)  # check the unit square
    # print("U", possible_values)
    return possible_values


def get_index(cur_value, possible_values_str):
    possible_values_str = str(possible_values_str)
    # print(possible_values_str, len(possible_values_str), cur_value)
    for i in range(0, len(possible_values_str)):
        if int(possible_values_str[i]) == cur_value:
            if len(possible_values_str) >= i:
                return i
    return -1


def column(matrix, i):
    return [row[i] for row in matrix]


def unit_square_builder(y, x):
    local_y = y % 3
    local_x = x % 3

    y = y - local_y
    x = x - local_x

    unit = [[sudoku[y][x], sudoku[y][x + 1], sudoku[y][x + 2]],
            [sudoku[y + 1][x], sudoku[y + 1][x + 1], sudoku[y + 1][x + 2]],
            [sudoku[y + 2][x], sudoku[y + 2][x + 1], sudoku[y + 2][x + 2]]]
    return unit


def matches(value):
    for z in range(1, 10):  # range of correct possible values is 1 to 9
        if value == z:
            return z
    return -1


def row_checker(row, possible_values):

    for x in range(0, len(row)):
        z = matches(row[x])
        if z >= 1:
            try:
                possible_values.remove(z)
            except:
                pass
    return possible_values


def col_checker(col, possible_values):
    for y in range(0, len(col)):
        z = matches(col[y])
        if z >= 1:
            try:
                possible_values.remove(z)
            except:
                pass
    return possible_values


def unit_checker(unit, possible_values):
    for y in range(0, 3):
        for x in range(0, 3):
            z = matches(unit[y][x])
            if z >= 1:
                try:
                    possible_values.remove(z)
                except:
                    pass
    return possible_values


final_sudoku = sudoku_solver(sudoku)

t1 = time.time()
total = t1-t0

print(final_sudoku)
print(total)
