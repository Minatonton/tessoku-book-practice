N = int(input())
S = input()

flag = False

for i in range(N - 2):
    if S[i] == "R" and S[i + 1] == "R" and S[i + 2] == "R":
        flag = True
    if S[i] == "B" and S[i + 1] == "B" and S[i + 2] == "B":
        flag = True

if flag:
    print("Yes")
else:
    print("No")
