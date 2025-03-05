N = int(input())
counting_map = {}

for i in range(N):
    a = input()
    if a in counting_map:
        counting_map[a] += 1
    else:
        counting_map[a] = 1
ans = 0
for i in counting_map:
    ans += counting_map[i] * (counting_map[i] - 1) // 2
print(ans)
