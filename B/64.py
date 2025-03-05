import heapq

N, M = map(int, input().split())
G = [list() for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))

INF = 10**10
dist = [INF] * N
ok = [False] * N
dist[0] = 0
que = []
heapq.heappush(que, (dist[0], 0))
while que:
    pos = heapq.heappop(que)[1]
    if ok[pos]:
        continue
    ok[pos] = True
    for e in G[pos]:
        if dist[e[0]] > dist[pos] + e[1]:
            dist[e[0]] = dist[pos] + e[1]
            heapq.heappush(que, (dist[e[0]], e[0]))

ans = []
current = N - 1
ans.append(current + 1)
current_dist = dist[N - 1]
while current != 0:
    for e in G[current]:
        if dist[e[0]] == current_dist - e[1]:
            current = e[0]
            current_dist = dist[e[0]]
            ans.append(current + 1)

print(" ".join(map(str, ans[::-1])))
