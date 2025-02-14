N = int(input())
A = []
i = 1
while i * i <= N:
    if i * i == N:
        A.append(i)
    else:
        if N % i == 0:
            A.append(i)
            A.append(N // i)
    i += 1
A.sort()
for a in A:
    print(a)
