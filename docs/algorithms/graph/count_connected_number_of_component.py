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

def dfs(source,visited,adjacency_list):
    ''' Function that performs DFS '''

    visited[source] = True
    for child in adjacency_list[source]:
        if not visited[child]:
            dfs(child,visited,adjacency_list)

def count_components(adjacency_list,size):
    '''
    Function that counts the Connected components on bases of DFS.
    return type : int
    '''

    count = 0
    visited = [False]*(size+1)
    for i in range(1,size+1):
        if not visited[i]:
            dfs(i,visited,adjacency_list)
            count+=1
    return count

def main():
    """
    Example application
    """
    node_count,edge_count = map(int, input("Enter the Number of Nodes and Edges \n").split(' '))
    adjacency = [[] for _ in range(node_count+1)]
    for _ in range(edge_count):
        print("Enter the edge's Nodes in form of `source target`\n")
        source,target = map(int,input().split(' '))
        adjacency[source].append(target)
        adjacency[target].append(source)
    print("Total number of Connected Components are : ", count_components(adjacency,node_count))

# Driver code
if __name__ == '__main__':
    main()
