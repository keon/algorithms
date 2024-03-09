"""
Implementing strongly connected components in a graph using Kosaraju's algorithm.
https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
"""


class Kosaraju:
    """
    Kosaraju's algorithm use depth first search approach to find strongly connected components in a directed graph.
    Approach:
        1. Make a DFS call to keep track of finish time of each vertex.
        2. Tranpose the original graph. ie 1->2 transpose is 1<-2
        3. Make another DFS call to calculate strongly connected components.
    """

    def dfs(self, i, V, adj, visited, stk):
        visited[i] = 1

        for x in adj[i]:
            if visited[x] == -1:
                self.dfs(x, V, adj, visited, stk)

        stk.append(i)

    def kosaraju(self, V, adj):

        stk, visited = [], [-1]*(V+1)

        for i in range(V):
            if visited[i] == -1:
                self.dfs(i, V, adj, visited, stk)

        stk.reverse()
        res = stk.copy()

        ans, visited1 = 0, [-1]*(V+1)

        adj1 = [[] for x in range(V)]

        for i in range(len(adj)):
            for x in adj[i]:
                adj1[x].append(i)

        for i in range(len(res)):
            if visited1[res[i]] == -1:
                ans += 1
                self.dfs(res[i], V, adj1, visited1, stk)

        return ans


def main():
    """
    Let's look at the sample input.

    6 7  #no of vertex, no of edges
    0 2  #directed edge 0->2
    1 0
    2 3
    3 1
    3 4
    4 5
    5 4

    calculating no of strongly connected compnenets in a directed graph.
    answer should be: 2
    1st strong component: 0->2->3->1->0
    2nd strongly connected component: 4->5->4
    """
    V, E = map(int, input().split())
    adj = [[] for x in range(V)]

    for i in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)

    print(Kosaraju().kosaraju(V, adj))


if __name__ == '__main__':
    main()
