def makez(s):
    n = len(s)
    l, r = 0, 0
    z = [0]*n; z[0] = n
    for i in range(1, n):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        while i+z[i] < n and s[i+z[i]] == s[z[i]]:
            z[i] += 1
        if r < i+z[i]-1:
            l, r = i, i+z[i]-1
    return z