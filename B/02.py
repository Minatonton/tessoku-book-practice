A, B = map(int, input().split())
counter = 0
for i in range(A, B + 1):
    if 100 % i == 0:
        counter += 1
if counter >= 1:
    print("Yes")
else:
    print("No")
