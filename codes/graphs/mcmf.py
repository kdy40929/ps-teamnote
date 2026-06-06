from collections import deque
INF = 10**9

def spfa(source, sink, graph, capa, flow, cost):
    path = [-1] * len(graph)
    dist = [INF] * len(graph)
    inque = [0] * len(graph)
    dist[source] = 0
    inque[source] = 1
    Q = deque([source])
    while Q:
        cur = Q.popleft()
        inque[cur] = 0
        for nxt in graph[cur]:
            if capa[cur][nxt] > flow[cur][nxt] and dist[nxt] > dist[cur] + cost[cur][nxt]:
                dist[nxt] = dist[cur] + cost[cur][nxt]
                path[nxt] = cur
                if not inque[nxt]:
                    inque[nxt] = 1
                    Q.append(nxt)
    return path

def mcmf(source, sink, graph, capa, flow, cost):
    size = len(graph)
    ans = [0, 0] # max flow, min cost
    while 1:
        path = spfa(source, sink, graph, capa, flow, cost)
        if path[sink] == -1: break
        aug = INF
        j = sink
        while j != source:
            i = path[j]
            aug = min(aug, capa[i][j] - flow[i][j])
            j = i
        j = sink
        while j != source:
            i = path[j]
            flow[i][j] += aug
            flow[j][i] -= aug
            ans[1] += cost[i][j] * aug
            j = i
        ans[0] += aug
    return ans