def buildhld(graph, n, root=1):
    # 1-base index
    parent = [0]*(n+1)
    depth = [0]*(n+1)
    size = [0]*(n+1)
    heavy = [-1]*(n+1)

    st = [(root, 0)]
    while st:
        node, flag = st.pop()
        if flag:
            hchild = -1; maxsize = 0
            size[node] = 1
            for child in graph[node]:
                if parent[node] == child: continue
                size[node] += size[child]
                if size[child] > maxsize:
                    maxsize = size[child]
                    hchild = child
            heavy[node] = hchild
        else:
            st.append((node, 1))
            for child in graph[node]:
                if parent[node] == child: continue
                parent[child] = node
                depth[child] = depth[node] + 1
                st.append((child, 0))

    head = [0]*(n+1)
    pos = [0]*(n+1)

    # decomposition
    st = [root] # chain head
    num = 0
    while st:
        h = st.pop()
        cur = h
        while cur != -1:
            head[cur] = h
            pos[cur] = num
            num += 1
            for nxt in graph[cur]:
                if parent[cur] == nxt or heavy[cur] == nxt:
                    continue
                st.append(nxt)
            cur = heavy[cur]

    return parent, depth, size, heavy, head, pos

def update_path(u, v, parent, depth, head, pos, a, b):
    while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
            u, v = v, u
        seg.update(pos[head[u]], pos[u], a, b)
        u = parent[head[u]]
    if depth[u] > depth[v]:
        u, v = v, u
    # include lca (u == lca)
    seg.update(pos[u], pos[v], a, b)
    return

def getsum_path(u, v, parent, depth, head, pos):
    ans = 0
    while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
            u, v = v, u
        ans = (ans + seg.range_sum(pos[head[u]], pos[u])) & mask
        u = parent[head[u]]
    if depth[u] > depth[v]:
        u, v = v, u
    # include lca (u == lca)
    ans = (ans + seg.range_sum(pos[u], pos[v])) & mask
    return ans