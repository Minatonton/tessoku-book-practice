N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = set()
for i in range(N):
    for j in range(N):
        AB.add(A[i] + B[j])

flag = False
for i in range(N):
    for j in range(N):
        if (K - (C[i] + D[j])) in AB:
            flag = True
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")
