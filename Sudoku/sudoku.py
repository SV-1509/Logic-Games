import sudoku_solver as s
import sudoku_maker as m
import numpy as np 
puzzle=m.puzzle(66)
print(np.matrix(puzzle))
s.sudoku=puzzle
print("solution")
ans=s.ans()
print(np.matrix(ans))