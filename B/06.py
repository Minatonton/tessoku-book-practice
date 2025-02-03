def judge(atari, hazure):
    if atari == hazure:
        print("draw")
    elif atari > hazure:
        print("win")
    else:
        print("lose")


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [None] * Q
R = [None] * Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())
sum = [0] * N
sum[0] = A[0]
for i in range(1, N):
    sum[i] = sum[i - 1] + A[i]
for i in range(Q):
    if L[i] == 1:
        atari = sum[R[i] - 1]
        hazure = R[i] - atari
        judge(atari, hazure)
    else:
        atari = sum[R[i] - 1] - sum[L[i] - 2]
        hazure = R[i] - L[i] + 1 - atari
        judge(atari, hazure)
