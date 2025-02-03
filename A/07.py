D = int(input())
N = int(input())
L = [None] * N
R = [None] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())
B = [0] * D
for i in range(N):
    B[L[i] - 1] += 1
    if R[i] != D:
        B[R[i]] -= 1
ans = 0
for i in range(D):
    ans += B[i]
    print(ans)
