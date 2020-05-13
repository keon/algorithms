import heapq  # for priority queue

# input number of nodes and edges in graph
n, e = map (int,input().split())

# initializing empty graph as a dictionary (of the form {int:list})
g = dict (zip ([i for i in range(1,n+1)],[[] for i in range(n)]))

# input graph data
for i in range(e):
    a, b, c = map (int,input().split())
    g[a].append([c,b])
    g[b].append([c,a])
    
vis = []
s = [[0,1]]
prim = []
mincost = 0

# prim's algo. to find weight of minimum spanning tree
while (len(s)>0):
    v = heapq.heappop(s)
    x = v[1]
    if (x in vis):
        continue

    mincost += v[0]
    prim.append(x)
    vis.append(x)

    for j in g[x]:
        i = j[-1]
        if(i not in vis):
            heapq.heappush(s,j)

print(mincost)
