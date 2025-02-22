N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def check(x):
    cnt = 0
    last_kireme = 0
    for i in range(N):
        if A[i] - last_kireme >= x and L - A[i] >= x:
            cnt += 1
            last_kireme = A[i]
    return cnt >= K


left, right = 1, 10**9
while left < right:
    mid = (left + right + 1) // 2
    ans = check(mid)
    if ans == False:
        right = mid - 1
    else:
        left = mid

print(left)
