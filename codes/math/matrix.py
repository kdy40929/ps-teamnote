def zero(n):
    return [[0]*n for _ in range(n)]

def eye(n):
    E = [[0]*n for _ in range(n)]
    for i in range(n):
        E[i][i] = 1
    return E

def add(A, B, mod):
    C = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = (A[i][j] + B[i][j]) % mod
    return C

def multiply(A, B, mod):
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= mod
    return C

def power(mat, exp, mod):
    n = len(mat)
    ans = eye(n)
    base = mat
    while exp:
        if exp&1: ans = multiply(ans, base, mod)
        base = multiply(base, base, mod)
        exp >>= 1
    return ans

def powsum(mat, exp, mod):
    # mat^exp, eye + mat + ... + mat^(exp-1)
    n = len(mat)
    m1, m2 = eye(n), zero(n)
    base1, base2 = [x[:] for x in mat], eye(n)
    while exp:
        if exp&1:
            m2 = add(m2, multiply(m1, base2, mod), mod)
            m1 = multiply(m1, base1, mod)
        base2 = multiply(base2, add(eye(n), base1, mod), mod)
        base1 = multiply(base1, base1, mod)
        exp >>= 1
    return (m1, m2)