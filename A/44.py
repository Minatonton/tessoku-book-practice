N, Q = map(int, input().split())
A = [0] + [i + 1 for i in range(N)]
queries = [[] for _ in range(Q)]
for i in range(Q):
    queries[i] = list(map(int, input().split()))

reverse = False

for i in range(Q):
    if queries[i][0] == 1:
        if reverse:
            A[N - queries[i][1] + 1] = queries[i][2]
        else:
            A[queries[i][1]] = queries[i][2]
    elif queries[i][0] == 2:
        reverse = not reverse
    else:
        if reverse:
            print(A[N - queries[i][1] + 1])
        else:
            print(A[queries[i][1]])
