N = int(input())
A = list(map(int, input().split()))
length_list = [0] * (101)
for a in A:
    length_list[a] += 1
ans = 0
for length in length_list:
    if length >= 3:
        ans += (length * (length - 1) * (length - 2)) / 6
print(int(ans))
