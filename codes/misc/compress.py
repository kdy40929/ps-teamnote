def compress(lst, typ=0):
    # typ == 1: return trace list together
    new = [(lst[i], i) for i in range(len(lst))]
    new.sort()
    ans = [0 for _ in range(len(lst))]
    trace = []
    k = 0
    for i in range(len(lst)):
        if i > 0 and new[i][0] > new[i-1][0]:
            k += 1
        ans[new[i][1]] = k
        if trace and trace[-1] == new[i][0]: continue
        trace.append(new[i][0])
    if typ: return ans, trace
    return ans