'''
This Prim's Algorithm Code is for finding weight of minimum spanning tree
of a connected graph.
For argument graph, it should be a dictionary type
such as
graph = {
    'a': [ [3, 'b'], [8,'c'] ],
    'b': [ [3, 'a'], [5, 'd'] ],
    'c': [ [8, 'a'], [2, 'd'], [4, 'e'] ],
    'd': [ [5, 'b'], [2, 'c'], [6, 'e'] ],
    'e': [ [4, 'c'], [6, 'd'] ]
}

where 'a','b','c','d','e' are nodes (these can be 1,2,3,4,5 as well)
'''


import heapq  # for priority queue

# prim's algo. to find weight of minimum spanning tree
def prims_minimum_spanning(graph_used):
    vis=[]
    s=[[0,1]]
    prim = []
    mincost=0
    
    while(len(s)>0):
        v=heapq.heappop(s)
        x=v[1]
        if(x in vis):
            continue

        mincost += v[0]
        prim.append(x)
        vis.append(x)

        for j in graph_used[x]:
            i=j[-1]
            if(i not in vis):
                heapq.heappush(s,j)

    return mincost
