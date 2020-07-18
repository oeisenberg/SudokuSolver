import numpy as np
from solver import sudoku_solver

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

ss = sudoku_solver()
print(ss.solve(sudoku))