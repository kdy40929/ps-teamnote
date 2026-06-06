INF = 10**18

def bellman_ford(edges, n, root):
    dist = [INF]*n
    dist[root] = 0
    for i in range(n):
        for j in range(len(edges)):
            if dist[edges[j][0]] < INF and dist[edges[j][1]] > dist[edges[j][0]] + edges[j][2]:
                dist[edges[j][1]] = dist[edges[j][0]] + edges[j][2]
                if i == n-1: return -1
    return dist