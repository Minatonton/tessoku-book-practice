N, K = map(int, input().split())
counter = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if K - i - j >= 1 and N >= K - i - j:
            counter += 1
print(counter)
