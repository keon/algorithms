"""
Given the capacity, source and sink of a graph,
computes the maximum flow from source to sink.
Input : capacity, source, sink
Output : maximum flow from source to sink
Capacity is a two-dimensional array that is v*v.
capacity[i][j] implies the capacity of the edge from i to j.
If there is no edge from i to j, capacity[i][j] should be zero.
"""

import queue

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
    # Time Complexity : O(Ef)
    # E is the number of edges and f is the maximum flow in the graph.
    v = len(capacity)
    ret = 0
    flow = [[0]*v for i in range(v)]
    while True:
        visit = [False for i in range(v)]
        tmp = dfs(capacity, flow, visit, v, source, sink)
        if tmp: ret += tmp
        else: break
    return ret

def edmonds_karp(capacity, source, sink):
    # Computes maximum flow from source to sink using BFS.
    # Time complexity : O(V*E^2)
    # V is the number of vertices and E is the number of edges.
    v = len(capacity)
    ret = 0
    flow = [[0]*v for i in range(v)]
    while True:
        tmp = 0
        q = queue.Queue()
        visit = [False for i in range(v)]
        par = [-1 for i in range(v)]
        visit[source] = True
        q.put((source, 1<<63))
        while q.qsize():
            front = q.get()
            idx = front[0]
            f = front[1]
            if idx == sink:
                tmp = f
                break
            for i in range(v):
                if not visit[i] and flow[idx][i] < capacity[idx][i]:
                    visit[i] = True
                    par[i] = idx
                    q.put((i, min(f, capacity[idx][i]-flow[idx][i])))
        if par[sink] == -1: break
        ret += tmp
        p = par[sink]
        idx = sink
        while p != -1:
            flow[p][idx] += tmp
            flow[idx][p] -= tmp
            idx = p
            p = par[p]
    return ret

def dinic_bfs(capacity, flow, level, source, sink):
    # BFS function for Dinic algorithm.
    # Check whether sink is reachable only using edges that is not full.

    v = len(capacity)
    q = queue.Queue()
    q.put(source)
    level[source] = 0
    while q.qsize():
        front = q.get()
        for i in range(v):
            if level[i] == -1 and flow[front][i] < capacity[front][i]:
                level[i] = level[front] + 1
                q.put(i)
    return level[sink] != -1
def dinic_dfs(capacity, flow, level, idx, sink, work, f = 1<<63):
    # DFS function for Dinic algorithm.
    # Finds new flow using edges that is not full.
    if idx == sink:
        return f
    v = len(capacity)
    for work[idx] in range(work[idx], v):
        nxt = work[idx]
        if level[nxt] == level[idx] + 1 and flow[idx][nxt] < capacity[idx][nxt]:
            tmp = dinic_dfs(capacity, flow, level, nxt, sink, work, min(f, capacity[idx][nxt] - flow[idx][nxt])) 
            if tmp > 0:
                flow[idx][nxt] += tmp
                flow[nxt][idx] -= tmp
                return tmp
    return 0
def dinic(capacity, source, sink):
    # Computes maximum flow from source to sink using Dinic algorithm.
    # Time complexity : O(V^2*E)
    # V is the number of vertices and E is the number of edges.
    v = len(capacity)
    flow = [[0]*v for i in range(v)]
    ret = 0
    while True:
        level = [-1 for i in range(v)]
        work = [0 for i in range(v)]
        if not dinic_bfs(capacity, flow, level, source, sink):
            break
        while True:
            tmp = dinic_dfs(capacity, flow, level, source, sink, work)
            if tmp > 0:
                ret += tmp
            else:
                break
    return ret

