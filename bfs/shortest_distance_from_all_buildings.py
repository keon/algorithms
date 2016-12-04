import collections

## do BFS from each building, and decrement all empty place for every building visit
## when grid[i][j] == -b_nums, it means that grid[i][j] are already visited from all b_nums
## and use dist to record distances from b_nums

def shortest_distance(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    if not m or not n:
        return -1

    dist = [[0] * n] * m
    b_nums = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1: b_nums+=1
    b_idx = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                bfs(grid, dist, i, j, b_idx)
                b_idx -= 1
    res = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] + b_nums == 0:
                res.append(dist[i][j])
    return min(res) if res else -1

def bfs(grid, dist, i, j, b_idx):
    m = len(grid)
    n = len(grid[0])
    queue = collections.deque([(i, j, 0)])
    while queue:
        i, j, d = queue.popleft()
        for x,y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if 0<=x<m and 0<=y<n and grid[x][y] == b_idx:
                dist[x][y] += d+1
                grid[x][y] -= 1
                queue.append((x, y, d+1))


grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(shortest_distance(grid))
