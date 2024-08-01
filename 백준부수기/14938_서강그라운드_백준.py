import heapq


def bfs(i, connection, items, n, m):
    result = 0
    visited = [False for _ in range(n)]
    heap = []
    heapq.heappush(heap, (0, i))
    
    while heap:
        distance, curr = heapq.heappop(heap)
        if visited[curr]:
            continue

        visited[curr] = True
        result += items[curr]

        for nxt, cost in connection[curr]:
            if not visited[nxt] and distance+cost <= m:
                heapq.heappush(heap, (distance+cost, nxt))
    
    return result

n, m, r = map(int, input().split())

items = list(map(int, input().split()))

connection = [[] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    connection[a-1].append((b-1, l))
    connection[b-1].append((a-1, l))

answer = 0
for i in range(n):
    answer = max(answer, bfs(i, connection, items, n, m))

print(answer)

