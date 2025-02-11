N = int(input())

wari_3 = N // 3
wari_5 = N // 5
wari_7 = N // 7
wari_15 = N // 15
wari_21 = N // 21
wari_35 = N // 35
wari_105 = N // 105
ans = wari_3 + wari_5 + wari_7 - wari_15 - wari_21 - wari_35 + wari_105
print(ans)
