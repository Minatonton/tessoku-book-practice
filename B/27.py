import math

A, B = map(int, input().split())
c = math.gcd(A, B)
print(c * (A // c) * (B // c))


def solve_gcd(a, b):
    if a >= 1 and b >= 1:
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a >= b:
        return b
    return a
