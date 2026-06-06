class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)

    def update(self, idx, val):
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    def count(self, idx):  # sum [1..idx]
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def kth(self, k):
        # smallest idx with prefix sum >= k
        if k <= 0: return 0
        if self.count(self.n) < k: return self.n + 1
        idx = 0
        step = 1 << (self.n.bit_length() - 1)
        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            step >>= 1
        return idx + 1