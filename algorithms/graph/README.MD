Graph Search Algorythims
=======================


Dijkstra
--------

Find Path between 2 vertices | nodes in a Graph with minimum Edges's weights sum cost.

Dijkstra Algorithm finds shortest paths between nodes in a graph for a given source node in the graph, the results is based on the relative point of the source path.

Dijkstra Algorithm is based on the principle of **Relaxation** an approximation to the correct distance is gradually replaced by more accurate values till the shortes distance path is found. 

It uses a **priotity queue** to greedily select the closest vertex that hasn't been processed, then performs the relaxation process on all of its neighbors. 


#### KeyWords

- Graph = Map = G ; 
- Vertex = Intersections = V 
- Vertex = u
- Edge = Roads | Path = E
- Edge's Length = Weight = W
- Path = P = ( v 1 , v 2 , … , v n ) ∈ V × V × ⋯ × V 
- Spanning Tree = T 
- Source = Root Node

------------------------------------------