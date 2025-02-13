N, A, B = map(int, input().split())
result = [None] * (N + 1)

for i in range(N + 1):
    if i >= A and result[i - A] == False:
        result[i] = True
    elif i >= B and result[i - B] == False:
        result[i] = True
    else:
        result[i] = False

if result[N]:
    print("First")
else:
    print("Second")
