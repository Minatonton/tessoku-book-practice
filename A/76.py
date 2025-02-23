import bisect

N, W, L, R = map(int, input().split())
X = list(map(int, input().split()))

X = [0] + X + [W]


MOD = 10**9 + 7
dp = [0] * (N + 2)
dp_sum = [0] * (N + 2)
dp[0] = 1
dp_sum[0] = 1
for i in range(1, N + 2):
    pos_l = bisect.bisect_left(X, X[i] - R)
    pos_r = bisect.bisect_left(X, X[i] - L + 1) - 1
    dp[i] = (dp_sum[pos_r] if pos_r >= 0 else 0) - (
        dp_sum[pos_l - 1] if pos_l >= 1 else 0
    )
    dp[i] %= MOD
    dp_sum[i] = dp_sum[i - 1] + dp[i]
    dp_sum[i] %= MOD

print(dp[N + 1])
