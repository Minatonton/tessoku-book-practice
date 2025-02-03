N = int(input())
A = list(map(int, input().split()))
is_exist = False
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j, N):
            if A[i] + A[j] + A[k] == 1000:
                is_exist = True
if is_exist:
    print("Yes")
else:
    print("No")
