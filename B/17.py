N = int(input())
H = list(map(int, input().split()))

cost = [10**9] * N
cost[0] = 0
cost[1] = abs(H[0] - H[1])
for i in range(2, N):
    cost[i] = min(cost[i], cost[i - 1] + abs(H[i] - H[i - 1]))
    cost[i] = min(cost[i], cost[i - 2] + abs(H[i] - H[i - 2]))

ans = [N - 1]
while ans[-1] != 0:
    if cost[ans[-1]] == cost[ans[-1] - 1] + abs(H[ans[-1]] - H[ans[-1] - 1]):
        ans.append(ans[-1] - 1)
    else:
        ans.append(ans[-1] - 2)
ans.reverse()
print(len(ans))
for answer in ans:
    print(answer + 1, end=" ")
print("")
