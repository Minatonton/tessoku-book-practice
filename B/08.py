N = int(input())
X = [None] * N
Y = [None] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

Q = int(input())
a = [None] * Q
b = [None] * Q
c = [None] * Q
d = [None] * Q

for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

dp = [[0] * 1501 for _ in range(1501)]
for i in range(N):
    dp[X[i]][Y[i]] += 1

for i in range(1, 1501):
    for j in range(1, 1501):
        dp[i][j] = dp[i][j - 1] + dp[i][j]

for i in range(1, 1501):
    for j in range(1, 1501):
        dp[j][i] = dp[j - 1][i] + dp[j][i]


for i in range(Q):
    ans = (
        dp[c[i]][d[i]]
        + dp[a[i] - 1][b[i] - 1]
        - dp[c[i]][b[i] - 1]
        - dp[a[i] - 1][d[i]]
    )
    print(ans)
