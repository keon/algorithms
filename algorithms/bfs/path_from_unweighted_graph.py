'''
Given an unweighted directional graph G, write a program to find out whether there is a path from i to j for all vertices (i, j).

The first line gives the number of vertices N (1 ≤ N ≤ 100). Lines 2 through N give the adjacency matrix of the graph. 
If the j number of the i line is 1, it means that there is an edge from i to j. The i number in line i is always zero.

Print the correct answer in question in adjacency matrix form over a total of N lines. 
If there is a path from vertex i to j, the jth number on line i should be printed as 1, otherwise 0.


ex 1)
if input is
3
0 1 0
0 0 1
1 0 0

output should be
1 1 1
1 1 1
1 1 1

ex 2)
if input is
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0

output should be
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
'''

def bfs(v, d):
    q = [v]
    visited = [False] * N
    state = False

    while q:
        v = q.pop(0)
        if not(visited[v]):
            visited[v] = True
            for e in adj[v]:
                if e == d:
                    print(1, end=" ")
                    state = True
                    break
                if not(visited[e]):
                    q.append(e)
            if state:
                break
    else:
        print(0, end=" ")

N = int(input())
adj = [[] for _ in range(N)]

for i in range(N):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        if a[j]:
            adj[i].append(j)

for i in range(N):
    for j in range(N):
        bfs(i, j)
    print()
