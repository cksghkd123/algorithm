from collections import defaultdict
import heapq

n,m = map(int,input().split())
costs_info = defaultdict(list)
for _ in range(m):
    a, b, c = map(int,input().split())
    costs_info[a].append((c, b))
    costs_info[b].append((c, a))

selected = [False for _ in range(n+1)]
selected[0] = True
selected[1] = True


heap = []
for i in costs_info[1]:
    heapq.heappush(heap,i)
result = []

while heap:
    weight, node = heapq.heappop(heap)

    if not selected[node]:
        selected[node] = True
        result.append(weight)

        for next_weight, next_node in costs_info[node]:
            if not selected[next_node]:
                heapq.heappush(heap, (next_weight, next_node))

answer = sum(result)-max(result)
print(answer)
