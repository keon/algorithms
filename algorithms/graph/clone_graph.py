"""
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and
each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as
separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a
self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
import collections


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


# BFS
def clone_graph1(node):
    if not node:
        return
    node_copy = UndirectedGraphNode(node.label)
    dic = {node: node_copy}
    queue = collections.deque([node])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if neighbor not in dic:  # neighbor is not visited
                neighbor_copy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighbor_copy
                dic[node].neighbors.append(neighbor_copy)
                queue.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return node_copy


# DFS iteratively
def clone_graph2(node):
    if not node:
        return
    node_copy = UndirectedGraphNode(node.label)
    dic = {node: node_copy}
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighbor_copy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighbor_copy
                dic[node].neighbors.append(neighbor_copy)
                stack.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return node_copy


# DFS recursively
def clone_graph(node):
    if not node:
        return
    node_copy = UndirectedGraphNode(node.label)
    dic = {node: node_copy}
    dfs(node, dic)
    return node_copy


def dfs(node, dic):
    for neighbor in node.neighbors:
        if neighbor not in dic:
            neighbor_copy = UndirectedGraphNode(neighbor.label)
            dic[neighbor] = neighbor_copy
            dic[node].neighbors.append(neighbor_copy)
            dfs(neighbor, dic)
        else:
            dic[node].neighbors.append(dic[neighbor])
