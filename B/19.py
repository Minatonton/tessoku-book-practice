N, W = map(int, input().split())
w = [None] * N
v = [None] * N

for i in range(N):
    w[i], v[i] = map(int, input().split())

V = sum(v) + 1
INF = float("inf")

dp = [[INF] * V for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(V):
        dp[i][j] = dp[i - 1][j]
        if j - v[i - 1] >= 0:
            dp[i][j] = min(dp[i - 1][j - v[i - 1]] + w[i - 1], dp[i][j])

ans = 0
for j in range(V):
    if dp[N][j] <= W:
        ans = j
print(ans)
