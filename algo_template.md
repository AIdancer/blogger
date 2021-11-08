### 前向星 & spfa & 负环
```C++
// POJ3259

#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

const int N = 2000;
const int M = 30000;

int e_cnt;
int F, n, m, w;
int h[N], e[M], t[M], nxt[M];
bool inqueue[N];
int dis[N];
int node_cnt[N];

void add_edge(int u, int v, int w) {
    e[e_cnt] = v;
    t[e_cnt] = w;
    nxt[e_cnt] = h[u];
    h[u] = e_cnt++;
}

bool spfa_check(int source) {
    queue<int> q;
    memset(inqueue, 0, sizeof(inqueue));
    memset(node_cnt, 0, sizeof(node_cnt));
    q.push(source);
    for (int i = 0; i <= n; i++) dis[i] = 0x1ffffff;
    int u, v;
    dis[source] = 0;
    while (!q.empty()) {
        u = q.front();
        for (int i = h[u]; i != -1; i = nxt[i]) {
            v = e[i];
            if (dis[v] > dis[u] + t[i]) {
                dis[v] = dis[u] + t[i];
                if (!inqueue[v]) {
                    q.push(v);
                    inqueue[v] = true;
                }
            }
        }
        q.pop();
        inqueue[u] = false;
        node_cnt[u] += 1;
        if (node_cnt[u] > n) {
            return true;
        }
    }
    return false;
}

int main() {
    scanf("%d", &F);
    int s, e, t;
    while (F--) {
        memset(h, -1, sizeof(h));
        e_cnt = 0;
        scanf(" %d %d %d", &n, &m, &w);
        for (int i = 0; i < m; i++) {
            scanf(" %d %d %d", &s, &e, &t);
            add_edge(s, e, t);
            add_edge(e, s, t);
        }
        for (int i = 0; i < w; i++) {
            scanf(" %d %d %d", &s, &e, &t);
            add_edge(s, e, -t);
        }
        for (int i = 1; i <= n; i++) {
            add_edge(0, i, 0);
        }
        if (spfa_check(0)) {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }
    return 0;
}
```


### C++优先队列 自定义比较函数
```C++

#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

struct Node {
    int x, y;
    Node() { x = 0, y = 0; }
    Node(int _x, int _y) :x(_x), y(_y) {}
};

struct cmp {
    bool operator() (const Node& a, const Node& b) {
        if (a.x == b.x) return a.y > b.y;
        else return a.x > b.x;
    }
};

priority_queue<Node, vector<Node>, cmp> q;

int main() {
    Node a(1, 2), b(1, 3), c(2, 5), d(-1, 3);
    Node val;
    q.push(a); q.push(b); q.push(c); q.push(d);
    while (!q.empty()) {
        val = q.top();
        q.pop();
        printf("%d %d\n", val.x, val.y);
    }
    return 0;
}
// 输出 -1,3   1,2    1,3   2,5
// 优先队列默认为大顶堆，此处定义新的比较函数cmp，使队列变为小顶堆
```

### 最短路径
```C++
// floyd所有点对最短路径
const int N = 105;

int c[N][N];
int n;

void floyd() {
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            if ((i == k) || (c[i][k] == -1)) continue;
            for (int j = 1; j <= n; j++) {
                if ((k == j) || (c[k][j] == -1)) continue;
                if ((i != j) && (j != k) && (i != k)) {
                    if ((c[i][j] == -1) || (c[i][j] > c[i][k] + c[k][j])) {
                        c[i][j] = c[i][k] + c[k][j];
                    }
                }
            }
        }
    }
}



```

### 最小生成树 & 并查集 & kruskal
```C++
//POJ 1287

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int N = 70;

struct Edge {
	int a, b, c;
	Edge() {}
	Edge(int _a, int _b, int _c) :a(_a), b(_b), c(_c) {}
};

bool cmp(const Edge& first, const Edge& second) {
	return first.c < second.c;
}

int fa[N];
int n, m;

vector<Edge> vec;

int get_father(int x) {
	if (fa[x] != x)
		fa[x] = get_father(fa[x]);
	return fa[x];
}

void union_set(int x, int y) {
	int fax, fay;
	fax = get_father(x);
	fay = get_father(y);
	if (fax != fay) {
		fa[fay] = fax;
	}
}

int get_kruskal_value() {
	int res = 0;
	for (int i = 1; i <= n; i++) fa[i] = i;
	int edges = vec.size();
	int fa, fb;
	Edge e;
	for (int i = 0; i < edges; i++) {
		e = vec[i];
		fa = get_father(e.a);
		fb = get_father(e.b);
		if (fa != fb) {
			res += e.c;
			union_set(fa, fb);
		}
	}
	return res;
}

int main() {
	int a, b, c;
	while (scanf(" %d", &n) != EOF) {
		if (n == 0) break;
		vec.clear();
		scanf(" %d", &m);
		for (int i = 0; i < m; i++) {
			scanf(" %d %d %d", &a, &b, &c);
			vec.push_back(Edge(a, b, c));
		}
		sort(vec.begin(), vec.end(), cmp);
		int res = get_kruskal_value();
		printf("%d\n", res);
	}
	return 0;
}
```

### 最小生成树(Prim)
```C++
// POJ1287

#include <cstdio>
#include <cstring>

using namespace std;

const int N = 70;

int dist[N];
int n, m;
int g[N][N];
int a, b, c;
bool visited[N];

int get_prim_value() {
	memset(visited, false, sizeof(visited));
	int total = 0;
	for (int i = 1; i <= n; i++) g[i][i] = 0;
	for (int i = 1; i <= n; i++) {
		if (g[1][i] != -1) {
			dist[i] = g[1][i];
		}
	}
	visited[1] = true;
	for (int i = 1; i < n; i++) {
		int mm = -1, index = -1;
		for (int j = 1; j <= n; j++) {
			if ((!visited[j]) && ((mm == -1) || (mm > dist[j])) ) {
				index = j;
				mm = dist[index];
			}
		}
		visited[index] = true;
		total += mm;
		for (int j = 1; j <= n; j++) {
			if ((!visited[j]) && (g[index][j] != -1) && ((dist[j] == -1) || (dist[j] > g[index][j]))) {
				dist[j] = g[index][j];
			}
		}
	}
	return total;
}

int main() {
	while (scanf(" %d", &n) != EOF) {
		if (n == 0) break;
		scanf(" %d", &m);
		memset(dist, -1, sizeof(dist));
		memset(g, -1, sizeof(g));
		for (int i = 0; i < m; i++) {
			scanf(" %d %d %d", &a, &b, &c);
			if ((g[a][b] == -1) || (g[a][b] > c)) {
				g[a][b] = g[b][a] = c;
			}
		}
		int ans = get_prim_value();
		printf("%d\n", ans);
	}
	return 0;
}
``` 


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
