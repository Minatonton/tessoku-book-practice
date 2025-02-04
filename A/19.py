N, W = map(int, input().split())
w = [None] * N
v = [None] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, W + 1):
        dp[i][j] = dp[i - 1][j]
        if j - w[i - 1] >= 0:
            dp[i][j] = max(dp[i - 1][j - w[i - 1]] + v[i - 1], dp[i - 1][j])

ans = 0
for i in range(0, W + 1):
    ans = max(ans, dp[N][i])
print(ans)
