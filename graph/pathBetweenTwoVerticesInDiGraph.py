from collections import defaultdict

class Graph:
	def __init__(self,v):
		self.v = v
		self.graph = defaultdict(list)
		self.hasPath = False

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def DFS(self,x,y):
		visited = [False] * self.v
		self.DFSUtil(visited,x,y,)

	def DFSUtil(self,visited,x,y):
		visited[x] = True
		for i in self.graph[x]:
			if y in self.graph[x]:
				self.hasPath = True
				return
			if(not(visited[i])):
				self.DFSUtil(visited,x,i)

	def isReachable(self,x,y):
		self.hasPath = False
		self.DFS(x,y)
		return self.hasPath


# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
u =1; v = 3
 
if g.isReachable(u, v):
    print("There is a path from %d to %d" % (u,v))
else :
    print("There is no path from %d to %d" % (u,v))
 
u = 3; v = 1
if g.isReachable(u, v) :
    print("There is a path from %d to %d" % (u,v))
else :
    print("There is no path from %d to %d" % (u,v))