class Node:
    def __init__(self, w=0):
        self.l = self.r = self.m = max(0, w)
        self.s = w

def merge(n1, n2):
    n3 = Node()
    n3.l = max(n1.l, n1.s + n2.l)
    n3.r = max(n2.r, n2.s + n1.r)
    n3.m = max(n1.m, n2.m, n1.r + n2.l)
    n3.s = n1.s + n2.s
    return n3

def rev(n1):
    n1.l, n1.r = n1.r, n1.l
    return n1

class MineSeg:
    def __init__(self, arr):
        k = len(arr) - 1
        self.h = k.bit_length()
        self.size = 1<<self.h
        self.seg = [Node(0) for _ in range(2*self.size)]
        self.lazy = [-INF]*(self.size)
        for i in range(len(arr)):
            self.seg[self.size + i] = Node(arr[i])
        for i in range(self.size-1, 0, -1):
            self.seg[i] = merge(self.seg[2*i], self.seg[2*i+1])

    def apply(self, idx, w):
        tmp = self.h - idx.bit_length() + 1
        self.seg[idx] = Node(w * (1<<tmp))
        if idx < self.size: self.lazy[idx] = w

    def push(self, idx):
        if self.lazy[idx] != -INF:
            self.apply(2*idx, self.lazy[idx])
            self.apply(2*idx+1, self.lazy[idx])
        self.lazy[idx] = -INF

    def update(self, l, r, w):
        l += self.size
        r += self.size
        for i in range(self.h, 0, -1):
            if l>>i<<i != l:
                self.push(l>>i)
            if (r+1)>>i<<i != r+1:
                self.push(r>>i)
        l0, r0 = l, r
        while l <= r:
            if l&1:
                self.apply(l, w)
                l += 1
            if ~r&1:
                self.apply(r, w)
                r -= 1
            l >>= 1; r >>= 1
        l, r = l0, r0
        for i in range(1, self.h+1):
            if l>>i<<i != l:
                k = l>>i
                self.seg[k] = merge(self.seg[2*k], self.seg[2*k+1])
            if (r+1)>>i<<i != r+1:
                k = r>>i
                self.seg[k] = merge(self.seg[2*k], self.seg[2*k+1])
        return

    def query(self, l, r):
        l += self.size
        r += self.size
        for i in range(self.h, 0, -1):
            if l>>i<<i != l:
                self.push(l>>i)
            if (r+1)>>i<<i != r+1:
                self.push(r>>i)
        nl, nr = Node(), Node()
        while l <= r:
            if l&1:
                nl = merge(nl, self.seg[l])
                l += 1
            if ~r&1:
                nr = merge(self.seg[r], nr)
                r -= 1
            l >>= 1; r >>= 1
        return merge(nl, nr)