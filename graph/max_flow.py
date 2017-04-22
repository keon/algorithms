'''
Computes Max-Flow in a network graph using Ford-Fulkerson Algorithm
A DFS is used for augment path
Arguments:
    cap - capacity 2d array of N*N
    source - 0 indexed source node
    sink - 0 indexed sink node
'''

def max_flow(cap,source,sink):
    
    def augment_flow(cap,source,sink,vis=None):
        if vis == None:
            vis = [False for x in range(len(cap))]
        if source==sink:
            return True
        vis[source]=True
        for to in range(len(cap)):
            if cap[source][to]>0 and not vis[to] and augment_flow(cap,to,sink,vis):
                cap[source][to] -= 1
                cap[to][source] += 1
                return True
        return False
    
    flow = 0
    while(augment_flow(cap,source,sink)):
        flow += 1
    return flow
