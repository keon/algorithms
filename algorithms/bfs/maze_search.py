'''
do BFS from (0,0) of the grid and get the minimum number of steps needed to get to the lower right column

only step on the columns whose value is 1

if there is no path, it returns -1
'''

def bfs(grid):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    n = len(grid)
    m = len(grid[0])
    q = [(0,0,0)]
    visit[[0]*m for _ in range(n)]
    if grid[0][0] == 0:
        print("-1")
        return
    visit[0][0] = 1
    while q:
        i, j, step = q.pop(0)
        if i == n-1 and j == m-1:
            print(step)
            return
        for dir in range(4):
            x = i + dx[dir]
            y = j + dy[dir]
            if x>=0 and x<n and y>=0 and y<m:
                if grid[x][y] ==1 and visit[x][y] == 0:
                    visit[x][y] = 1
                    q.append((x,y,step+1))
    print("-1")
