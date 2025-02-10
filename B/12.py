N = int(input())

l = 0.0
r = 100.0


def target_function(x):
    return x**3 + x


x = 0
while l <= r:
    m = (l + r) / 2
    if target_function(m) - N > 0.00001:
        r = m - 0.001
    elif N - target_function(m) < 0.00001:
        l = m + 0.001
    else:
        x = m
        l = m + 0.001
print(x)
