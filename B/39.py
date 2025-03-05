import heapq

N, D = map(int, input().split())
X = [None] * N
Y = [None] * N
work = []
for i in range(N):
    X[i], Y[i] = map(int, input().split())
    work.append((X[i], Y[i]))

work.sort()

q = []
index = 0
ans = 0
for d in range(1, D + 1):
    while index <= N - 1 and work[index][0] <= d:
        heapq.heappush(q, -work[index][1])
        index += 1
    if q:
        money = -heapq.heappop(q)
        ans += money

print(ans)
