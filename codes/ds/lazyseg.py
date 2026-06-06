mod = 998244353

class LazySeg():
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1<<((self.n-1).bit_length())
        self.h = self.size.bit_length() - 1
        self.seg = [0]*(2*self.size)
        self.lazya = [1]*self.size
        self.lazyb = [0]*self.size
        base = self.size
        for i, v in enumerate(arr):
            self.seg[base + i] = v % mod
        for i in range(self.size-1, 0, -1):
            self.seg[i] = (self.seg[2*i] + self.seg[2*i+1]) % mod

    def _apply(self, i, a, b, leng):
        self.seg[i] = (a*self.seg[i] + b*leng) % mod
        if i < self.size:
            self.lazya[i] = (a * self.lazya[i]) % mod
            self.lazyb[i] = (a * self.lazyb[i] + b) % mod

    def _push(self, idx):
        for s in range(self.h, 0, -1):
            i = idx >> s
            a, b = self.lazya[i], self.lazyb[i]
            if a != 1 or b != 0:
                tmp = 1 << (s-1)
                self._apply(2*i, a, b, tmp)
                self._apply(2*i+1, a, b, tmp)
                self.lazya[i] = 1
                self.lazyb[i] = 0
        return

    def _pull(self, idx):
        leng = 1
        while idx > 1:
            idx >>= 1
            leng <<= 1
            self.seg[idx] = (self.seg[2*idx] + self.seg[2*idx+1]) % mod
            a, b = self.lazya[idx], self.lazyb[idx]
            if a != 1 or b != 0:
                self.seg[idx] = (a*self.seg[idx] + b * leng) % mod


    def update(self, left, right, a, b):
        # [left, right] update
        if left > right: return
        l0, r0 = left + self.size, right + 1 + self.size
        self._push(l0)
        self._push(r0-1)
        leng = 1
        l, r = l0, r0
        while l < r:
            if l&1:
                self._apply(l, a, b, leng)
                l += 1
            if r&1:
                r -= 1
                self._apply(r, a, b, leng)
            l >>= 1
            r >>= 1
            leng <<= 1
        self._pull(l0)
        self._pull(r0-1)
        return

    def range_sum(self, left, right):
        # [left, right] sum
        if left > right: return 0
        l, r = left + self.size, right + 1 + self.size
        self._push(l)
        self._push(r-1)
        lsum, rsum = 0, 0
        while l < r:
            if l&1:
                lsum = (lsum + self.seg[l]) % mod
                l += 1
            if r&1:
                r -= 1
                rsum = (rsum + self.seg[r]) % mod
            l >>= 1
            r >>= 1
        return (lsum + rsum) % mod