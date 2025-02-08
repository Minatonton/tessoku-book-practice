N = int(input())
A = list(map(int, input().split()))
amari = [0] * 100
for a in A:
    amari[a % 100] += 1

ans = 0
for i in range(1, 50):
    ans += amari[i] * amari[100 - i]
# あまりが0の時
ans += (amari[0]) * (amari[0] - 1) / 2
# あまりが50の時
ans += (amari[50]) * (amari[50] - 1) / 2

print(int(ans))
