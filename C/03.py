D = int(input())
X = int(input())
A = [None] * D
for i in range(1, D):
    A[i] = int(input())

Q = int(input())
S = [None] * Q
T = [None] * Q

for i in range(Q):
    S[i], T[i] = map(int, input().split())

total_difference = [0] * D
total_difference[1] = A[1]
for i in range(2, D):
    total_difference[i] = total_difference[i - 1] + A[i]

for i in range(Q):
    stock_price_s = X + total_difference[S[i] - 1]
    stock_price_t = X + total_difference[T[i] - 1]
    if stock_price_s > stock_price_t:
        print(S[i])
    elif stock_price_s == stock_price_t:
        print("Same")
    else:
        print(T[i])
