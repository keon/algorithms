"""
It's similar to how human solve Sudoku.

create a hash table (dictionary) val to store possible values in every location.
Each time, start from the location with fewest possible values, choose one value
from it and then update the board and possible values at other locations.
If this update is valid, keep solving (DFS). If this update is invalid (leaving
zero possible values at some locations) or this value doesn't lead to the
solution, undo the updates and then choose the next value.
Since we calculated val at the beginning and start filling the board from the
location with fewest possible values, the amount of calculation and thus the
runtime can be significantly reduced:


The run time is 48-68 ms on LeetCode OJ, which seems to be among the fastest
python solutions here.


The PossibleVals function may be further simplified/optimized, but it works just
fine for now. (it would look less lengthy if we are allowed to use numpy array
for the board lol).
"""

def solveSudoku(self, board):
    self.board = board
    self.val = self.PossibleVals()
    self.Solver()

def PossibleVals(self):
    a = "123456789"
    d, val = {}, {}
    for i in xrange(9):
        for j in xrange(9):
            ele = self.board[i][j]
            if ele != ".":
                d[("r", i)] = d.get(("r", i), []) + [ele]
                d[("c", j)] = d.get(("c", j), []) + [ele]
                d[(i//3, j//3)] = d.get((i//3, j//3), []) + [ele]
            else:
                val[(i,j)] = []
    for (i,j) in val.keys():
        inval = d.get(("r",i),[])+d.get(("c",j),[])+d.get((i/3,j/3),[])
        val[(i,j)] = [n for n in a if n not in inval ]
    return val

def Solver(self):
    if len(self.val)==0:
        return True
    kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
    nums = self.val[kee]
    for n in nums:
        update = {kee:self.val[kee]}
        if self.ValidOne(n, kee, update): # valid choice
            if self.Solver(): # keep solving
                return True
        self.undo(kee, update) # invalid choice or didn't solve it => undo
    return False

def ValidOne(self, n, kee, update):
    self.board[kee[0]][kee[1]] = n
    del self.val[kee]
    i, j = kee
    for ind in self.val.keys():
        if n in self.val[ind]:
            if ind[0]==i or ind[1]==j or (ind[0]/3,ind[1]/3)==(i/3,j/3):
                update[ind] = n
                self.val[ind].remove(n)
                if len(self.val[ind])==0:
                    return False
    return True

def undo(self, kee, update):
    self.board[kee[0]][kee[1]]="."
    for k in update:
        if k not in self.val:
            self.val[k]= update[k]
        else:
            self.val[k].append(update[k])
    return None
