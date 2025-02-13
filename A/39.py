N = int(input())
A = []

for i in range(N):
    l, r = map(int, input().split())
    A.append([r, l])

A.sort()

now = 0
ans = 0

for i in range(N):
    if now <= A[i][1]:
        now = A[i][0]
        ans += 1

print(ans)
