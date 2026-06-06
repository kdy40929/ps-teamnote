from bisect import bisect_left
INF = 10**18

n = int(input())
arr = [*map(int,input().split())]
leng = [-INF]
dp = [0]*n
for i in range(n):
    dp[i] = bisect_left(leng, arr[i])
    if dp[i] == len(leng):
        leng.append(arr[i])
    else:
        leng[dp[i]] = arr[i]
tmp = max(dp)
print(tmp)
lis = []
for i in range(n-1, -1, -1):
    if tmp == dp[i]:
        tmp -= 1
        lis.append(arr[i])
print(*lis[::-1])