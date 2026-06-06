INF = 10**18

def floyd(edges, n):
    floyd = [[INF]*n for _ in range(n)]
    for i in range(n+1):
        floyd[i][i] = 0
    for u, v, w in edges:
        floyd[u][v] = min(w, floyd[u][v])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
    return floyd