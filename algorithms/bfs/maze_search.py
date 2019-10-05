'''
BFS time complexity : O(|E|)
BFS space complexity : O(|V|)

do BFS from (sx,sy) (default: (0, 0)), of the grid and get the minimum number of steps needed to get to (ex, ey)(default: the lower right column)

only step on the columns whose value is 1

if there is no path, it returns -1

Ex 1)
If grid is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]], 
Start at (0, 0), and End at (the lower right column)
the answer is: 14

Ex 2)
If grid is
[[1,0,0],
 [0,1,1],
 [0,1,1]],
Start at (0, 0), and End at (the lower right column)
the answer is: -1
'''

def maze_search(grid, sx=0, sy=0, ex=-1, ey=-1):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    n = len(grid)
    m = len(grid[0])
    if ex==-1 or ey==-1:
        ex = n-1
        ey = m-1
    q = [(sx, sy,0)]
    visit = [[0]*m for _ in range(n)]
    if grid[0][0] == 0:
        return -1
    visit[0][0] = 1
    while q:
        i, j, step = q.pop(0)
        if i == ex and j == ey:
            return step
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if x>=0 and x<n and y>=0 and y<m:
                if grid[x][y] ==1 and visit[x][y] == 0:
                    visit[x][y] = 1
                    q.append((x,y,step+1))
    return -1
