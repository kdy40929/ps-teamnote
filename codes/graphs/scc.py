def makescc(graph, n):
    seq, low = [-1]*n, [-1]*n
    onst = [0]*n
    sccs = []
    num = 0
    st1, st2 = [], []
    # st1: tarjan stack, st2: dfs stack

    for start in range(n):
        if seq[start] != -1: continue
        st2.append((start, -1, 0))
        while st2:
            cur, pr, flag = st2.pop()
            if flag:
                for nxt in graph[cur]:
                    if onst[nxt]:
                        low[cur] = min(low[cur], seq[nxt])
                if pr != -1:
                    low[pr] = min(low[pr], low[cur])
                if seq[cur] == low[cur]:
                    scc = []
                    while st1:
                        v = st1.pop()
                        onst[v] = 0
                        scc.append(v)
                        if v == cur: break
                    sccs.append(sorted(scc))
            else:
                if seq[cur] != -1: continue
                seq[cur] = low[cur] = num
                num += 1
                st1.append(cur); onst[cur] = 1
                st2.append((cur, pr, 1))
                for nxt in graph[cur]:
                    if seq[nxt] == -1:
                        st2.append((nxt, cur, 0))
    return sccs[::-1]