### KMP算法（POJ 3461）
```C++
#include <iostream>
#include <cstring>
using namespace std;

const int M = 10005;
const int N = 1000005;

int nxt[M];
char W[M];
char T[N];

void getNext(char* s) {
	int n = strlen(s);
	memset(nxt, -1, sizeof(nxt));
	nxt[0] = -1;
	int j = -1;
	for (int i = 1; i < n; i++) {
		while ((j >= 0) && (s[j + 1] != s[i])) j = nxt[j];
		if (s[j + 1] == s[i]) nxt[i] = ++j;
	}
}

void KMP() {
	int n = strlen(T), i = 0, j = -1, count = 0;
	int mlen = strlen(W);
	while(i < n) {
		if ((T[i] == W[j+1])) {
			++i;
			++j;
		}
		else {
			if (j == -1) ++i;
			else j = nxt[j];
		}
		if (j == (mlen - 1)) ++count;
	}
	printf("%d\n", count);
}

int main() {
	int c;
	scanf("%d", &c);
	while (c--) {
		scanf(" %s", W);
		scanf(" %s", T);
		getNext(W);
		KMP();
	}
	return 0;
}

```

### Trie树（POJ 3630）
```C++
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MaxTreeNodeNum = 100000;

struct Node {
	int count;
	int ch[10];
	void init() {
		count = 0;
		memset(ch, -1, sizeof(ch));
	}
};
Node tree[MaxTreeNodeNum];
int ncnt;
bool ans;

void insert(char *s) {
	int n = strlen(s);
	char c;
	int index;
	int u = 0;
	for (int i = 0; i < n; i++) {
		c = s[i];
		index = c - '0';
		if (tree[u].count > 0) ans = false;
		if (tree[u].ch[index] == -1) {
			++ncnt;
			tree[ncnt].init();
			tree[u].ch[index] = ncnt;
			u = ncnt;
		}
		else {
			u = tree[u].ch[index];
		}
	}
	tree[u].count += 1;
	for (int i = 0; i < 10; i++) {
		if (tree[u].ch[i] != -1) {
			ans = false;
		}
	}
}

void init_tree() {
	ncnt = 0;
	tree[0].init();
}

int main() {
	int t, n;
	char phone[11];
	scanf("%d", &t);
	while (t--) {
		scanf(" %d", &n);
		ans = true;
		init_tree();
		for (int i = 0; i < n; i++) {
			scanf(" %s", phone);
			if (ans)
				insert(phone);
		}
		if (ans) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	return 0;
}
```

### AC自动机/Trie图/DFA（POJ 1204）
``` C++
#include <iostream>
#include <cstring>
#include <string>
#include <queue>
using namespace std;

const int MaxCharacterLimit = 26;
const int MaxTreeNodeLimit = 100000;

const int tx[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int ty[8] = {0, 1, 1, 1, 0, -1, -1, -1};

struct Node {
	int label;
	int ch[MaxCharacterLimit];
	int fail;
	void init() {
		label = -1;
		fail = -1;
		memset(ch, -1, sizeof(ch));
	}
};

int node_cnt;
Node tree[MaxTreeNodeLimit];

int L, C, W;
char cmap[1002][1002];
char words[1001][1001];

queue<int> q;

int ans[1001][3];

void init_tree() {
	node_cnt = 0;
	tree[0].init();
}

void insert(char* str, int label) {
	int n = strlen(str);
	int u = 0;
	int index;
	for (int i = n - 1; i >= 0; i--) {
		index = str[i] - 'A';
		if (tree[u].ch[index] == -1) {
			++node_cnt;
			tree[node_cnt].init();
			tree[u].ch[index] = node_cnt;
		}
		u = tree[u].ch[index];
	}
	tree[u].label = label;
}

void buildDFA() {
	int u, v;
	tree[0].fail = 0;
	while (!q.empty()) q.pop();
	q.push(0);
	while (!q.empty()) {
		u = q.front();
		for (int i = 0; i < MaxCharacterLimit; i++) {
			if (tree[u].ch[i] != -1) {
				v = tree[u].ch[i];
				if (u == 0) {
					tree[v].fail = 0;
				}
				else {
					int p = tree[u].fail;
					while ((tree[p].ch[i] == -1) && (p != 0)) p = tree[p].fail;
					if (tree[p].ch[i] != -1) tree[v].fail = tree[p].ch[i];
					else tree[v].fail = 0;
				}
				q.push(v);
			}
		}
		q.pop();
	}
}

void update(int w, int x, int y, int dir) {
	if ((ans[w][0] == -1) || (x < ans[w][0]) || ((x == ans[w][0]) && (y < ans[w][1]))) {
		ans[w][0] = x;
		ans[w][1] = y;
		ans[w][2] = dir;
	}
}

void check(int x, int y, int dir, int dir_out) {
	int px = x, py = y;
	int u = 0;
	char c;
	int index;
	while ((px >= 0) && (px < L) && (py >= 0) && (py < C)) {
		c = cmap[px][py];
		index = c - 'A';
		while ((u != 0) && (tree[u].ch[index] == -1)) {
			u = tree[u].fail;
		}
		if (tree[u].ch[index] != -1) {
			u = tree[u].ch[index];
			int temp = u;
			while (temp != 0) {
				if (tree[temp].label != -1)
					update(tree[temp].label, px, py, dir_out);
				temp = tree[temp].fail;
			}
		}
		px += tx[dir];
		py += ty[dir];
	}
}

int main() {
	while (scanf("%d %d %d", &L, &C, &W) != EOF) {
		init_tree();
		for (int i = 0; i < L; i++) {
			scanf(" %s", cmap[i]);
		}

		for (int i = 0; i < W; i++) {
			scanf(" %s", words[i]);
			insert(words[i], i);
		}
		buildDFA();
		memset(ans, -1, sizeof(ans));
		for (int i = 0; i < L; i++) {
			check(i, 0, 1, 5);
			check(i, 0, 2, 6);
			check(i, 0, 3, 7);
			check(i, C - 1, 5, 1);
			check(i, C - 1, 6, 2);
			check(i, C - 1, 7, 3);
		}
		for (int i = 0; i < C; i++) {
			check(0, i, 3, 7);
			check(0, i, 4, 0);
			check(0, i, 5, 1);
			check(L - 1, i, 0, 4);
			check(L - 1, i, 1, 5);
			check(L - 1, i, 7, 3);
		}
		for (int i = 0; i < W; i++) {
			printf("%d %d %c\n", ans[i][0], ans[i][1], (char)ans[i][2] + 'A');
		}
	}
	return 0;
}
```
