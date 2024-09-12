import heapq


INF = float('inf')
N, M = map(int, input().split())

crosswalks = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    crosswalks[a].append((b, i+1))
    crosswalks[b].append((a, i+1))

visited = [INF for _ in range(N+1)]
heap = [(0, 1, 0)]

while heap:
    time, curr, order1 = heapq.heappop(heap)
    if visited[curr] < time:
        continue

    visited[curr] = time

    for nxt, order2 in crosswalks[curr]:
        if order1 < order2:
            if time + order2 - order1 < visited[nxt]:
                heapq.heappush(heap, (time + order2 - order1, nxt, order2))
        else:
            if time + M + order1 - order2 < visited[nxt]:
                heapq.heappush(heap, (time + M + order2 - order1, nxt, order2))

answer = visited[N]
print(answer)