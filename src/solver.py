import numpy as np

class sudoku_solver():

    def __init__(self):
        self.invalid_puzzle = np.full((9, 9), -1)
    
    # Creates a list that contains a list of possible values for each square
    def _create_whitelist(self, puzzle):
        whitelist_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            ]

        for y in range(0, 9):
            for x in range(0, 9):
                if puzzle[y][x] == 0:
                    possible_values = self._check_all_possible_values(puzzle, x, y)
                    # if -1 is returned return the invalid puzzle
                    if int(possible_values[0]) == -1:
                        return self.invalid_puzzle

                    whitelist_array[y][x] = ''.join(map(str, possible_values))
                else:
                    whitelist_array[y][x] = puzzle[y][x]
        return whitelist_array

    def _solved(self, puzzle, whitelist):
        # Re-formats the data from the whitelist array to a list
        def get_possible_values_list(whitelist_array, col, row):
            possible_values_list = []
            for i in range(0, len(str(whitelist_array[row][col]))):
                possible_values_list.append(str(whitelist_array[row][col])[i])
            return possible_values_list

        # Checks the location to get a new list of accepted inputs
        def check_if_location_is_safe(puzzle, row, col, num):
            values = self._check_all_possible_values(puzzle, col, row)
            if num in values:
                return True
            return False

        # Finds the next empty square in the sudoku puzzle.
        def find_next_square(puzzle, location):
            for col in range(9):
                for row in range(9):
                    if puzzle[row][col] == 0:
                        location[0] = row
                        location[1] = col
                        return True
            # All squares are full, puzzle completed
            return False

        location = [0, 0]
        if not find_next_square(puzzle, location):
            return True
        row = location[0]
        col = location[1]
        poss_puzzle = get_possible_values_list(whitelist, col, row)

        for i in range(0, len(poss_puzzle)):
            num = int(poss_puzzle[i])
            if check_if_location_is_safe(puzzle, row, col, num):
                puzzle[row][col] = num
                if self._solved(puzzle, whitelist):
                    return True
                puzzle[row][col] = 0
        return False

    def _check_all_possible_values(self, puzzle, x, y):

        # Checks all integers within the row/column
        def data_checker(data, possible_values):
            for i in range(9):
                if data[i] >= 1:
                    try:
                        possible_values.remove(data[i])
                    except:
                        pass
            return possible_values
        
        # Checks all integers within the unit square
        def unit_checker(unit_square, possible_values):
            for y in range(0, 3):
                for x in range(0, 3):
                    try:
                        possible_values.remove(unit_square[y][x])
                    except:
                        pass
            return possible_values

        # Builds a unit square by first finding the coordinates of the first square
        def unit_square_builder(y, x, question):
            local_y = y % 3
            local_x = x % 3

            y = y - local_y
            x = x - local_x

            unit_square = [[question[y][x], question[y][x + 1], question[y][x + 2]],
                        [question[y + 1][x], question[y + 1][x + 1], question[y + 1][x + 2]],
                        [question[y + 2][x], question[y + 2][x + 1], question[y + 2][x + 2]]]
            return unit_square

        # Retrives the column of a given array
        def column(puzzle, i):
            return [row[i] for row in puzzle]

        possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        possible_values = data_checker(puzzle[y], possible_values)
        possible_values = data_checker(column(puzzle, x), possible_values)
        possible_values = unit_checker(unit_square_builder(y, x, puzzle), possible_values)

        if not possible_values:
            possible_values = [-1]

        return possible_values

    def solve(self, puzzle):
        whitelist = self._create_whitelist(puzzle)
        if -1 in whitelist:
            return self.invalid_puzzle
        else:
            if not self._solved(puzzle, whitelist):
                return self.invalid_puzzle
        return puzzle