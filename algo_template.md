### 手撸快速排序
```c++
# define _CRT_SECURE_NO_WARNINGS

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long LL;

const int N = 200005;

int num[100000];

int partition(int a[], int low, int high) {
    int key, i, j;
    key = a[low];
    i = low;
    j = high;
    while (i < j) {
        while ((i < j) && (a[j] >= key)) j--;
        if (i < j) a[i] = a[j];
        while ((i < j) && (a[i] <= key)) i++;
        if (i < j) a[j] = a[i];
    }
    a[i] = key;
    return i;
}

void quick_sort(int a[], int low, int high) {
    if (low >= high) return;
    int mid;
    mid = partition(a, low, high);
    quick_sort(a, low, mid - 1);
    quick_sort(a, mid + 1, high);
}

void solve() {
    int n = 30;
    for (int i = 0; i < n; i++)
        num[i] = rand() % 50;
    printf("origin:\n");
    for (int i = 0; i < n; i++) printf("%d ", num[i]); printf("\n");
    quick_sort(num, 0, n-1);
    printf("sorted:\n");
    for (int i = 0; i < n; i++) printf("%d ", num[i]); printf("\n");
}

int main() {
    solve();
    return 0;
}
```

### Tarjan求解LCA | ural1471
```C++
#define _CRT_SECURE_NO_WARNINGS

#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <functional>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 50005;

int n, m;
int depth[N];
bool visit[N];
vector<pair<int, int>> g[N];
vector<int> querys[N];
map<pair<int, int>, int> res;
vector<pair<int, int>> query_records;

int fa[N];

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

void tarjan(int u, int p, int d) {
    depth[u] = d;
    int ch_size = g[u].size();
    pair<int, int> v;
    for (int i = 0; i < ch_size; i++) {
        v = g[u][i];
        if (v.first == p) continue;
        tarjan(v.first, u, d + v.second);
        union_set(u, v.first);
    }
    visit[u] = true;
    ch_size = querys[u].size();
    int node_v;
    for (int i = 0; i < ch_size; i++) {
        node_v = querys[u][i];
        if (visit[node_v]) {
            int lca = get_father(node_v);
            int ans = depth[u] + depth[node_v] - depth[lca] * 2;
            res[make_pair(u, node_v)] = ans;
            res[make_pair(node_v, u)] = ans;
        }
    }
}

void solve() {
    int a, b, w;
    scanf("%d", &n);
    for (int i = 1; i < n; i++) {
        scanf(" %d %d %d", &a, &b, &w);
        g[a].push_back(make_pair(b, w));
        g[b].push_back(make_pair(a, w));
    }
    scanf(" %d", &m);
    for (int i = 0; i < m; i++) {
        scanf(" %d %d", &a, &b);
        querys[a].push_back(b);
        querys[b].push_back(a);
        query_records.push_back(make_pair(a, b));
    }
    for (int i = 0; i < n; i++) fa[i] = i;
    for (int i = 0; i < n; i++) visit[i] = false;
    tarjan(0, -1, 0);
    for (int i = 0; i < m; i++) {
        printf("%d\n", res[query_records[i]]);
    }
}

int main(int argc, const char* argv[]) {
    solve();
    return 0;
}
```

### 求第k大数
```C++
unsigned int a[250005];

unsigned int select_k(unsigned int a[], int l, int r, int index) {
    if (l == r) return a[l];
    int i = l, j = r;
    unsigned int x = a[l];
    while (i < j) {
        while ((x <= a[j]) && (i < j)) j--;
        a[i] = a[j];
        while ((x >= a[i]) && (i < j)) i++;
        a[j] = a[i];
    }
    a[i] = x;
    if (i == index) return a[i];
    else if (i < index) return select_k(a, i + 1, r, index);
    else return select_k(a, l, i - 1, index);
}
```

### 线段树 codeforces|Stone Age Problem
```c++
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;
 
typedef long long LL;
 
const int N = 200005;
 
struct node {
    LL sum;
    int lazy;
    int l, r;
} tree[N<<2];
 
int n, q, a[N];
 
void build(int u, int l, int r) {
    tree[u].l = l;
    tree[u].r = r;
    if (l == r) {
        tree[u].sum = a[l];
        tree[u].lazy = a[l];
        return;
    }
    int lch, rch;
    lch = u << 1;
    rch = lch + 1;
    int mid = (l+r) >> 1;
    build(lch, l, mid);
    build(rch, mid+1, r);
    tree[u].lazy = -1;
    tree[u].sum = tree[lch].sum + tree[rch].sum;
}
 
void update(int u, int l, int r, int val) {
    if (tree[u].l == l && tree[u].r == r) {
        tree[u].sum = LL(val) * (r - l + 1);
        tree[u].lazy = val;
        return;
    } else {
        int lch, rch;
        lch = u << 1;
        rch = lch + 1;
        int mid = (tree[u].l + tree[u].r) >> 1;
        if (tree[u].lazy != -1) {
            update(lch, tree[lch].l, tree[lch].r, tree[u].lazy);
            update(rch, tree[rch].l, tree[rch].r, tree[u].lazy);
            tree[u].lazy = -1;
        }
        if (r <= mid) {
            update(lch, l, r, val);
        } else if (l > mid) {
            update(rch, l, r, val);
        } else {
            update(lch, l, mid, val);
            update(rch, mid+1, r, val);
        }
        tree[u].sum = tree[lch].sum + tree[rch].sum;
    }
}
 
void test_case(int t) {
    int tt, pos, x;
    scanf(" %d %d", &n, &q);
    for (int i = 1; i <= n; i++) scanf(" %d", a+i);
    build(1, 1, n);
    while (q--) {
        scanf(" %d", &tt);
        if (tt == 1) {
            scanf(" %d %d", &pos, &x);
            update(1, pos, pos, x);
        } else if (tt == 2) {
            scanf(" %d", &x);
            update(1, 1, n, x);
        }
        printf("%lld\n", tree[1].sum);
    }
}
 
int main(int argc, const char * argv[]) {
    test_case(0);
    return 0;
}
```


### c++ multi set使用
```c++
// codeforces 1672D
// 注意multiset的erase(val)方法会删除所有值为val的数据，要想只删除一个，需要find到iterator，然后erase(iterator)
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
using std::max;
using std::min;


typedef long long LL;

const int N = 200005;

int n, a[N], b[N];

void test_case(int case_num) {
    scanf(" %d", &n);
    multiset<int> free_num;
    multiset<int>::iterator it;
    for (int i = 0; i < n; i++) scanf(" %d", a + i);
    for (int i = 0; i < n; i++) scanf(" %d", b + i);
    int i = n-1, j = n-1;
    bool flag = true;
    while (i >= 0 && j >= 0) {
        while (j - 1 >= 0 && (b[j] == b[j - 1])) {
            free_num.insert(b[j]);
            --j;
        }
        if (a[i] == b[j]) {
            --i;
            --j;
        }
        else {
            it = free_num.find(a[i]);
            if (it == free_num.end()) {
                flag = false;
                break;
            }
            else {
                free_num.erase(it);
                --i;
            }
        }
    }
    if (flag) printf("yes\n");
    else printf("no\n");
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
        test_case(i);
    return 0;
}
```


### 扩展欧几里得 求解模线性方程 ax = b (mod n)
```c++

#include <cassert>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef long long LL;

int ext_gcd(int a, int b, int& x, int& y) {
    int d;
    if (b == 0) {
        d = a;
        x = 1; y = 0;
        return d;
    }
    else {
        d = ext_gcd(b, a % b, x, y);
        int tx, ty;
        tx = y;
        ty = x - a / b * y;
        x = tx; y = ty;
        return d;
    }
}

void mod_equation(int a, int b, int n) {
    int d, tx, ty, x0;
    d = ext_gcd(a, n, tx, ty);
    if (b % d == 0) {
        x0 = tx * (b / d);
        // 输出解系 
        for (int i = 0; i < d; i++)
            // a * x0 = b (mod n)  -->  a * (x0 + i * (n/d)) = b (mod n)
            printf("%d ", x0 + i * (n / d));
        printf("\n");
    }
    else {
        printf("no solution\n");
    }
}
```

### 扩展欧几里得 求解 ax+by=gcd(a,b)
```c++
#include <cassert>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef long long LL;

int ext_gcd(int a, int b, int& x, int& y) {
    int d;
    if (b == 0) {
        d = a;
        x = 1; y = 0;
        return d;
    }
    else {
        d = ext_gcd(b, a % b, x, y);
        int tx, ty;
        tx = y;
        ty = x - a / b * y;
        x = tx; y = ty;
        return d;
    }
}
```


### 欧拉函数求解（包括筛法）
```c++

#include <cassert>
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

typedef long long LL;

const int N = 200005;

int phi[N];

// 若gcd(a, m) == 1 则有 a^phi(m) mod m = 1

int cal_phi(int n) {
    // phi(n) = n * (p[1]-1)/p[1] * (p[2]-1)/p[2] * ... * (p[k]-1)/p[k]
    int ans = n, temp = n;
    for (int i = 2; i * i <= n; i++) {
        if (temp % i == 0) {
            ans = ans / i * (i - 1);
            while (temp % i == 0) temp /= i;
        }
    }
    if (temp > 1) ans = ans / temp * (temp - 1);
    return ans;
}

void sieve_phi() {
    for (int i = 1; i < N; i++) phi[i] = i;
    for (int i = 2; i < N; i++) {
        if (phi[i] == i) {
            phi[i] = i - 1;
            for (int j = i+i; j < N; j += i) {
                phi[j] = phi[j] / i * (i - 1);
            }
        }
    }
}
```

### 筛法求素数
```C++
#include <cassert>
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

typedef long long LL;

const int N = 20005;
bool is_prime[N];

void sieve_prime() {
    memset(is_prime, true, sizeof(is_prime));
    is_prime[1] = false;
    for (int i = 2; i < N; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j < N; j += i) is_prime[j] = false;
        }
    }
}
```


### 最大公约数|最小公倍数
```C++
// 最大公约数
int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a % b);
}

// 最小公倍数
int lcm(int a, int b) {
    int g = gcd(a, b);
    return a / g * b;
}
```

### 强连通分量|poj2186
```python
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
using std::max;
using std::min;


typedef long long LL;

const double pi = atan(1) * 4;

const int N = 10005;

// n为点数，m为边数，top为栈指针，dcnt控制深度遍历顺序，scnt为强连通分量计数器，s为栈
// scc[i]表示顶点i所属强连通分量，scc_sz[k]表示第k个强连通分量大小
int n, m, top, dcnt, scnt, d[N], low[N], s[N], scc[N], scc_sz[N];
bool instack[N]; // instack用于判断dfs过程中，某个节点是否已在栈s中，用于判断当前边是否通向父节点或者父节点子环。
vector<int> g[N];

vector<int> g2[N];
int in[N];
bool visit[N];

void tarjan(int u) {
    d[u] = low[u] = ++dcnt;
    instack[u] = true;
    s[++top] = u;
    int sz = g[u].size(), v;
    for (int i = 0; i < sz; i++) {
        v = g[u][i];
        if (!d[v]) {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        }
        else {
            if (instack[v]) {
                low[u] = min(low[u], d[v]);
            }
        }
    }
    if (d[u] == low[u]) {
        ++scnt;
        scc_sz[scnt] = 0;
        while (s[top] != u) {
            v = s[top];
            scc[v] = scnt;
            ++scc_sz[scnt];
            instack[v] = false;
            --top;
        }
        v = s[top];
        scc[v] = scnt;
        ++scc_sz[scnt];
        instack[v] = false;
        --top;
    }
}

void dfs(int u) {
    int sz = g2[u].size(), v;
    visit[u] = true;
    for (int i = 0; i < sz; i++) {
        v = g2[u][i];
        if (!visit[v]) {
            dfs(v);
        }
    }
}

void test_case(int case_num) {
    int a, b;
    scanf(" %d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        scanf(" %d %d", &a, &b);
        g[a].push_back(b);
    }
    dcnt = 0; top = 0; scnt = 0;
    for (int i = 1; i <= n; i++) { d[i] = 0; instack[i] = false; }
    for (int i = 1; i <= n; i++) {
        if (d[i] == 0)
            tarjan(i);
    }
    for (int i = 1; i <= scnt; i++) {
        in[i] = 0;
        visit[i] = false;
    }
    for (int i = 1; i <= n; i++) {
        int sz = g[i].size();
        a = i;
        for (int j = 0; j < sz; j++) {
            b = g[i][j];
            if (scc[a] != scc[b]) {
                g2[scc[b]].push_back(scc[a]);
                ++in[scc[a]];
            }
        }
    }
    int ccnt = 0, source;
    for (int i = 1; i <= scnt; i++) {
        if (in[i] == 0) {
            source = i;
            ++ccnt;
        }
    }
    if (ccnt > 1 || ccnt == 0) {
        printf("0\n");
        return;
    }
    dfs(source);
    bool flag = true;
    for (int i = 1; i <= scnt; i++) {
        if (!visit[i]) {
            flag = false;
            break;
        }
    }
    if (!flag) {
        printf("0\n");
    }
    else {
        printf("%d\n", scc_sz[source]);
    }
}

int main() {
    test_case(0);
    return 0;
}
```


### 最大流dinic
```C++

#include <cassert>
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

typedef long long LL;

const int INF = 0x7fffffff;
const int N = 105;
const int M = 20005;

int h[N];
int ecnt, u[M], v[M], w[M], nxt[M], depth[N];

void init_graph() {
    memset(h, -1, sizeof(h));
    ecnt = 0;
}

void add_edge(int a, int b, int c) {
    u[ecnt] = a; v[ecnt] = b; w[ecnt] = c; nxt[ecnt] = h[a]; h[a] = ecnt++;
    u[ecnt] = b; v[ecnt] = a; w[ecnt] = 0; nxt[ecnt] = h[b]; h[b] = ecnt++;
}

bool dinic_bfs(int source, int end) {
    queue<int> q;
    memset(depth, -1, sizeof(depth));
    depth[source] = 0;
    q.push(source);
    int a, b, c;
    while (!q.empty()) {
        a = q.front(); q.pop();
        for (int i = h[a]; i != -1; i = nxt[i]) {
            b = v[i];
            c = w[i];
            if ((depth[b] == -1) && (c > 0)) {
                depth[b] = depth[a] + 1;
                q.push(b);
            }
        }
    }
    if (depth[end] == -1) return false;
    else return true;
}

int dinic_dfs(int source, int end, int maxflow) {
    int temp_flow;
    if (source == end) {
        return maxflow;
    }
    int sum_flow = 0;
    int a, b, c;
    for (int i = h[source]; i != -1; i = nxt[i]) {
        a = u[i]; b = v[i]; c = w[i];
        if ((depth[b] == depth[a] + 1) && (c > 0)) {
            temp_flow = dinic_dfs(b, end, min(maxflow - sum_flow, c));
            if (temp_flow > 0) {
                sum_flow += temp_flow;
                w[i] -= temp_flow;
                w[i ^ 1] += temp_flow;
                if (maxflow == sum_flow) break;
            }
        }
    }
    return sum_flow;
}

int dinic(int source, int end) {
    int ans = 0;
    while (dinic_bfs(source, end)) {
        int new_flow = 0;
        while (new_flow = dinic_dfs(source, end, INF)) {
            ans += new_flow;
        }
    }
    return ans;
}

int m, n, P[1005], A, B, K, last[1005];

void test_case() {
    init_graph();
    memset(last, -1, sizeof(last));
    scanf(" %d %d", &m, &n);
    for (int i = 1; i <= m; i++) scanf(" %d", P + i);
    for (int i = 1; i <= n; i++) {
        scanf(" %d", &A);
        int sum_pig = 0;
        for (int j = 1; j <= A; j++) {
            scanf(" %d", &K);
            if (last[K] == -1) {
                sum_pig += P[K];
            }
            else {
                add_edge(last[K], i, INF);
            }
            last[K] = i;
        }
        add_edge(0, i, sum_pig);
        scanf(" %d", &B);
        add_edge(i, n + 1, B);
    }
    int ans = dinic(0, n + 1);
    printf("%d\n", ans);
}

int main() {
    test_case();
    return 0;
}

```

### 后缀数组
```C++

#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

typedef long long LL;

const int N = 200005;
const int maxn = 100005;

int n, m;

char s[maxn];
int y[maxn], x[maxn], c[maxn], sa[maxn], rk[maxn], height[maxn], wt[30];
void get_SA() {
    for (int i = 1; i <= n; ++i) ++c[x[i] = s[i - 1]];
    //c数组是桶
    //x[i]是第i个元素的第一关键字
    for (int i = 2; i <= m; ++i) c[i] += c[i - 1];
    //做c的前缀和，我们就可以得出每个关键字最多是在第几名
    for (int i = n; i >= 1; --i) sa[c[x[i]]--] = i;
    for (int k = 1; k <= n; k <<= 1) {
        int num = 0;
        for (int i = n - k + 1; i <= n; ++i) y[++num] = i;
        //y[i]表示第二关键字排名为i的数，第一关键字的位置
        //第n-k+1到第n位是没有第二关键字的 所以排名在最前面
        for (int i = 1; i <= n; ++i) if (sa[i] > k) y[++num] = sa[i] - k;
        //排名为i的数 在数组中是否在第k位以后
        //如果满足(sa[i]>k) 那么它可以作为别人的第二关键字，就把它的第一关键字的位置添加进y就行了
        //所以i枚举的是第二关键字的排名，第二关键字靠前的先入队
        for (int i = 1; i <= m; ++i) c[i] = 0;
        //初始化c桶
        for (int i = 1; i <= n; ++i) ++c[x[i]];
        //因为上一次循环已经算出了这次的第一关键字 所以直接加就行了
        for (int i = 2; i <= m; ++i) c[i] += c[i - 1]; //第一关键字排名为1~i的数有多少个
        for (int i = n; i >= 1; --i) sa[c[x[y[i]]]--] = y[i], y[i] = 0;
        //因为y的顺序是按照第二关键字的顺序来排的
        //第二关键字靠后的，在同一个第一关键字桶中排名越靠后
        //基数排序
        swap(x, y);
        //这里不用想太多，因为要生成新的x时要用到旧的，就把旧的复制下来，没别的意思
        x[sa[1]] = 1;
        num = 1;
        for (int i = 2; i <= n; ++i)
            x[sa[i]] = (y[sa[i]] == y[sa[i - 1]] && y[sa[i] + k] == y[sa[i - 1] + k]) ? num : ++num;
        //因为sa[i]已经排好序了，所以可以按排名枚举，生成下一次的第一关键字
        if (num == n) break;
        m = num;
        //这里就不用那个122了，因为都有新的编号了
    }
}

// rk[i]表示i作为起始位置的后缀在所有后缀中的排名
// height[i] = lcp(sa[i], sa[i-1])
// height[rk[i]] >= height[rk[i-1]] - 1
void get_height() {
    int k = 0;
    for (int i = 1; i <= n; ++i) rk[sa[i]] = i;
    for (int i = 1; i <= n; ++i) {
        if (rk[i] == 1) continue;//第一名height为0
        if (k) --k;//h[i]>=h[i-1]-1;
        int j = sa[rk[i] - 1];
        // 字符串s起始位置为0
        while (j + k <= n && i + k <= n && s[i + k - 1] == s[j + k - 1]) ++k;
        height[rk[i]] = k;//h[i]=height[rk[i]];
    }
    for (int i = 1; i <= n; i++) printf("%d ", height[i]); printf("\n");
}

void test_case() {
    scanf("%s", s);
    n = strlen(s);
    m = 300;
    get_SA();
    get_height();
}

int main() {
    test_case(); 
    return 0;
}


```

### 二分图最大匹配 & 匈牙利算法
```C++
// POJ1274

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int N = 205;

vector<int> g[N];
int n, m;
bool visited[N];
int match[N];

bool dfs(int u) {
	for (int i = g[u].size() - 1; i >= 0; i--) {
		int v = g[u][i];
		if (!visited[v]) {
			visited[v] = true;
			if ((match[v] == -1) || dfs(match[v])) {
				match[v] = u;
				return true;
			}
		}
	}
	return false;
}

int get_max_match() {
	memset(visited, false, sizeof(visited));
	memset(match, -1, sizeof(match));
	int ans = 0;
	for (int i = 1; i <= n; i++) {
		memset(visited, false, sizeof(visited));
		if (dfs(i)) ans += 1;
	}
	return ans;
}

int main() {
	int c, v;
	while (scanf(" %d %d", &n, &m) != EOF) {
		for (int i = 1; i < N; i++) g[i].clear();
		for (int i = 1; i <= n; i++) {
			scanf(" %d", &c);
			while (c--) {
				scanf(" %d", &v);
				g[i].push_back(v);
			}
		}
		int ans = get_max_match();
		printf("%d\n", ans);
	}
	return 0;
}

```

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
