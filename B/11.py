N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [None] * Q
for i in range(Q):
    X[i] = int(input())

A.sort()


def check(x):
    l = 0
    r = N - 1
    while l <= r:
        m = (l + r) // 2
        if x == A[m]:
            if m == 0:
                return 0
            else:
                return m
        elif x > A[m]:
            l = m + 1
        else:
            r = m - 1
    return r + 1


for i in range(Q):
    print(check(X[i]))
