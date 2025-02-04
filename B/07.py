T = int(input())
N = int(input())
L = [None] * N
R = [None] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

zougenn = [0] * (T + 1)
for i in range(N):
    zougenn[L[i]] += 1
    zougenn[R[i]] -= 1
time = [0] * (T)
time[0] += zougenn[0]
print(time[0])
for i in range(1, T):
    time[i] = time[i - 1] + zougenn[i]
    print(time[i])
