from collections import defaultdict

class Graph:
    def __init__(self, directed=True, weighted=False):
        self.__adjacency_list = {}
        self.__weighted_adj_list = defaultdict()
        self.__vertex_list = []
        self.__directed = directed
        self.__weighted = weighted 

    def add_vertex(self, vertex):
        if vertex not in self.__vertex_list:
            self.__vertex_list.append(vertex)
            self.__adjacency_list[vertex] = []
            self.__weighted_adj_list[vertex] = {}

    def add_edge(self, v1, v2, weight=0):
        if not self.__adjacency_list.get(v1):
            self.add_vertex(v1)
        if not self.__adjacency_list.get(v2):
            self.add_vertex(v2)
        if not self.__weighted:
            self.__adjacency_list[v1].append(v2)
            if not self.__directed:
                self.__adjacency_list[v2].append(v1)
        else:
            self.__adjacency_list[v1].append(v2)
            self.__weighted_adj_list[v1][v2] = weight
            if not self.__directed:
                self.__adjacency_list[v2].append(v1)
                self.__weighted_adj_list[v2][v1] = weight

    @property
    def weighted_adj_list(self):
        weighted_list = {k: v for k, v in self.__weighted_adj_list.items()}
        return weighted_list
        
    @property
    def vertecies_list(self):
        return self.__vertex_list

    @property
    def adjacency_list(self):
        return self.__adjacency_list
    
    def get_weight(self, u, v):
        weight = self.__weighted_adj_list[u][v]
        return weight 

    def weighted_matrix(self):
        """
>>> g = graph.Graph(directed=False, weighted=True)
>>> g.add_vertex("a")
>>> g.add_vertex("b")
>>> g.add_vertex("c")
>>> g.add_vertex("d")
>>> g.add_edge("b", "c", 7)
>>> g.add_edge("a", "b", 6)
>>> g.add_edge("a", "c", 4)
>>> g.add_edge("b", "d", 5)
>>> g.add_edge("c", "d", 6)
>>> w = g.weighted_matrix()
>>> graph.print_matrix(w)
...     # a  b  c  d
...      [0, 6, 4, 0] # a
...      [6, 0, 7, 5] # b
...      [4, 7, 0, 6] # c
...      [0, 5, 6, 0] # d
        """
        size = len(self.__vertex_list)
        index_id = {}
        matrix = [[0 for x in range(size)] for y in range(size)]
        index = 0
        for i in sorted(self.__vertex_list):
            index_id[i] = index
            index += 1
        for u in sorted(self.__weighted_adj_list):
            for v in sorted(self.__weighted_adj_list[u]):
                matrix[index_id[u]][index_id[v]] = self.__weighted_adj_list[u][v]
        return matrix

    def adj_matrix(self):
        """  
>>> graph = Graph()
>>> graph.add_vertex("a")
>>> graph.add_vertex("b")
>>> graph.add_vertex("c")  
>>> graph.add_vertex("d")
>>> graph.add_vertex("e")
>>> graph.add_vertex("f")
>>> graph.add_edge("a", "c")
>>> graph.add_edge("a", "f")
>>> graph.add_edge("b", "c")
>>> graph.add_edge("b", "d")
>>> graph.add_edge("b", "f")
>>> graph.add_edge("c", "d")
>>> graph.add_edge("d", "e")
>>> graph.add_edge("d", "f")
>>> graph.add_edge("e", "f")
>>> graph.print_matrix()
...    # a  b  c  d  e  f
...     [0, 0, 1, 0, 0, 1] # a
...     [0, 0, 1, 1, 0, 1] # b
...     [0, 0, 0, 1, 0, 0] # c
...     [0, 0, 0, 0, 1, 1] # d
...     [0, 0, 0, 0, 0, 1] # e
...     [0, 0, 0, 0, 0, 0] # f
        """
        keys = sorted(self.__adjacency_list.keys())
        size = len(keys)
        vertex_indices = dict(zip(keys, range(size)))
        matrix = [[0 for x in range(size)] for y in range(size)]
        for i in range(size):
            for j in range(i, size):
                for e in self.__adjacency_list[keys[i]]:
                    j = vertex_indices[e]
                    matrix[i][j] = 1
        return matrix

def print_matrix(matrix):
    for x in matrix:
        print(x)

def transpose(matrix):
    size = len(matrix)
    res = [[matrix[y][x] for y in range(size)] for x in range(len(matrix[0]))]
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod() 
