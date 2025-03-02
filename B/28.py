N = int(input())
M = int(1e9 + 7)

a_n_2 = 1
a_n_1 = 1
a_n = 0

for i in range(N - 2):
    a_n = (a_n_1 + a_n_2) % M
    a_n_2 = a_n_1
    a_n_1 = a_n

print((a_n) % M)
