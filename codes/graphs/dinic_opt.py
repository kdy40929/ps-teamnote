from collections import deque

def bfs(source, sink):
    level[:] = [-1]*len(graph)
    level[source] = 0
    Q = deque([source])
    while Q:
        cur = Q.popleft()
        for nxt, c, _ in graph[cur]:
            if level[nxt] == -1 and c:
                level[nxt] = level[cur] + 1
                Q.append(nxt)
    return level[sink] != -1

def dfs(source, sink, work):
    st = [(source, -1, 10**9)]
    while st:
        cur, ix, flw = st[-1]
        if cur == sink:
            for _ in range(level[sink]):
                nxt, idx, res = st.pop()
                work[st[-1][0]] -= 1
                graph[st[-1][0]][idx][1] -= flw
                revidx = graph[st[-1][0]][idx][2]
                graph[nxt][revidx][1] += flw
            return flw
        for idx in range(work[cur], len(graph[cur])):
            nxt, res = graph[cur][idx][:2]
            work[cur] += 1
            if res > 0 and level[nxt] == level[cur] + 1:
                if flw > res: flw = res
                st.append((nxt, idx, flw))
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

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
level = [-1 for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    # connected node, capa, edge num
    graph[a].append([b, 1, len(graph[b])])
    graph[b].append([a, 0, len(graph[a])-1])
print(dinic(0, n-1))