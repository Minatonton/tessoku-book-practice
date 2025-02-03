N, X = map(int, input().split())
A = list(map(int, input().split()))
is_included = False
for a in A:
    if a == X:
        is_included = True
if is_included:
    print("Yes")
else:
    print("No")
