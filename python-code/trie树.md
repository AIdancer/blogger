```python

class Node:
    def __init__(self):
        self.label = None
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node()
        self.character_set = set()
        self.index_count = 0

    def insert_word(self, word):
        cur = self.root
        for c in word:
            if c not in self.character_set:
                self.character_set.add(c)
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.label = self.index_count
        self.index_count += 1

    def get_kpi_index(self, kpi_name):
        n = len(kpi_name)
        ret = -1
        u = self.root
        for i in range(n):
            c = kpi_name[i]
            if c in u.child:
                u = u.child[c]
                if u.label is not None:
                    ret = u.label
            else:
                break
        return ret


if __name__ == '__main__':
    words = ['hello', 'word', 'haha.haha']
    trie = Trie()
    for w in words:
        trie.insert_word(w)
    print(w, trie.index_count)
    for w in words:
        print(trie.get_kpi_index(w))
    print(trie.get_kpi_index('hahaha'))
```
