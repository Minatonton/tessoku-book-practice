class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.par[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.par[root_v] = root_u
                self.size[root_u] += self.size[root_v]

    def same(self, u, v):
        return self.root(u) == self.root(v)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

edges.sort(key=lambda x: x[2])

uf = UnionFind(N)
ans = 0
for a, b, c in edges:
    if not uf.same(a, b):
        uf.unite(a, b)
        ans += c

print(ans)
