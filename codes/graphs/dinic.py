from collections import deque

def bfs(source, sink):
    level[:] = [-1]*len(graph)
    level[source] = 0
    Q = deque([source])
    while Q:
        cur = Q.popleft()
        for nxt in graph[cur]:
            if level[nxt] == -1 and capa[cur][nxt] - flow[cur][nxt] > 0:
                level[nxt] = level[cur] + 1
                Q.append(nxt)
    return level[sink] != -1

def dfs(source, sink, work):
    st = [(source, 10**9)]
    while st:
        cur, flw = st[-1]
        if cur == sink:
            for _ in range(level[sink]):
                nxt, res = st.pop()
                work[st[-1][0]] -= 1
                flow[st[-1][0]][nxt] += flw
                flow[nxt][st[-1][0]] -= flw
            return flw
        for idx in range(work[cur], len(graph[cur])):
            nxt = graph[cur][idx]
            work[cur] += 1
            res = capa[cur][nxt] - flow[cur][nxt]
            if res > 0 and level[nxt] == level[cur] + 1:
                if flw > res: flw = res
                st.append((nxt, flw))
                break
        else: st.pop()
    return 0

def dinic(source, sink):
    total = 0
    while bfs(source, sink):
        work = [0 for _ in range(len(graph))]
        while 1:
            minflow = dfs(source, sink, work)
            if minflow == 0: break
            total += minflow
    return total

n = int(input())
graph = [[] for _ in range(n)]
capa = [[0]*n for _ in range(n)]
flow = [[0]*n for _ in range(n)]
level = [-1 for _ in range(n)]