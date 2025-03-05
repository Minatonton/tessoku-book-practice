from collections import deque

S = input()

stack = deque()
ans = []

for i in range(len(S)):
    if S[i] == "(":
        stack.append(i + 1)
    else:
        ans.append((stack[-1], i + 1))
        stack.pop()

for answer in ans:
    print(answer[0], answer[1])
