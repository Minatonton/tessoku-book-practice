D, N = map(int, input().split())
L = [None] * N
R = [None] * N
H = [None] * N

for i in range(N):
    L[i], R[i], H[i] = map(int, input().split())

day_max = [float("INF")] * D

for i in range(N):
    for j in range(L[i], R[i] + 1):
        day_max[j - 1] = min(day_max[j - 1], H[i])

ans = 0
for i in range(D):
    if day_max[i] != float("INF"):
        ans += day_max[i]
    else:
        ans += 24

print(ans)
