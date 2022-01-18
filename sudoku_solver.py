#Not optimized for professional use, performance or readibility yet.
import numpy as np

def sudoku_solver(sudoku):
    if sudoku.size == 0:
        return sudoku
    invalid_inputs = []
    for rindex in range(9):
        for cindex in range(9):
            if sudoku[rindex][cindex] == 0:
                invalid_inputs = search_invalid_inputs(sudoku, rindex, cindex, invalid_inputs)
                inputs = np.array([x for x in range(1,10) if x not in invalid_inputs])
                if inputs.size == 0:
                    return np.array([])
                for attempt in inputs:
                    solved_sudoku = sudoku.copy()
                    solved_sudoku[rindex][cindex] = attempt
                    solved_sudoku = sudoku_solver(solved_sudoku)
                    if solved_sudoku.size != 0:
                        return solved_sudoku
                return solved_sudoku
    return sudoku

def search_invalid_inputs(sudoku, rindex, cindex, invalid_inputs):
    for col in range(9):
        if sudoku[rindex][col] not in invalid_inputs:
            invalid_inputs.append(sudoku[rindex][col])
    for row in range(9):
        if sudoku[row][cindex] not in invalid_inputs:
            invalid_inputs.append(sudoku[row][cindex])
    invalid_inputs = search_invalid_block(sudoku, rindex, cindex, invalid_inputs)
    return invalid_inputs
    
def search_invalid_block(sudoku, rindex, cindex, invalid_inputs):
    cblock = (cindex//3) * 3
    rblock = (rindex//3) * 3
    for col in range(cblock, cblock+3):
        for row in range(rblock, rblock+3):
            if sudoku[row][col] not in invalid_inputs:
                invalid_inputs.append(sudoku[row][col])
    return invalid_inputs



puzzle  = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0], 
    [0, 9, 8, 0, 0, 0, 0, 6, 0], 
    [8, 0, 0, 0, 6, 0, 0, 0, 3], 
    [4, 0, 0, 8, 0, 3, 0, 0, 1], 
    [7, 0, 0, 0, 2, 0, 0, 0, 6], 
    [0, 6, 0, 0, 0, 0, 2, 8, 0], 
    [0, 0, 0, 4, 1, 9, 0, 0, 5], 
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

solved = puzzle.copy()

print(sudoku_solver(solved))
