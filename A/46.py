N = int(input())
X = [None] * N
Y = [None] * N


def calculate_distance(x_i, y_i, x_j, y_j):
    return (x_i - x_j) ** 2 + (y_i - y_j) ** 2


for i in range(N):
    X[i], Y[i] = map(int, input().split())


ans = [0]
visited = [False] * N
visited[0] = True
for _ in range(N):
    min_distance = 10000000000
    min_index = 0
    for j in range(N):
        distance = calculate_distance(X[ans[-1]], Y[ans[-1]], X[j], Y[j])
        if distance < min_distance and not visited[j]:
            min_index = j
            min_distance = distance
    visited[min_index] = True
    ans.append(min_index)
for answer in ans:
    print(answer + 1)
