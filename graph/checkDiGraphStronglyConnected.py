from collections import defaultdict

class Graph:
	def __init__(self,v):
		self.v = v;
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def  DFS(self):
		visited = [False] * self.v
		self.DFSUtil(0,visited)
		if visited == [True]*self.v:
			return True
		return False

	def DFSUtil(self,i,visited):
		visited[i] = True
		for u in self.graph[i]:
			if not(visited[u]):
				self.DFSUtil(u,visited)

	def reverseGraph(self):
		g = Graph(self.v)
		for i in range(len(self.graph)):
			for j in self.graph[i]:
				g.addEdge(j,i)
		return g


	def isSC(self):
		if self.DFS():
			gr = self.reverseGraph()
			if gr.DFS():
				return True
		return False


# Create a graph given in the above diagram
g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
print ("Yes") if g1.isSC() else print("No")
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("Yes") if g2.isSC() else print("No")
