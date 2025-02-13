N = int(input())

prime = [True] * 1000009

MAX = int(N**0.5)

for i in range(2, MAX + 1):
    if prime[i]:
        for j in range(i * 2, N + 1, i):
            prime[j] = False


for i in range(2, N + 1):
    if prime[i]:
        print(i)
