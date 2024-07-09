import collections
import heapq


commands = list(map(int, input().split()))
answer = float('inf')

heap = []
heapq.heappush(heap,(0, 0, 0, 0))

visited = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(commands))]

while heap:
    amount, left, right, idx = heapq.heappop(heap)

    if visited[idx][left][right]:
        continue

    visited[idx][left][right] = True
    
    if commands[idx] == 0:
        answer = amount
        break

    target = commands[idx]

    if target == left or target == right:
        heapq.heappush(heap,(amount+1, left, right, idx+1))
    else:
        if left == 0:
            heapq.heappush(heap,(amount+2, target, right, idx+1))
        if right == 0:
            heapq.heappush(heap,(amount+2, left, target, idx+1))
        if abs(target-left) == 2:
            heapq.heappush(heap,(amount+4, target, right, idx+1))
        else:
            heapq.heappush(heap,(amount+3, target, right, idx+1))

        if abs(target-right) == 2:
            heapq.heappush(heap, (amount+4, left, target, idx+1))
        else:
            heapq.heappush(heap,(amount+3, left, target, idx+1))

print(answer)
    