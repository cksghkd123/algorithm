from collections import deque
import heapq


n, m = map(int,input().split())

ordering = [set() for _ in range(n+1)]
trailer = [[] for _ in range(n+1)]

#b보다 먼저 풀어야 하는 a를 b에 기록
for _ in range(m):
    a, b = map(int,input().split())
    ordering[b].add(a)
    trailer[a].append(b)

solved = [False for _ in range(n+1)]
answer = []

heap = []
for number in range(1,n+1):
    heapq.heappush(heap,(len(ordering[number]), number))

while heap:
    i, number = heapq.heappop(heap)

    if solved[number]:
        continue
    
    if i == 0:
        for t_number in trailer[number]:
            ordering[t_number].remove(number)
            heapq.heappush(heap,(len(ordering[t_number]), t_number))
        answer.append(str(number))

a = ' '.join(answer)
print(a)
