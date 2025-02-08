N, K = map(int, input().split())
S = input()
now_on = 0
for i in range(N):
    if S[i] == "1":
        now_on += 1

if abs(K - now_on) % 2 == 0:
    print("Yes")
else:
    print("No")
