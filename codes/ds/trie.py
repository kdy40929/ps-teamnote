class Trie:
    def __init__(self, alpha, max_node, func):
        # alpha: the number of characters
        # max_node: the maximum number of nodes
        # func: function that translates characters to index num
        self.alpha = alpha
        self.trie = [0] * (alpha * max_node)
        self.cnt = [0] * max_node
        self.end = [0] * max_node
        self.num = 0
        self.f = func

    def insert(self, word):
        i = 0
        self.cnt[i] += 1
        for ch in word:
            idx = self.f(ch)
            pt = self.alpha * i + idx
            if self.trie[pt] == 0:
                self.num += 1
                self.trie[pt] = self.num
            i = self.trie[pt]
            self.cnt[i] += 1
        self.end[i] += 1