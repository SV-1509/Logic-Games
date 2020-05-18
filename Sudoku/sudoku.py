import numpy as np
sudoku =[[0,6,0,7,4,9,0,0,8],
[0,0,0,0,0,0,0,0,0],
[0,8,0,0,5,0,0,0,0],
[0,0,0,0,9,0,0,0,0],
[5,0,0,1,0,0,7,0,0],
[4,0,0,0,7,0,1,3,2],
[0,0,0,8,0,2,0,0,6],
[0,0,0,0,0,0,0,0,4],
[2,0,0,4,0,0,0,0,7]]


def check(x,y,n):
    global sudoku
    for i in range(0,9):
        if sudoku[x][i]==n:
            return False
    for i in range(0,9):
        if sudoku[i][y]==n:
            return False
    xo=(x//3)*3
    yo=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[xo+i][yo+j]==n:
                return False
    return True



def solve():
    global sudoku
    for x in range(9):
        for y in range(9):
            if sudoku[x][y]==0:
                for n in range(1,10):
                    if check(x,y,n):
                        sudoku[x][y]=n
                        solve()
                        sudoku[x][y]=0
                return
    print(np.matrix(sudoku))
    


solve()







