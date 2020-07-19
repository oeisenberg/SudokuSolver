# SudokuSolver

## What is Sudoku?
Sudoku appeared in Japan in 1984 [[1]](https://sudoku.com/how-to-play/the-history-of-sudoku/) and revolves around the distinct placement of the digits 1-9 within rows, columns and 3x3 squares which form a 9x9 grid.

Varients of Sudoku exist to add further challenge via the addition of further constraints. More information can be found here [here](https://en.wikipedia.org/wiki/Sudoku) on the Sudoku Wikipage.

## How does this code work?
The code solves Sudoku puzzles using depth-first search with backtracking. Along side the puzzle a 2D 'whitelist' array is initialised which contains valid numbers for each grid square. The possible values can be visualised as horizontal nodes within the DFS tree, if this tree is traversed to a node of _-1_ then a different value is chosen for the parent node.

## Comments
The purpose is of this publication is to demonstrate projects that I have completed during my time at university and not to provide a platform for existing students to take inspiration from.

## Excecution
The `main.py` file imports the sudoku solver and passes a puzzle in the form of a 2D numpy array.
