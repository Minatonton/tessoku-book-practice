import heapq

Q = int(input())
queries = [input().split() for i in range(Q)]

T = []
for q in queries:
    if q[0] == "1":
        heapq.heappush(T, int(q[1]))
    elif q[0] == "2":
        print(T[0])
    else:
        heapq.heappop(T)
