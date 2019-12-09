'''
This Bellman-Ford Code is for determination whether we can get
shortest path from given graph or not for single-source shortest-paths problem.
In other words, if given graph has any negative-weight cycle that is reachable
from the source, then it will give answer False for "no solution exits".
For argument graph, it should be a dictionary type
such as
graph = {
    'a': {'b': 6, 'e': 7},
    'b': {'c': 5, 'd': -4, 'e': 8},
    'c': {'b': -2},
    'd': {'a': 2, 'c': 7},
    'e': {'b': -3}
}
'''

def bellman_ford(graph, source):
    weight = {}
    pre_node = {}

    initialize_single_source(graph, source, weight, pre_node)

    for i in range(1, len(graph)):
        for node in graph:
            for adjacent in graph[node]:
                if weight[adjacent] > weight[node] + graph[node][adjacent]:
                    weight[adjacent] = weight[node] + graph[node][adjacent]
                    pre_node[adjacent] = node

    for node in graph:
        for adjacent in graph[node]:
            if weight[adjacent] > weight[node] + graph[node][adjacent]:
                return False

    return True

def initialize_single_source(graph, source, weight, pre_node):

    for node in graph:
        weight[node] = float('inf')
        pre_node[node] = None

    weight[source] = 0
    
