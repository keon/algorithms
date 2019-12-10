'''
The virus was leaked from a laboratory that was studying deadly viruses. 
Fortunately, the virus hasn't spread yet, and you are trying to build a wall in the lab to prevent the virus from spreading.

The laboratory can be represented by a rectangle of size N × M, which is divided into squares of size 1 × 1. 
The laboratory consists of blank spaces and walls which occupy one space.

Some spaces contain a virus that can spread to adjacent spaces vertically and horizontally. 
you must build three new walls exactly.

For example, let's consider the case where a research institute is created below.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

At this time, 0 is blank, 1 is the wall, and 2 is the virus. If no wall is built, the virus can spread to all blanks.

If you set up the walls in 2 rows, 1 column, 1 row 2 columns, 4 rows 6 columns, the map would look like this:

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

After the virus spreads, it looks like this:

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

After building three walls, the area where the virus cannot spread is called a safe area. 
In the map above, the size of the safe area is 27.

Write a program that calculates the maximum value of the safe zone size that can be obtained when the map of lab is given.

The first line gives the map's height N and its width M. (3 ≤ N, M ≤ 8)

From the second line on, N lines are given the shape of the map. 0 is blank, 1 is the wall, 2 is the location of the virus. 
The number of two is a natural number greater than or equal to two and less than or equal to ten.

The number of blanks is three or more.

ex 1)

input:
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

output:
27

ex 2)

input:
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

output:
9

ex 3)

input:
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

output:
3

'''

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False]*m for _ in range(n)]
v, safe, virus = [], -3, 100

def dfs(x, y):
    res = 1
    c[x][y] = True
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not (c[nx][ny] or a[nx][ny]):
            res += dfs(nx, ny)
    return res

def solve(wall, x, y):
    global virus, c
    if wall == 3:
        cnt = 0
        c = [[False]*m for _ in range(n)]
        for i, j in v:
            cnt += dfs(i, j)
        virus = min(virus, cnt)
        return
    for i in range(x, n):
        k = y if i == x else 0
        for j in range(k, m):
            if a[i][j] == 0:
                a[i][j] = 1
                solve(wall+1, i, j+1)
                a[i][j] = 0

for i in range(n):
    for j in range(m):
        if a[i][j] != 1:
            safe += 1
        if a[i][j] == 2:
            v.append((i, j))
solve(0, 0, 0)
print(safe-virus)
