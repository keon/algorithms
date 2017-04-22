'''
Computes Max-Flow in a network graph using Ford-Fulkerson Algorithm
A BFS is used for augment path
Arguments:
    cap - capacity 2d array of N*N
    source - 0 indexed source node
    sink - 0 indexed sink node
'''

import queue

def max_flow(cap,source,sink):
    def augment_flow(cap,source,sink):
        q = queue.Queue()
        q.put(source)
        par = [-1 for x in range(len(cap))]
        while(not q.empty()):
            src = q.get()
            for to in range(len(cap)):
                if cap[src][to] and par[to]==-1:
                    par[to] = src
                    if to == sink:
                        break
                    q.put(to)
                if to == sink:
                    break
        if par[sink] == -1:
            return False
        track = sink
        parent = par[sink]
        while(par[parent]!=-1):
            cap[parent][track] -= 1
            cap[track][parent] += 1
            track = parent
            parent = par[track]
        return True

    flow = 0
    while(augment_flow(cap,source,sink)):
        flow += 1
    return flow

'''
Example:
cap = [[0,10,5,0],[0,0,15,5],[0,0,0,10],[0,0,0,0]]
max_flow(cap,0,3)
'''
