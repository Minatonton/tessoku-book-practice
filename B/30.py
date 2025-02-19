def Power(a, b, m):
    p = a
    Answer = 1
    for i in range(30):
        wari = 2**i
        if (b // wari) % 2 == 1:
            Answer = (Answer * p) % m
        p = (p * p) % m
    return Answer


def Division(a, b, m):
    return (a * Power(b, m - 2, m)) % m


def ncr(n, r):
    M = 1000000007

    a = 1
    for i in range(1, n + 1):
        a = (a * i) % M

    b = 1
    for i in range(1, r + 1):
        b = (b * i) % M
    for i in range(1, n - r + 1):
        b = (b * i) % M

    return Division(a, b, M)


H, W = map(int, input().split())
print(ncr(H + W - 2, W - 1))
