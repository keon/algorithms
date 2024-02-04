grid = []
m, n = len(grid), len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def isValid(a, b):
    return 0 <= a < m and 0 <= b < n and grid[a][b] == 1
seen = set()
def dfs(q):
    this = []
    while q:
        ri, cj = q.pop()
        if (ri, cj) in seen: continue
        this.append((ri, cj))
        seen.add((ri, cj))
        for i, j in directions:
            nr, nc = ri + i, cj + j
            if isValid(nr, nc): q.append((nr, nc))
    return this