from collections import deque
INF = 10**18

def SPFA(graph, root):
    n = len(graph)
    dist = [INF for _ in range(n)]
    dist[root] = 0
    Q = deque([root])
    inque = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    visited[root] = 1
    inque[root] = 1
    while Q:
        cur = Q.popleft()
        inque[cur] = 0
        for nxt, weight in graph[cur]:
            if dist[nxt] > dist[cur] + weight:
                dist[nxt] = dist[cur] + weight
                if not inque[nxt]:
                    Q.append(nxt)
                    inque[nxt] = 1
                    visited[nxt] += 1
                    if visited[nxt] >= len(graph):
                        return -1
    return dist