from collections import deque
import heapq


n, m = map(int,input().split())
preceding = [[] for _ in range(n+1)]
trailing = [[] for _ in range(n+1)]
selected = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    preceding[b].append(a)
    heapq.heappush(trailing[a],b)

numbers = [(i,i) for i in range(1,n+1)]
numbers = deque(numbers)

result = []
while numbers:
    i, n = numbers.popleft()
    if selected[n]:
        continue

    for pre_n in preceding[n]:
        if not selected[pre_n]:
            numbers.append(n)
            break
    else:
        result.append(n)
        selected[n] = True
        while trailing[n]:
            nn = heapq.heappop(trailing)
            for pre_n in preceding[nn]:
                if not selected[pre_n]:
                    numbers.append(n)
                    break
            