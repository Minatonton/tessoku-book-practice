N = int(input())
A = [None] * (N + 1)
P = [None] * (N + 1)

for i in range(1, N + 1):
    P[i], A[i] = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][N] = 0

for length in range(N - 2, -1, -1):
    for l in range(1, N - length + 1):
        r = l + length
        score_l = 0
        if l >= 2 and P[l - 1] >= l and P[l - 1] <= r:
            score_l = A[l - 1]
        score_r = 0
        if r + 1 <= N and P[r + 1] >= l and P[r + 1] <= r:
            score_r = A[r + 1]
        if l == 1:
            dp[l][r] = dp[l][r + 1] + score_r
        elif r == N:
            dp[l][r] = dp[l - 1][r] + score_l
        else:
            dp[l][r] = max(dp[l][r + 1] + score_r, dp[l - 1][r] + score_l)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, dp[i][i])
print(ans)
