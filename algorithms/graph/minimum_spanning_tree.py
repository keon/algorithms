"""
Minimum spanning tree (MST) is going to use an undirected graph
"""

import sys

# pylint: disable=too-few-public-methods
class Edge:
    """
    An edge of an undirected graph
    """

    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class DisjointSet:
    """
    The disjoint set is represented with an list <n> of integers where
    <n[i]> is the parent of the node at position <i>.
    If <n[i]> = <i>, <i> it's a root, or a head, of a set
    """

    def __init__(self, size):
        """
        Args:
            n (int): Number of vertices in the graph
        """

        self.parent = [None] * size # Contains wich node is the parent of the node at poisition <i>
        self.size = [1] * size # Contains size of node at index <i>, used to optimize merge
        for i in range(size):
            self.parent[i] = i # Make all nodes his own parent, creating n sets.

    def merge_set(self, node1, node2):
        """
        Args:
            node1, node2 (int): Indexes of nodes whose sets will be merged.
        """

        # Get the set of nodes at position <a> and <b>
        # If <a> and <b> are the roots, this will be constant O(1)
        node1 = self.find_set(node1)
        node2 = self.find_set(node2)

        # Join the shortest node to the longest, minimizing tree size (faster find)
        if self.size[node1] < self.size[node2]:
            self.parent[node1] = node2 # Merge set(a) and set(b)
            self.size[node2] += self.size[node1] # Add size of old set(a) to set(b)
        else:
            self.parent[node2] = node1 # Merge set(b) and set(a)
            self.size[node1] += self.size[node2] # Add size of old set(b) to set(a)

    def find_set(self, node):
        """
        Get the root element of the set containing <a>
        """
        if self.parent[node] != node:
            # Very important, memoize result of the
            # recursion in the list to optimize next
            # calls and make this operation practically constant, O(1)
            self.parent[node] = self.find_set(self.parent[node])

        # node <a> it's the set root, so we can return that index
        return self.parent[node]


def kruskal(vertex_count, edges, forest):
    """
    Args:
        vertex_count (int): Number of vertices in the graph
        edges (list of Edge): Edges of the graph
        forest (DisjointSet): DisjointSet of the vertices
    Returns:
        int: sum of weights of the minnimum spanning tree

    Kruskal algorithm:
        This algorithm will find the optimal graph with less edges and less
        total weight to connect all vertices (MST), the MST will always contain
        n-1 edges because it's the minimum required to connect n vertices.

    Procedure:
        Sort the edges (criteria: less weight).
        Only take edges of nodes in different sets.
        If we take a edge, we need to merge the sets to discard these.
        After repeat this until select n-1 edges, we will have the complete MST.
    """
    edges.sort(key=lambda edge: edge.weight)

    mst = [] # List of edges taken, minimum spanning tree

    for edge in edges:
        set_u = forest.find_set(edge.u) # Set of the node <u>
        set_v = forest.find_set(edge.v) # Set of the node <v>
        if set_u != set_v:
            forest.merge_set(set_u, set_v)
            mst.append(edge)
            if len(mst) == vertex_count-1:
                # If we have selected n-1 edges, all the other
                # edges will be discarted, so, we can stop here
                break

    return sum([edge.weight for edge in mst])


def main():
    """
    Test. How input works:
    Input consists of different weighted, connected, undirected graphs.
    line 1:
      integers n, m
    lines 2..m+2:
      edge with the format -> node index u, node index v, integer weight

    Samples of input:

    5 6
    1 2 3
    1 3 8
    2 4 5
    3 4 2
    3 5 4
    4 5 6

    3 3
    2 1 20
    3 1 20
    2 3 100

    Sum of weights of the optimal paths:
    14, 40
    """
    for size in sys.stdin:
        vertex_count, edge_count = map(int, size.split())
        forest = DisjointSet(edge_count)
        edges = [None] * edge_count # Create list of size <m>

        # Read <m> edges from input
        for i in range(edge_count):
            source, target, weight = map(int, input().split())
            source -= 1 # Convert from 1-indexed to 0-indexed
            target -= 1 # Convert from 1-indexed to 0-indexed
            edges[i] = Edge(source, target, weight)

        # After finish input and graph creation, use Kruskal algorithm for MST:
        print("MST weights sum:", kruskal(vertex_count, edges, forest))

if __name__ == "__main__":
    main()
