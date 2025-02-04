N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# 初期条件を思いつくのに時間がかかった
score = [-(10**9)] * (N + 1)
score[1] = 0
for i in range(1, N):
    score[A[i - 1]] = max(score[A[i - 1]], score[i] + 100)
    score[B[i - 1]] = max(score[B[i - 1]], score[i] + 150)
print(score[N])
