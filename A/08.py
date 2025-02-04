H, W = map(int, input().split())
X = [None] * H
for i in range(H):
    X[i] = list(map(int, input().split()))
Q = int(input())
A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())
sum = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + X[i - 1][j - 1]

for i in range(Q):
    print(
        sum[C[i]][D[i]]
        - sum[A[i] - 1][D[i]]
        - sum[C[i]][B[i] - 1]
        + sum[A[i] - 1][B[i] - 1]
    )
