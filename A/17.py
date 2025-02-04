N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))
time = [0] * N
time[1] = A[1] + time[0]
for i in range(2, N):
    time[i] = min(time[i - 1] + A[i], time[i - 2] + B[i])
ans = [N - 1]
while ans[-1] != 0:
    if time[ans[-1]] == time[ans[-1] - 1] + A[ans[-1]]:
        ans.append(ans[-1] - 1)
    else:
        ans.append(ans[-1] - 2)

print(len(ans))
for i in range(len(ans) - 1, -1, -1):
    print(ans[i] + 1, end=" ")
print("")
