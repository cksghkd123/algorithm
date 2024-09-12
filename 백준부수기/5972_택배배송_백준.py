import heapq


N, M = map(int, input().split())

connections = [[] for _ in range(N+1)]
for _ in range(M):
    ai, bi, ci = map(int, input().split())
    connections[ai].append((bi, ci))
    connections[bi].append((ai, ci))
    
visited = [False for _ in range(N+1)]
heap = []

heapq.heappush(heap, (0, 1))

answer = 0

while heap:
    amount, curr = heapq.heappop(heap)
    if not visited[curr]:
        visited[curr] = True
    else:
        continue

    if curr == N:
        answer = amount

    for nxt, cost in connections[curr]:
        if not visited[nxt]:
            heapq.heappush(heap, (amount+cost, nxt))

print(answer)