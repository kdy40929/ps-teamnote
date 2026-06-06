def search(val, st):
    left, right = 0, len(st)-1
    while left + 1 < right:
        mid = (left + right)//2
        t1 = st[mid][0] * val + st[mid][1]
        t2 = st[mid+1][0] * val + st[mid+1][1]
        if t1 < t2: right = mid
        else: left = mid+1
    t1 = st[left][0] * val + st[left][1]
    t2 = st[right][0] * val + st[right][1]
    return left if t1 < t2 else right

def check(l1, l2, l3):
    return (l3[1]-l2[1]) * (l1[0]-l2[0]) <= (l2[1]-l1[1]) * (l2[0]-l3[0])

n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
dp = [0]*n
st = []
st.append((b[0], 0))
for i in range(1, n):
    idx = search(a[i], st)
    dp[i] = st[idx][0] * a[i] + st[idx][1]
    while len(st) > 1 and check(st[-2], st[-1], (b[i], dp[i])):
        st.pop()
    st.append((b[i], dp[i]))
print(dp[-1])