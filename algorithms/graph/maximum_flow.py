"""
Maximum Flow Algorithms

Implements Ford-Fulkerson (DFS), Edmonds-Karp (BFS) and Dinic's algorithm
for computing maximum flow in a flow network.

Reference: https://en.wikipedia.org/wiki/Maximum_flow_problem

Complexity:
    Ford-Fulkerson: O(E * f)  where f is the max flow value
    Edmonds-Karp:   O(V * E^2)
    Dinic:          O(V^2 * E)
"""

from __future__ import annotations

from queue import Queue


def _dfs(
    capacity: list[list[int]],
    flow: list[list[int]],
    visit: list[bool],
    vertices: int,
    idx: int,
    sink: int,
    current_flow: int = 1 << 63,
) -> int:
    """DFS helper for Ford-Fulkerson.

    Args:
        capacity: Capacity matrix.
        flow: Current flow matrix.
        visit: Visited flags.
        vertices: Total number of vertices.
        idx: Current vertex index.
        sink: Sink vertex index.
        current_flow: Flow available along this path.

    Returns:
        Flow pushed along the augmenting path found.
    """
    if idx == sink:
        return current_flow
    visit[idx] = True
    for nxt in range(vertices):
        if not visit[nxt] and flow[idx][nxt] < capacity[idx][nxt]:
            available_flow = min(current_flow, capacity[idx][nxt] - flow[idx][nxt])
            tmp = _dfs(capacity, flow, visit, vertices, nxt, sink, available_flow)
            if tmp:
                flow[idx][nxt] += tmp
                flow[nxt][idx] -= tmp
                return tmp
    return 0


def ford_fulkerson(capacity: list[list[int]], source: int, sink: int) -> int:
    """Compute maximum flow using Ford-Fulkerson (DFS).

    Args:
        capacity: Capacity matrix.
        source: Source vertex.
        sink: Sink vertex.

    Returns:
        The maximum flow value.

    Examples:
        >>> ford_fulkerson([[0, 10, 0], [0, 0, 10], [0, 0, 0]], 0, 2)
        10
    """
    vertices = len(capacity)
    ret = 0
    flow = [[0] * vertices for _ in range(vertices)]
    while True:
        visit = [False for _ in range(vertices)]
        tmp = _dfs(capacity, flow, visit, vertices, source, sink)
        if tmp:
            ret += tmp
        else:
            break
    return ret


def edmonds_karp(capacity: list[list[int]], source: int, sink: int) -> int:
    """Compute maximum flow using Edmonds-Karp (BFS).

    Args:
        capacity: Capacity matrix.
        source: Source vertex.
        sink: Sink vertex.

    Returns:
        The maximum flow value.

    Examples:
        >>> edmonds_karp([[0, 10, 0], [0, 0, 10], [0, 0, 0]], 0, 2)
        10
    """
    vertices = len(capacity)
    ret = 0
    flow = [[0] * vertices for _ in range(vertices)]
    while True:
        tmp = 0
        queue: Queue[tuple[int, int]] = Queue()
        visit = [False for _ in range(vertices)]
        par = [-1 for _ in range(vertices)]
        visit[source] = True
        queue.put((source, 1 << 63))
        while queue.qsize():
            front = queue.get()
            idx, current_flow = front
            if idx == sink:
                tmp = current_flow
                break
            for nxt in range(vertices):
                if not visit[nxt] and flow[idx][nxt] < capacity[idx][nxt]:
                    visit[nxt] = True
                    par[nxt] = idx
                    queue.put(
                        (nxt, min(current_flow, capacity[idx][nxt] - flow[idx][nxt]))
                    )
        if par[sink] == -1:
            break
        ret += tmp
        parent = par[sink]
        idx = sink
        while parent != -1:
            flow[parent][idx] += tmp
            flow[idx][parent] -= tmp
            idx = parent
            parent = par[parent]
    return ret


def _dinic_bfs(
    capacity: list[list[int]],
    flow: list[list[int]],
    level: list[int],
    source: int,
    sink: int,
) -> bool:
    """BFS level graph construction for Dinic's algorithm.

    Args:
        capacity: Capacity matrix.
        flow: Current flow matrix.
        level: Level array (modified in place).
        source: Source vertex.
        sink: Sink vertex.

    Returns:
        True if sink is reachable from source.
    """
    vertices = len(capacity)
    queue: Queue[int] = Queue()
    queue.put(source)
    level[source] = 0
    while queue.qsize():
        front = queue.get()
        for nxt in range(vertices):
            if level[nxt] == -1 and flow[front][nxt] < capacity[front][nxt]:
                level[nxt] = level[front] + 1
                queue.put(nxt)
    return level[sink] != -1


def _dinic_dfs(
    capacity: list[list[int]],
    flow: list[list[int]],
    level: list[int],
    idx: int,
    sink: int,
    work: list[int],
    current_flow: int = 1 << 63,
) -> int:
    """DFS blocking flow for Dinic's algorithm.

    Args:
        capacity: Capacity matrix.
        flow: Current flow matrix.
        level: Level array.
        idx: Current vertex.
        sink: Sink vertex.
        work: Work pointer array.
        current_flow: Available flow.

    Returns:
        Flow pushed.
    """
    if idx == sink:
        return current_flow
    vertices = len(capacity)
    while work[idx] < vertices:
        nxt = work[idx]
        if level[nxt] == level[idx] + 1 and flow[idx][nxt] < capacity[idx][nxt]:
            available_flow = min(current_flow, capacity[idx][nxt] - flow[idx][nxt])
            tmp = _dinic_dfs(capacity, flow, level, nxt, sink, work, available_flow)
            if tmp > 0:
                flow[idx][nxt] += tmp
                flow[nxt][idx] -= tmp
                return tmp
        work[idx] += 1
    return 0


def dinic(capacity: list[list[int]], source: int, sink: int) -> int:
    """Compute maximum flow using Dinic's algorithm.

    Args:
        capacity: Capacity matrix.
        source: Source vertex.
        sink: Sink vertex.

    Returns:
        The maximum flow value.

    Examples:
        >>> dinic([[0, 10, 0], [0, 0, 10], [0, 0, 0]], 0, 2)
        10
    """
    vertices = len(capacity)
    flow = [[0] * vertices for _ in range(vertices)]
    ret = 0
    while True:
        level = [-1 for _ in range(vertices)]
        work = [0 for _ in range(vertices)]
        if not _dinic_bfs(capacity, flow, level, source, sink):
            break
        while True:
            tmp = _dinic_dfs(capacity, flow, level, source, sink, work)
            if tmp > 0:
                ret += tmp
            else:
                break
    return ret
