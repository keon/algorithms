#count connected no of component using DFS
'''
In graph theory, a component, sometimes called a connected component, 
of an undirected graph is a subgraph in which any 
two vertices are connected to each other by paths.

Example:


    1                3------------7
    |
    |
    2--------4
    |        |
    |        |              output = 2
    6--------5

'''

# Code is Here

def dfs(source,visited,l):
    ''' Function that performs DFS '''

    visited[source] = True
    for child in l[source]:
        if not visited[child]:
            dfs(child,visited,l)
            
def count_components(l,size):
    ''' 
    Function that counts the Connected components on bases of DFS.
    return type : int
    '''

    count = 0
    visited = [False]*(size+1)
    for i in range(1,size+1):
        if not visited[i]:
            dfs(i,visited,l)
            count+=1
    return count   

    
# Driver code
if __name__ == '__main__':
    n,m = map(int, input("Enter the Number of Nodes and Edges \n").split(' '))
    l = [[] for _ in range(n+1)]
    for i in range(m):
        print("Enter the edge's Nodes in form of a b\n")
        a,b = map(int,input().split(' '))
        l[a].append(b)
        l[b].append(a)
    print("Total number of Connected Components are : ", count_components(l,n))
