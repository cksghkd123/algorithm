import heapq
import sys

n, k = map(int, sys.stdin.readline().split())
jewelry = []
bag = []

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    jewelry.append((m, v))
for _ in range(k):
    c = int(sys.stdin.readline())
    bag.append(c)

jewelry.sort()
bag.sort()
answer = 0

candidate_j = []
for i in range(k):
    while jewelry and jewelry[0][0] <= bag[i]:
        weight, price = heapq.heappop(jewelry)
        heapq.heappush(candidate_j, -price)
    
    if candidate_j:
        answer -= heapq.heappop(candidate_j)
    elif not jewelry:
        break

print(answer)