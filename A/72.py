import itertools

H, W, K = map(int, input().split())
c = [input() for i in range(H)]


def paint_row(H, W, d, remaining_steps):
    column = [([d[i][j] for i in range(H)].count("."), j) for j in range(W)]
    column.sort(reverse=True)

    for j in range(remaining_steps):
        idx = column[j][1]
        for i in range(H):
            d[i][idx] = "#"

    return sum(map(lambda l: l.count("#"), d))


answer = 0
for v in itertools.product([0, 1], repeat=H):
    d = [list(c[i]) for i in range(H)]
    remaining_steps = K
    for i in range(H):
        if v[i] == 1:
            d[i] = ["#"] * W
            remaining_steps -= 1
    if remaining_steps >= 0:
        subanswer = paint_row(H, W, d, remaining_steps)
        answer = max(answer, subanswer)

print(answer)
