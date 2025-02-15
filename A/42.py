N, K = map(int, input().split())
A = [None] * N
B = [None] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = 0

for a in range(1, 101):
    for b in range(1, 101):
        count = 0
        for i in range(N):
            if A[i] >= a and B[i] >= b and A[i] <= a + K and B[i] <= b + K:
                count += 1
        ans = max(count, ans)

print(ans)
