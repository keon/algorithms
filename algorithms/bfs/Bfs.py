from collections import defaultdict

class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, s):
        visited = [False]*(len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            print s,
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def dfs_visited(self,v,visited):
        visited[v]= True
        print v,
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_visited(i, visited)

    def DFS(self,v):
        visited = [False]*(len(self.graph))
        self.dfs_visited(v,visited)
        
g = Graph()
g.addEdge(0, 3)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print "Following is BFS starting from 2"
g.BFS(2)

print "\nFollowing is DFS starting from 2"
g.DFS(2)
