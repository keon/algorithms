import heapq  # for priority queue

# prim's algo. to find weight of minimum spanning tree
def prims(graph):
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

        for j in g[x]:
            i=j[-1]
            if(i not in vis):
                heapq.heappush(s,j)

    return mincost



if __name__=="__main__":

    # input number of nodes and edges in graph
    n,e = map(int,input().split())

    # initializing empty graph as a dictionary (of the form {int:list})
    g=dict(zip([i for i in range(1,n+1)],[[] for i in range(n)]))

    # input graph data
    for i in range(e):
        a,b,c=map(int,input().split())
        g[a].append([c,b])
        g[b].append([c,a])

    # print weight of minimum spanning tree
    print(prims(g))

    ''' tests-
    Input : 4 5
            1 2 7
            1 4 6
            2 4 9
            4 3 8
            2 3 6
    Output : 19


    Input : 5 6
            1 2 3
            1 3 8
            2 4 5
            3 4 2
            3 5 4
            4 5 6
    Output : 14
    '''
