from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

K = [list(input().strip()) for _ in range(R)]


dist = [[-1] * C for _ in range(R)]
dist[sy][sx] = 0

que = deque()
que.append((sy, sx))

while que:
    current_y, current_x = que.popleft()

    for i in range(4):
        ny, nx = current_y + dy[i], current_x + dx[i]
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue

        if dist[ny][nx] == -1 and K[ny][nx] == ".":
            que.append((ny, nx))
            dist[ny][nx] = dist[current_y][current_x] + 1

print(dist[gy][gx])
