import heapq as hq
INF = 10**18
 
def dijkstra(graph, root):
    n = len(graph)
    dist = [INF]*n
    dist[root] = 0
    heap = []
    hq.heappush(heap, (0, root))
    while heap:
        val, cur = hq.heappop(heap)
        if dist[cur] != val: continue
        for nxt, w in graph[cur]:
            if dist[cur] + w < dist[nxt]:
                dist[nxt] = dist[cur] + w
                hq.heappush(heap, (dist[nxt], nxt))
    return dist