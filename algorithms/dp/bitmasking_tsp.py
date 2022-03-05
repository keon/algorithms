import math

MAX_ROW = 12
MAX_COLUMN = 12
MAX_HOUSE = 12

# neighbor nodes position
D_X = [-1, 0, 0, 1]
D_Y = [0, 1, -1, 0]

"""
Check that the given nodes is valid

:param nodes: The nodes to check
:param nbRow: The number of rows
:param nbColumn: The number of columns
:returns: Nothing but raises error if invalid nodes
"""
def check_argument(nodes: list, nbRow: int, nbColumn: int):
    if len(nodes) != nbRow:
        raise ValueError(f'The number of rows in nodes ({len(nodes)}) does not match the given number of row: {nbRow} !')
    for row in nodes:
        if not isinstance(row, list):
            raise ValueError(f'The given row {row} is not valid !')
        if len(row) != nbColumn:
            raise ValueError(f'The number of columns in row {row} does not match the given number of column: {nbColumn} !')
        for node in row:
            if node != '.' and node != '*' and node != '#':
                raise ValueError(f'The given node "{node}" in row {row} is not valid !')

"""
Check if the given position is valid

:param nodes: The nodes
:param nbRow: The number of rows
:param nbColumn: The number of columns
:returns: True if the position is valid, False otherwise
"""
def is_safe_pos(nodes: list, nbRow: int, nbColumn: int, r: int, c: int):
    return r >= 0 and r < nbRow and c >= 0 and c < nbColumn and nodes[r][c] != '#'


"""
Compute all the distances from the given house to all nodes using BFS

:param nodes: The nodes
:param houses: The houses location
:param nbRow: The number of rows
:param nbColumn: The number of columns
:param dist: All distances
:param index: The house index
:returns: Nothing 
"""
def getDist(nodes: list, houses: list, nbRow: int, nbColumn: int, dist: list, index: int):
    
    visited = [[False for c in range(nbColumn)] for r in range(nbRow)]

    curr_row = houses[index][0]
    curr_col = houses[index][1]

    queue = [[curr_row, curr_col]]
    visited[curr_row][curr_col] = True
    dist[curr_row][curr_col][index] = 0

    while queue != []:
        pos = queue.pop(0)
        # iterate on all 4 neighbors
        for dir in range(4):
            curr_row = pos[0] + D_X[dir]
            curr_col = pos[1] + D_Y[dir]
            # check if the neighbor is a valid node
            if is_safe_pos(nodes, nbRow, nbColumn, curr_row, curr_col):
                if not visited[curr_row][curr_col]:
                    visited[curr_row][curr_col] = True
                    dist[curr_row][curr_col][index] = dist[pos[0]][pos[1]][index] + 1
                    queue.append([curr_row, curr_col])

"""
Compute all the distances from all houses to all nodes

:param nodes: The nodes
:param houses: The houses location
:param nbRow: The number of rows
:param nbColumn: The number of columns
:returns: All the distances
"""
def getAllDist(nodes: list, houses: list, nbRow: int, nbColumn: int):

    dist = [[[math.inf for house in range(len(houses))] for column in range(nbColumn)] for row in range(nbRow)]

    for index in range(len(houses)):
        getDist(nodes, houses, nbRow, nbColumn, dist, index)

    return dist

"""
Initialize the variables

:param nodes: The nodes given
:param nbRow: The number of rows
:param nbColumn: The number of columns
"""
def initialization(nodes: list, nbRow: int, nbColumn: int):

    # check if the arguments are valid
    check_argument(nodes, nbRow, nbColumn)

    # add starting point as "house"
    houses = [[0, 0]]

    # get all houses
    for i in range(nbRow):
        for j in range(nbColumn):
            if nodes[i][j] == '*':
                houses.append([i, j])
    
    # check the number of houses
    if len(houses) > MAX_HOUSE:
        raise ValueError(f'The maximum number of houses is {MAX_HOUSE}, but you gave {len(houses)} houses !')
    
    # initialize the DP matrix
    DP = [[-1 for mask in range(2 ** len(houses))] for i in range(len(houses))]
    
    # compute all distances
    dist = getAllDist(nodes, houses, nbRow, nbColumn)

    return houses, DP, dist

"""
Find the shortest path

:param houses: The houses location
:param DP: The DP matrix
:param dist: All distances
:param index: The house index
:param mask: The current mask
:returns: The shortest path
"""
def find_shortest_path(houses: list, DP: list, dist: list, index: int, mask: int):

    # if the mask is full, then we found a path
    if mask == (1 << len(houses)) - 1:
        return dist[0][0][index]
    
    # if this subproblem has already been computed, just return the solution
    if DP[index][mask] != -1:
        return DP[index][mask]
    
    minDist = math.inf

    for index_ in range(len(houses)):
        if not (mask & (1 << index_)):
            minDist = min(
                minDist,
                find_shortest_path(houses, DP, dist, index_, mask | (1 << index_)) + dist[houses[index_][0]][houses[index_][1]][index]
            )
    
    # store the result in the DP matrix
    DP[index][mask] = minDist

    return DP[index][mask]

"""
Finds the length of the shortest Euler circuit using bitmasking and dynamic programming (DP).
:param nodes: Contains integer tuples of the node coordinates.
:returns: the length of the shortest Euler circuit.
"""
def tsp(nodes: list, nbRow: int, nbColumn: int) -> int:
    
    houses, DP, dist = initialization(nodes, nbRow, nbColumn)

    return find_shortest_path(houses, DP, dist, 0, 1)

# For debugging purposes
def main():
    nodes = [
        ['.', '.', '.', '.', '.', '*', '.'],
        ['.', '.', '.', '#', '.', '.', '.'],
        ['.', '*', '.', '#', '.', '*', '.'],
        ['.', '.', '.', '.', '.', '*', '.']
    ]
    nbRow = 4
    nbColumn = 7
    print(tsp(nodes, nbRow, nbColumn))

if __name__ == '__main__':
    main()