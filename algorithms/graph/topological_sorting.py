def findOrder(self, numCourses, prerequisites):
    def topologicalsort(g):
        indegrees = {node : 0 for node in g}
        
        for node in g:
            for neighbor in g[node]:
                indegrees[neighbor] += 1
                
        q = []
        for node in g:
            if indegrees[node] == 0:
                q.append(node)
                
        order = []
        while q:
            node = q.pop()
            order.append(node)
            for neighbor in g[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
                    
        return order
    
    g = {i : [] for i in range(numCourses)}
    for p in prerequisites:
        src,dest = p
        g[src].append(dest)
        
    order = topologicalsort(g)
    
    return reversed(order) if len(order) == numCourses else []