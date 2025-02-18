from collections import deque

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(N + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (N + 1)
dist[1] = 0

que = deque()
que.append(1)

while len(que) >= 1:
    pos = que.popleft()
    for next in G[pos]:
        if dist[next] == -1:
            que.append(next)
            dist[next] = dist[pos] + 1

for i in range(1, N + 1):
    print(dist[i])
