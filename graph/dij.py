#Dijkstra's single source shortest path algorithm

import sys
 
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t\t Min Distance from Source")
        for node in range(self.V):
            print(node,"   \t\t",dist[node])
 

    def minDistance(self, dist, MinSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and MinSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 

    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        MinSet = [False] * self.V
 
        for cout in range(self.V):
 
	    #minimum distance vertex that is not processed
            u = self.minDistance(dist, MinSet)
 
	    #put minimum distance vertex in shortest tree
            MinSet[u] = True
 
            # Update dist value of the adjacent vertices 
            for v in range(self.V):
                if self.graph[u][v] > 0 and MinSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
 
#MAIN
"""vert=input("Enter the number of vertices: ")
g  = Graph(vert)
print("Enter the adjacency matrix representation of graph: ")
for i in range(0, 9):
	for j in range(0, 9):
		g.graph[i][j]=input()
sv=input("Enter the source vertex: ")
g.dijkstra(sv);"""

g=Graph(6)
g.graph= [[0, 4, 4, 0, 0, 0],
	  [4, 0, 2, 0, 0, 0],
	  [4, 2, 0, 3, 6, 1],
	  [0, 0, 3, 0, 2, 0],
	  [0, 0, 6, 2, 0, 3],
	  [0, 0, 1, 0, 3, 0]]
g.dijkstra(0)
