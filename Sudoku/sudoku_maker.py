#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
grid=[]
sudoku=[]
arr=[0,1,2,3,4,5,6,7,8]
arr1=[]


# In[2]:


def check(x,y,n):
    global grid
    for i in range(0,9):
        if grid[x][i]==n:
            return False
    for i in range(0,9):
        if grid[i][y]==n:
            return False
    xo=(x//3)*3
    yo=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[xo+i][yo+j]==n:
                return False
    return True


# In[3]:


def create():
    global it,sudoku,grid,arr1
    while it == True:
        
        for x in arr:
            for y in arr1:
                if grid[x][y]==0:
                    for n in range(1,10):
                        if check(x,y,n):
                            grid[x][y]=n
                            create()
                            grid[x][y]=0
                    return
        it = False
        for x in range(9):
            q=[]
            for y in range(9):
                q.append(grid[x][y])
            sudoku.append(q)


# In[4]:


def puzzle(diff):
    global arr1,grid,sudoku,it
    it=True
    grid =[[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]
    sudoku=[]
    
    arr1=random.sample(arr,9)
    create()
    for i in range(diff):
            x=random.randint(0,8)
            y=random.randint(0,8)
            sudoku[x][y]=0
    return sudoku


# In[5]:





# In[ ]:





# In[ ]:




