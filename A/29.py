a, b = map(int, input().split())


def power(a, b, m):
    p = a
    ans = 1
    for i in range(31):
        wari = 2**i
        if (b // wari) % 2 == 1:
            p = p % m
            ans = (ans * p) % m
        p = (p * p) % m
    return ans


print(power(a, b, 1000000007))
