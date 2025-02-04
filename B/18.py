import sys

N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        dp[i][j] = dp[i - 1][j]
        if j - A[i] >= 0:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i]]

if not dp[N][S]:
    print(-1)
    sys.exit(0)

ans = []
n = N
s = S
while n != 0:
    if dp[n - 1][s]:
        s = s
    else:
        ans.append(n)
        s -= A[n]
    n -= 1
ans = [str(answer) for answer in ans]
print(len(ans))
print(" ".join(ans))
