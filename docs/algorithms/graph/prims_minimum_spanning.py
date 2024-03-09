'''
This Prim's Algorithm Code is for finding weight of minimum spanning tree
of a connected graph.
For argument graph, it should be a dictionary type such as:

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

def prims_minimum_spanning(graph_used):
    """
    Prim's algorithm to find weight of minimum spanning tree
    """
    vis=[]
    heap=[[0,1]]
    prim = set()
    mincost=0

    while len(heap) > 0:
        cost, node = heapq.heappop(heap)
        if node in vis:
            continue

        mincost += cost
        prim.add(node)
        vis.append(node)

        for distance, adjacent in graph_used[node]:
            if adjacent not in vis:
                heapq.heappush(heap, [distance, adjacent])

    return mincost
