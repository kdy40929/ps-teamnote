from collections import deque

class Aho_Corasick:
    def __init__(self, alpha, func, patterns):
        self.alpha = alpha
        self.f = func
        self.patterns = patterns

        max_node = sum(len(p) for p in patterns) + 1
        self.trie = [0] * (alpha * max_node)
        self.fail = [0] * max_node
        self.out = [-1] * max_node
        self.end = [0] * max_node

        self.num = 0
        self.occcnt = [0] * max_node # count the occurence
        self.out_link = [-1] * max_node # linked list
        self.items = []
        
        for pid, pattern in enumerate(patterns):
            self.insert(pattern, pid)
        self.build()
        
    def insert(self, word, pid):
        i = 0
        for ch in word:
            idx = self.f(ch)
            pos = self.alpha * i + idx
            if self.trie[pos] == 0:
                self.num += 1
                self.trie[pos] = self.num
            i = self.trie[pos]
        self.end[i] += 1
        prev = self.out[i]
        self.items.append((pid, len(word), prev))
        self.out[i] = len(self.items) - 1

    def build(self):
        q = deque()
        for c in range(self.alpha):
            v = self.trie[c]
            if v != 0:
                self.fail[v] = 0
                q.append(v)
        self.occcnt[0] = self.end[0]
        self.out_link[0] = -1
        
        while q:
            cur = q.popleft()
            fcur = self.fail[cur]
            self.occcnt[cur] = self.end[cur] + self.occcnt[fcur]
            self.out_link[cur] = fcur if self.out[fcur] != -1 else self.out_link[fcur]
            for c in range(self.alpha):
                pos = self.alpha * cur + c
                nxt = self.trie[pos]
                if nxt != 0:
                    self.fail[nxt] = self.trie[self.alpha * fcur + c]
                    q.append(nxt)
                else:
                    self.trie[pos] = self.trie[self.alpha * fcur + c]

    def findall(self, text):
        ans = []
        i = 0
        for pos, ch in enumerate(text):
            idx = self.f(ch)
            i = self.trie[self.alpha * i + idx]
            node = i
            while node != -1:
                head = self.out[node]
                while head != -1:
                    pid, leng, nxt = self.items[head]
                    ans.append((pos-leng+1, pos, pid))
                    head = nxt
                node = self.out_link[node]
        return ans