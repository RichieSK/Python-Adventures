#Program to solve the N Queen problem.
#Unoptimized for readability, performance and use.
import numpy as np

def nqueen_solver(n):
    board = np.array([np.zeros(n) for x in range(n)])
    board = nqueen_row_solver(board, n, 0)
    return board

def nqueen_row_solver(board, n, row):
    if row == n:
        return board
    for col in range(n):
        solved_board = board.copy()
        solved_board[row][col] = 1
        if cell_is_valid(solved_board, n, row, col):
            solved_board = nqueen_row_solver(solved_board, n, row+1)
            if solved_board is not None:
                return solved_board
        else:
            solved_board = None
    return solved_board

def cell_is_valid(board, n, rindex, cindex):
    if np.sum(board[rindex]) != 1:
        print(board)
        return False
    if np.sum(board[:,cindex]) != 1:
        return False
    row, col = rindex, cindex
    if col >= row:
        col -= row
        row = 0
    else:
        row -= col
        col = 0
    while row < n and col < n:
        if row != rindex:
            if board[row][col] == 1:
                return False
        row += 1
        col += 1
    row, col = rindex, cindex
    while row > 0 and col < n-1:
        row -= 1
        col += 1
    while row < n and col >= 0:
        if row != rindex:
            if board[row][col] == 1:
                # print("False 4")
                return False
        col -= 1
        row += 1
    return True

print(nqueen_solver(8))
