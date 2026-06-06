from collections import deque
INF = 10**9

def bfs(bigraph, matchL, matchR, dist):
    Q = deque()
    dist[0] = INF
    for i in range(1, len(bigraph)):
        if matchL[i] == 0:
            dist[i] = 0
            Q.append(i)
        else:
            dist[i] = INF
    while Q:
        x = Q.popleft()
        if dist[x] < dist[0]:
            for y in bigraph[x]:
                z = matchR[y]
                if dist[z] == INF:
                    dist[z] = dist[x] + 1
                    Q.append(z)
    return dist[0] != INF

def dfs(bigraph, matchL, matchR, dist, work, root):
    st = [root]
    path = []
    while st:
        x = st[-1]
        if x == 0:
            for u, v in zip(st[:-1], path):
                matchL[u] = v
                matchR[v] = u
            return 1
        while work[x] < len(bigraph[x]):
            y = bigraph[x][work[x]]
            work[x] += 1
            z = matchR[y]
            if dist[z] == dist[x] + 1:
                path.append(y)
                st.append(z)
                work[z] = 0
                break
        else:
            st.pop()
            if path: path.pop()
            dist[x] = INF
    return 0

def hopcroft_karp(bigraph, n, m):
    # 1-base index
    matchL = [0] * (n+1)
    matchR = [0] * (m+1)
    dist = [0] * (n+1)
    ans = 0
    while bfs(bigraph, matchL, matchR, dist):
        work = [0] * (n+1)
        for i in range(1, n+1):
            if matchL[i] == 0:
                ans += dfs(bigraph, matchL, matchR, dist, work, i)
    return ans