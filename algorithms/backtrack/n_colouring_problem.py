def isSafe(graph, m, v):  # For checking whether this node can be colored with m or not
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and col[i] == m:
            return False
    return True


def solve(graph, m, v):
    if v >= 4:
        return True
    else:
        for i in range(m):
            if isSafe(graph, i, v):
                col[v] = i
                if solve(graph, m, v + 1):
                    return True
                col[v] = -1
    return False


# Can consider any graph
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]

# initialise color with -1
col = [-1 for i in range(4)]

# Number of different colors allowed
m = int(input("Enter number of different colors"))

if solve(graph, m, 0):
    print("Solution Exists: Following are the assigned colors")
    for i in col:
        print(i),
    print()
else:
    print("No Solution Exists")
    
# By cosmos
