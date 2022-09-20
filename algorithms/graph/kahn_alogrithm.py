"""
Kahn's algorithm:
    This algorithm is used for topological sorting inside graph 
    [vertex, connected to]
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should 
have finished both courses 1 and 2. Both courses 1 and 2 should be taken after 
you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
"""

def findOrder(numCourses: int, prerequisites: list[list[int]]):
    adj_list = defaultdict(list)
    indegree = {}
    for dest, src in prerequisites:
        adj_list[src].append(dest)
        indegree[dest] = indegree.get(dest,0) +1 #record each node indegree

    zero_indegree_qeue = deque([k for k in range(numCourses) if k not in indegree])
    topological_sorted_order = []

    while zero_indegree_qeue:

        vertex = zero_indegree_qeue.popleft()
        topological_sorted_order.append(vertex)
        if vertex in adj_list:
            for neighbour in adj_list[vertex]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    zero_indegree_qeue.append(neighbour)

    return topological_sorted_order if len(topological_sorted_order) == numCourses else []
        
