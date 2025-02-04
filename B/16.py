N = int(input())
H = list(map(int, input().split()))

cost = [10**9] * N
cost[0] = 0
cost[1] = abs(H[0] - H[1])
for i in range(2, N):
    cost[i] = min(cost[i], cost[i - 1] + abs(H[i] - H[i - 1]))
    cost[i] = min(cost[i], cost[i - 2] + abs(H[i] - H[i - 2]))
print(cost[N - 1])
