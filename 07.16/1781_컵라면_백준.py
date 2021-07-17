import heapq


N = int(input())
table = {i:[] for i in range(N+1)}
dead_end = -1

for _ in range(N):
    dead, cup = map(int,input().split())
    table[dead].append(cup)
    dead_end = max(dead,dead_end)

result = 0
choice = []

for i in range(dead_end, 0, -1):
    for j in table[i]:
        heapq.heappush(choice, -j)
    if choice:
        result -= heapq.heappop(choice)

print(result)