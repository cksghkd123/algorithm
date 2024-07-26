import heapq


n = int(input())
m = int(input())

connections = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, v = map(int, input().split())
    connections[a].append((b, v))


s, e = map(int, input().split())


heap = []
result = [-1 for _ in range(n+1)]

heapq.heappush(heap, (0, [s]))

while heap:
    amount, trace = heapq.heappop(heap)
    if result[trace[-1]] == -1:
        result[trace[-1]] = (amount, trace)
    else:
        continue

    if trace[-1] == e:
        break
    
    for next_city, cost in connections[trace[-1]]:
        if result[next_city] == -1:
            heapq.heappush(heap, (amount+cost, trace + [next_city]))

        
print(result[e][0])
print(len(result[e][1]))
print(*result[e][1])