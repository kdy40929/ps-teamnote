plist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
def isprime(k):
    if k <= 37 and k in plist: return 1
    elif k <= 37: return 0
    tmp = k-1
    cnt = 0
    while tmp%2 == 0:
        tmp //= 2
        cnt += 1
    s,t = cnt, tmp
    for p in plist:
        tmp = pow(p, t, k)
        if tmp == 1: continue
        flag = 0
        for _ in range(s):
            if tmp == k-1:
                flag = 1; break
            tmp = pow(tmp, 2, k)
        if flag == 0: return 0
    return 1

def f(x,n):
    return (x*x+1)%n

def polar(n, x):
    tmp = x
    if isprime(n): return n
    for i in plist:
        if n%i == 0: return i
    y = x
    gcd = 1
    while gcd == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        gcd = math.gcd(abs(x-y), n)
    if gcd == n:
        return polar(n, tmp+1)
    if isprime(gcd):
        return gcd
    return polar(gcd, 2)