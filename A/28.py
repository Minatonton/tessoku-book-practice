N = int(input())
T = [None] * N
A = [None] * N

for i in range(N):
    T[i], A[i] = input().split()
    A[i] = int(A[i])

ans = 0

for i in range(N):
    if T[i] == "+":
        ans = (ans + A[i]) % 10000
    elif T[i] == "-":
        ans = (ans - A[i] + 10000) % 10000
    else:
        ans = (ans * A[i]) % 10000
    print(ans)
