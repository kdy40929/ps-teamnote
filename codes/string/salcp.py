from bisect import bisect_left

def count_sort(arr, key, k):
    # count sorting by key[idx], range: 0 - k
    n = len(arr)
    cnt = [0] * (k+1)
    for val in arr:
        cnt[key[val]] += 1
    pfs = [0] * (k+1)
    for i in range(k):
        pfs[i+1] = pfs[i] + cnt[i]
    out = [0] * n
    for val in arr:
        out[pfs[key[val]]] = val
        pfs[key[val]] += 1
    return out

def make_suffix(s):
    n = len(s)
    if n == 0: return []
    sa = [*range(n)]
    uniq = []
    for ch in sorted(s):
        if not uniq or ch != uniq[-1]:
            uniq.append(ch)
    rank = [bisect_left(uniq, ch) for ch in s]
    k = 1
    while k < n:
        key1 = [r+1 for r in rank]
        key2 = [rank[i+k]+1 if i+k < n else 0 for i in range(n)]
        sa = count_sort(sa, key2, max(key2))
        sa = count_sort(sa, key1, max(key1))
        cnt = 0
        new_rank = [0] * n
        new_rank[sa[0]] = 0
        for i in range(1, n):
            a, b = sa[i], sa[i-1]
            ra, rb = rank[a], rank[b]
            rka = rank[a+k] if a+k < n else -1
            rkb = rank[b+k] if b+k < n else -1
            if ra != rb or rka != rkb:
                cnt += 1
            new_rank[a] = cnt
        rank = new_rank[:]
        if cnt == n-1: break
        k *= 2
    return sa

def makelcp(s, sa):
    n = len(s)
    if n <= 1: return []
    rev = [0] * n
    for i, p in enumerate(sa):
        rev[p] = i
    lcp = [0] * (n-1)
    prvl = 0
    for i in range(n):
        r = rev[i]
        if r == 0: prvl = 0; continue
        j = sa[r-1]
        while i+prvl < n and j+prvl < n and s[i+prvl] == s[j+prvl]:
            prvl += 1
        lcp[r-1] = prvl
        if prvl: prvl -= 1
    return lcp