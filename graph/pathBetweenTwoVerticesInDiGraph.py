from collections import defaultdict

class Graph:
	def __init__(self,v):
		self.v = v
		self.graph = defaultdict(list)
		self.has_path = False

	def add_edge(self,u,v):
		self.graph[u].append(v)

	def dfs(self,x,y):
		visited = [False] * self.v
		self.dfsutil(visited,x,y,)

	def dfsutil(self,visited,x,y):
		visited[x] = True
		for i in self.graph[x]:
			if y in self.graph[x]:
				self.has_path = True
				return
			if(not(visited[i])):
				self.dfsutil(visited,x,i)

	def is_reachable(self,x,y):
		self.has_path = False
		self.dfs(x,y)
		return self.has_path


# Create a graph given in the above diagram
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
 
u =1; v = 3
 
if g.is_reachable(u, v):
    print("There is a path from %d to %d" % (u,v))
else :
    print("There is no path from %d to %d" % (u,v))
 
u = 3; v = 1
if g.is_reachable(u, v) :
    print("There is a path from %d to %d" % (u,v))
else :
    print("There is no path from %d to %d" % (u,v))
