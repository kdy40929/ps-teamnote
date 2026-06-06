n, m = map(int, input().split())
graph = [[] for _ in range(2*n+1)]
edge = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)
    edge.append((-a, b))
    edge.append((-b, a))
sccs = makescc(2*n+1, graph)
group = [-1 for _ in range(2*n+1)]
for i in range(len(sccs)):
    for node in sccs[i]:
        group[node] = i
flag = 1
solution = [0 for _ in range(n)]
for i in range(1, n+1):
    if group[i] == group[-i]:
        flag = 0
        break
    if group[i] > group[-i]:
        solution[i-1] = 1