class OrientedGraph:
	def __init__(self):
		self.nodes = {}

	def insertNode(self, u):
		if u not in self.nodes:
			self.nodes[u] = {}

	def V(self):
		return self.nodes.keys()

	def adj(self, u):
		if u in self.nodes:
			return self.nodes[u]

	def insertEdge(self, u, v, w=0):
		if u not in self.nodes:
			self.insertNode(u)
		if v not in self.nodes:
			self.insertNode(v)
		self.nodes[u][v] = w

	def bfs(self, start):
		S = [start]
		visited = {}
		for node in self.V():
			visited[node] = False
		visited[start] = True
		while len(S) > 0:
			u = S.pop(0)
			for v in self.adj(u):
				print u, v, self.nodes[u][v]
				if not visited[v]:
					visited[v] = True
					S.append(v)

	def dfs(self, start):
		S = [start]
		visited = {}
		for node in self.V():
			visited[node] = False
		visited[start] = True
		while len(S) > 0:
			u = S.pop(-1)
			for v in self.adj(u):
				print u, v
				if not visited[v]:
					visited[v] = True
					S.append(v)

	def __str__(self):
		string = ""
		for u in self.V():
			string += (str(u) + "->" + str(self.adj(u)) + "\n")
		return string

	def init_bellman(self, source):
		d = {}  # Stands for destination
		p = {}  # Stands for predecessor
		for node in self.nodes:
			d[node] = float('Inf')  # We start admiting that the rest of nodes are very very far
			p[node] = None
		d[source] = 0  # For the source we know how to reach
		return d, p

	def relax(self, node, neighbour, graph, d, p):
		if d[neighbour] > d[node] + graph[node][neighbour]:
			# Record this lower distance
			d[neighbour] = d[node] + graph[node][neighbour]
			p[neighbour] = node

	def bellman_ford(self, start):
		graph = self.nodes
		d, p = self.init_bellman(start)
		for i in range(len(graph) - 1):  #Run this until is converges
			for u in graph:
				for v in graph[u]:
					self.relax(u, v, graph, d, p)  # Lets relax it

		for u in graph:
			for v in graph[u]:
				assert d[v] <= d[u] + graph[u][v]

		print "Costs to reach destination from", start, "after bellman-ford: ", d
		return d, p


def init():
	graph = OrientedGraph()
	for u in ['a', 'b', 'c', 'd', 'e', 'f']:
		graph.insertNode(u)
	for u, v, w in [('a', 'b', 3), ('a', 'd', 2), ('b', 'c', 0), ('d', 'a', 1), ('d', 'c', 6), ('d', 'e', 10), ('e', 'c', 1), ('e', 'f', 0)]:
		graph.insertEdge(u, v, w)
	print str(graph)
	#  Test bellman starting from a
	graph.bellman_ford('a')
	return


if __name__ == "__main__":
	init()
