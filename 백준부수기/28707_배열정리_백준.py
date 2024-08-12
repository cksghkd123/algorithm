import heapq

N = int(input())
A = list(map(int, input().split()))
M = int(input())
commands = [list(map(int, input().split())) for _ in range(M)]

target = tuple(sorted(A))

visited = set()

heap = []
heapq.heappush(heap, (0, tuple(A)))

answer = -1

while heap:
    count, curr = heapq.heappop(heap)

    if curr in visited:
        continue

    visited.add(curr)

    if curr == target:
        answer = count
        break

    for l, r, c in commands:
        l -= 1
        r -= 1
        nxt = list(curr)
        nxt[l], nxt[r] = nxt[r], nxt[l]

        heapq.heappush(heap, (count + c, tuple(nxt)))

print(answer)
