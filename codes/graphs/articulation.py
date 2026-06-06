def makedst(n, graph):
    visited = [0 for _ in range(n)]
    dst = [[] for _ in range(n)]
    parent = [-1 for _ in range(n)]
    for root in range(n):
        if visited[root]: continue
        stack = [(root, -1)]
        while stack:
            node, prt = stack.pop()
            if visited[node]: continue
            if prt != -1:
                dst[node].append(prt)
                dst[prt].append(node)
            visited[node] = 1
            for adj in graph[node]:
                if visited[adj]: continue
                stack.append((adj, node))
    return dst

def artic_point(n, graph):
    cnt = 0
    dst = makedst(n, graph)
    parent = [-1 for _ in range(n)]
    points = []
    visited = [0 for _ in range(n)]
    seq = [0 for _ in range(n)]
    minidx = [0 for _ in range(n)]
    for root in range(n):
        if visited[root]: continue
        stack = [(root, 0)]
        while stack:
            node, flag = stack.pop()
            if flag:
                if node == root:
                    if len(dst[root]) > 1:
                        points.append(node)
                    continue
                for adj in dst[node]:
                    if parent[node] == adj: continue
                    if seq[node] <= minidx[adj]:
                        points.append(node)
                        break
                for adj in graph[node]:
                    if parent[node] == adj: continue
                    minidx[node] = min(minidx[node], minidx[adj])
            else:
                visited[node] = 1
                seq[node] = cnt
                minidx[node] = cnt
                cnt += 1
                stack.append((node, 1))
                for adj in dst[node]:
                    if visited[adj]: continue
                    stack.append((adj, 0))
                    parent[adj] = node
    return points

def artic_line(n, graph):
    cnt = 0
    dst = makedst(n, graph)
    parent = [-1 for _ in range(n)]
    lines = []
    visited = [0 for _ in range(n)]
    seq = [0 for _ in range(n)]
    minidx = [0 for _ in range(n)]
    for root in range(n):
        if visited[root]: continue
        stack = [(root, 0)]
        while stack:
            node, flag = stack.pop()
            if flag:
                for adj in dst[node]:
                    if parent[node] == adj: continue
                    if seq[node] < minidx[adj]:
                        if node < adj: lines.append((node, adj))
                        else: lines.append((adj, node))
                for adj in graph[node]:
                    if parent[node] == adj: continue
                    minidx[node] = min(minidx[node], minidx[adj])
            else:
                visited[node] = 1
                seq[node] = cnt
                minidx[node] = cnt
                cnt += 1
                stack.append((node, 1))
                for adj in dst[node]:
                    if visited[adj]: continue
                    stack.append((adj, 0))
                    parent[adj] = node
    return lines