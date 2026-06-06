# BOJ 22940
n = int(input())
eq = [[*map(int, input().split())] for _ in range(n)]
for k in range(n):
    for i in range(k+1, n):
        for j in range(n, k-1, -1):
            eq[i][j] = eq[k][k] * eq[i][j] - eq[i][k] * eq[k][j]
ans = [0]*n
for i in range(n-1, -1, -1):
    tmp = eq[i][n]
    for j in range(i+1, n):
        tmp -= eq[i][j] * ans[j]
    ans[i] = tmp//eq[i][i]
print(*ans)