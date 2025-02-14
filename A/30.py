n, r = map(int, input().split())
M = 1000000007


def power(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        wari = 2**i
        if (b // wari) % 2 == 1:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans


bunnsi = 1
for i in range(1, n + 1):
    bunnsi = (bunnsi * i) % M

bunnbo = 1
for i in range(1, r + 1):
    bunnbo = (bunnbo * i) % M
for i in range(1, n - r + 1):
    bunnbo = (bunnbo * i) % M

bunnbo = power(bunnbo, M - 2, M)

print((bunnsi * bunnbo) % M)
