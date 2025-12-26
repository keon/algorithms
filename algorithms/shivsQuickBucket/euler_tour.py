from collections import defaultdict as dd

def eulerTour(u, index):
    seen[u] = True
    Euler[index] = u
    index += 1
    for nei in adj[u]:
        if not seen[u]:
            index = eulerTour(nei, index)
            Euler[index] = u
            index += 1
    return index
n = 10 # No. of nodes
seen = dd(bool)
adj = dd(list)
Euler = [0] * (2 * (10 ** 5))
eulerTour(1, 0)
for i in range(2 * n - 1):
    print(Euler[i], end = "  ")

# Another way for this - 

def Euler(node):
    tin[node] = timer
    timer += 1
    path[tin[node]] = node
    for child in adj[node]:
        Euler(child)
    tout[node] = timer - 1

tin, tout = [0] * (n + 1), [0] * (n + 1)
path = [0] * (n + 1)
