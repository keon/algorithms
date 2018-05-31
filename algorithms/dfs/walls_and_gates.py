

# fill the empty room with distance to its nearest gate


def walls_and_gates(rooms):
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                dfs(rooms, i, j, 0)


def dfs(rooms, i, j, depth):
    if (i < 0 or i >= len(rooms)) or (j < 0 or j >= len(rooms[0])):
        return  # out of bounds
    if rooms[i][j] < depth:
        return  # crossed
    rooms[i][j] = depth
    dfs(rooms, i+1, j, depth+1)
    dfs(rooms, i-1, j, depth+1)
    dfs(rooms, i, j+1, depth+1)
    dfs(rooms, i, j-1, depth+1)
