def lca(u, v):
    # 1-base index
    if level[u] > level[v]: u, v = v, u
    for j in range(len(parent[0])-1, -1, -1):
        if level[parent[v][j]] >= level[u]:
            v = parent[v][j]
    if u == v: return u
    for j in range(len(parent[0])-1, -1, -1):
        if parent[u][j] == parent[v][j]: continue
        u, v = parent[u][j], parent[v][j]
    return parent[u][0]

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
parent = [[0]*n.bit_length() for _ in range(n+1)]
st = [1]
while st:
    node = st.pop()
    for child in graph[node]:
        if parent[node][0] == child: continue
        st.append(child)
        parent[child][0] = node
for j in range(1, len(parent[0])):
    for i in range(1, n+1):
        parent[i][j] = parent[parent[i][j-1]][j-1]