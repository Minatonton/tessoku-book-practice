Q = int(input())
X = [None] * Q
for i in range(Q):
    X[i] = int(input())


def prime_check(x):
    flag = True
    i = 2
    while i * i <= x:
        if x % i == 0:
            flag = False
        i += 1
    return flag


for i in range(Q):
    ans = prime_check(X[i])
    if ans:
        print("Yes")
    else:
        print("No")
