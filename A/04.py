N = int(input())
for x in range(9, -1, -1):
    print((N // (2**x)) % 2, end="")
print("")
