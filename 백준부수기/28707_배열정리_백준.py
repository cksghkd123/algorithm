import collections
import heapq


N = int(input())
A = list(map(int, input().split()))
M = int(input())
commands = [list(map(int, input().split())) for _ in range(M)]

visited = set()

target = ''.join(map(str, sorted(A)))

heap = []
heapq.heappush(heap,(0,''.join(map(str, A))))

answer = 0

while heap:
    print(heap)
    count, curr = heapq.heappop(heap)
    if curr not in visited:
        visited.add(curr)
    else:
        continue

    if curr == target:
        answer = count
        break

    for c in commands:
        nxt = curr
        print(type(nxt))
        nxt[c[0]-1], nxt[c[1]-1] = nxt[c[1]-1], nxt[c[0]-1]
        heapq.heappush(heap, (count+c[2], nxt))

print(answer)