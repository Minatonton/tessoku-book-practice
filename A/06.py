N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [None] * Q
R = [None] * Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())
sum_list = [0] * N
sum_list[0] = A[0]
for i in range(1, N):
    sum_list[i] = sum_list[i - 1] + A[i]
for i in range(Q):
    if L[i] == 1:
        print(sum_list[R[i] - 1])
    else:
        print(sum_list[R[i] - 1] - sum_list[L[i] - 2])
