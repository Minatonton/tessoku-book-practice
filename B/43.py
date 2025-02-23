N, M = map(int, input().split())
A = list(map(int, input().split()))

miss = [0] * N

for i in range(M):
    miss[A[i] - 1] += 1

for i in range(N):
    print(M - miss[i])
