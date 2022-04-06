```python

import queue


class Node:
    def __init__(self):
        # if label is 0, it represent a middle node; if label is 1, it represent a tail node of word.
        self.label = None
        # each child links to the next node in matching.
        self.child = {}
        # fail point to the longest common prefix node if matching is failed.
        self.fail = None


class AhoCorasick:
    def __init__(self):
        self.root = Node()
        self.character_set = set()
        self.is_build = False

    def insert_word(self, word):
        cur = self.root
        for c in word:
            if c not in self.character_set:
                self.character_set.add(c)
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.label = 1

    def build_ac(self):
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            u = q.get()
            for c in self.character_set:
                if c in u.child:
                    v = u.child[c]
                    if (u == self.root):
                        v.fail = self.root
                    else:
                        p = u.fail
                        while (c not in p.child) and (p != self.root):
                            p = p.fail
                        if c in p.child:
                            v.fail = p.child[c]
                        else:
                            v.fail = self.root
                    q.put(v)
        self.is_build = True

    def check_text(self, text):
        n = len(text)
        u = self.root
        ans = 0
        for i in range(n):
            c = text[i]
            while (u is not self.root) and (c not in u.child):
                u = u.fail
            if c in u.child:
                u = u.child[c]
                if u.label == 1:
                    ans += 1
        return ans


if __name__ == '__main__':
    ac = AhoCorasick()
    ac.insert_word('hello')
    ac.insert_word('world')
    ac.build_ac()
    print(ac.is_build)
    line = 'hello, world.'
    ans = ac.check_text(line)
    print(ans)
```
