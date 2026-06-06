def euler_phi(n):
    if n < 4: return n - 1
    ans = n
    p = 2
    while p*p <= n:
        if n % p == 0:
            ans = ans // p * (p - 1)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans = ans // n * (n - 1)
    return ans