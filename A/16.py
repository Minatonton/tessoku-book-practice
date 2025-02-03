N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))
time = [0] * N
time[1] = A[1] + time[0]
for i in range(2, N):
    time[i] = min(time[i - 1] + A[i], time[i - 2] + B[i])
print(time[N - 1])
