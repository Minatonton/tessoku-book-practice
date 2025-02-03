N = input()
length = len(N)
sum = 0
for i in range(length):
    if N[i] == "1":
        sum += 2 ** (length - i - 1)
print(sum)
