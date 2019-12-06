"""
Given the capacity, source and sink of a graph,
computes the maximum flow from source to sink.
Input : capacity, source, sink
Output : maximum flow from source to sink
Capacity is a two-dimensional array that is v*v.
capacity[i][j] implies the capacity of the edge from i to j.
If there is no edge from i to j, capacity[i][j] should be zero.
"""

def dfs(capacity, flow, visit, v, idx, sink, f = 1<<63):
    # DFS function for ford_fulkerson algorithm.
    if idx == sink: return f
    visit[idx] = True
    for i in range(v):
        if not visit[i] and flow[idx][i] < capacity[idx][i]:
            tmp = dfs(capacity, flow, visit, v, i, sink, min(f, capacity[idx][i]-flow[idx][i]))
            if tmp:
                flow[idx][i] += tmp
                flow[i][idx] -= tmp
                return tmp
    return 0

def ford_fulkerson(capacity, source, sink):
    # Computes maximum flow from source to sink using DFS.
    v = len(capacity)
    ret = 0
    flow = [[0]*v for i in range(v)]
    while True:
        visit = [False for i in range(v)]
        tmp = dfs(capacity, flow, visit, v, source, sink)
        if tmp: ret += tmp
        else: break
    return ret

