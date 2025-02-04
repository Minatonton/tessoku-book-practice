def binary_search(X, A):
    L = 0
    R = len(A) - 1
    while L <= R:
        M = (L + R) // 2
        if A[M] < X:
            L = M + 1
        elif A[M] == X:
            return M
        else:
            R = M - 1


N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = binary_search(X, A)
print(ans + 1)
