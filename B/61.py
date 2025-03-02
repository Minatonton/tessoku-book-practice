N, M = map(int, input().split())
G = [list() for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

max_index = 0
max_count = len(G[0])
for i in range(1, N):
    if max_count < len(G[i]):
        max_index = i
        max_count = len(G[i])

print(max_index + 1)
