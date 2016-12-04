import collections

## do BFS from each building, and decrement all empty place for every building visit
## when grid[i][j] == -b_nums, it means that grid[i][j] are already visited from all b_nums
## and use dist to record distances from b_nums
def shortest_distance(grid):
    if not grid or not grid[0]:
        return -1

    matrix = [[[0,0] for i in range(len(grid[0]))] for j in range(len(grid))]

    cnt = 0    # count how many building we have visited
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                bfs([i,j], grid, matrix, cnt)
                cnt += 1

    res = float('inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j][1]==cnt:
                res = min(res, matrix[i][j][0])

    return res if res!=float('inf') else -1

def bfs(start, grid, matrix, cnt):
    q = [(start, 0)]
    while q:
        tmp = q.pop(0)
        po, step = tmp[0], tmp[1]
        for dp in [(-1,0), (1,0), (0,1), (0,-1)]:
            i, j = po[0]+dp[0], po[1]+dp[1]
            # only the position be visited by cnt times will append to queue
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and matrix[i][j][1]==cnt and grid[i][j]==0:
                matrix[i][j][0] += step+1
                matrix[i][j][1] = cnt+1
                q.append(([i,j], step+1))

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(shortest_distance(grid))
