def combination(n, k, p):
    if k < 0 or k > n: return 0
    numer, denom = 1, 1
    if 2*k > n: k = n-k
    for i in range(n, n-k, -1):
        numer = (numer * i) % p
    for j in range(1, k+1):
        denom = (denom * j) % p
    return numer * pow(denom, -1, p) % p

def lucas_comb(n, k, p):
    ans = 1
    while n > 0 or k > 0:
        ans = ans * combination(n%m, k%m, m) % m
        n //= m; k //= m
    return ans