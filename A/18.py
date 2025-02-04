N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))
dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(S + 1):
        dp[i][j] = dp[i - 1][j]
        if j - A[i] >= 0:
            dp[i][j] += dp[i - 1][j - A[i]]
if dp[N][S] >= 1:
    print("Yes")
else:
    print("No")
