N, L = map(int, input().split())
A = [None] * N
B = [None] * N

for i in range(N):
    A[i], B[i] = input().split()
    A[i] = int(A[i])

ans = 0

for i in range(N):
    if B[i] == "E":
        ans = max(L - A[i], ans)
    else:
        ans = max(A[i], ans)
print(ans)
