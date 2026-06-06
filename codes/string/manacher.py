def manacher(s):
    n = len(s)
    r, ctr = 0, 0
    arr = [0]*n
    for i in range(n):
        if i <= r:
            arr[i] = min(arr[2*ctr-i], r-i)
        while i-arr[i] >= 1 and i+arr[i] < n-1 and s[i-arr[i]-1] == s[i+arr[i]+1]:
            arr[i] += 1
        if r < i+arr[i]:
            r, ctr = i+arr[i], i
    return arr