'''
Find shortest path from top left column to the right lowest column using DFS.
only step on the columns whose value is 1
if there is no path, it returns -1

Ex 1)
If maze is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]],
the answer is: 14

Ex 2)
If maze is
[[1,0,0],
 [0,1,1],
 [0,1,1]],
the answer is: -1
'''

global cnt
global directions
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def find_path(maze):
    global cnt
    cnt = -1

    dfs(maze, 0, 0, 0)
    return cnt


def dfs(maze, i, j, depth):
    global directions
    global cnt

    row = len(maze)
    col = len(maze[0])

    if i == row - 1 and j == col - 1:
        if cnt == -1:
            cnt = depth
        else:
            if cnt > depth:
                cnt = depth
        return

    maze[i][j] = 0

    for k in range(len(directions)):
        nx_i = i + directions[k][0]
        nx_j = j + directions[k][1]

        if nx_i >= 0 and nx_i < row and nx_j >= 0 and nx_j < col:
            if maze[nx_i][nx_j] == 1:
                dfs(maze, nx_i, nx_j, depth + 1)

    maze[i][j] = 1

    return
