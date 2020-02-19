"""
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

(More info at: http://en.wikipedia.org/wiki/Sudoku)
"""

# Using dict/hash-table
from collections import defaultdict

def valid_solution_hashtable(board):
    for i in range(len(board)):
        dict_row = defaultdict(int)
        dict_col = defaultdict(int)
        check_valid_value(board)
    if not check_addition(board):
        return False
    #if everything is right
    return True

def check_valid_value(board):
    for j in range(len(board[0])):
        value_row = board[i][j]
        value_col = board[j][i]
        if not value_row or value_col == 0:
            return False
        if value_row in dict_row:
            return False
        else:
            dict_row[value_row] += 1

        if value_col in dict_col:
            return False
        else:
            dict_col[value_col] += 1
    return board

def check_addition(board):
    for i in range(3):
        for j in range(3):
            grid_add = 0
            for k in range(3):
                for l in range(3):
                    grid_add += board[i*3+k][j*3+l]
            if grid_add != 45:
                return False
    return True
   