N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = int(1e9)


def count(m):
    total = 0
    for a in A:
        total += m // a
    return total


ans = -1
while l <= r:
    m = (l + r) // 2
    total = count(m)

    if total >= K:
        ans = m
        r = m - 1
    else:
        l = m + 1

print(ans)
