def power(a, b, m):
    p = a
    ans = 1
    for i in range(61):
        wari = 2**i
        if (b // wari) % 2 == 1:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans


a, b = map(int, input().split())
m = 1000000007

print(power(a, b, m))
