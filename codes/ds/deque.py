from collections import deque

n, l = map(int, input().split())
arr = [*map(int, input().split())]
Q = deque()
for i in range(n):
    while Q and Q[-1][0] >= arr[i]:
        Q.pop()
    Q.append((arr[i], i))
    if Q[0][1] <= i-l:
        Q.popleft()
    print(Q[0][0], end=' ')