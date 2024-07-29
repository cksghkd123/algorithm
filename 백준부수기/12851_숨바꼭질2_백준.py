import collections


N, K = map(int, input().split())

visited = [0 for _ in range(100001)]
records = [float('inf') for _ in range(100001)]

visited[N] = 1
records[N] = 0

deq = collections.deque()
deq.append((N, 0))

while deq:
    curr_point, cost = deq.popleft()
    for next_point in [curr_point-1, curr_point+1, curr_point*2]:
        if 0 <= next_point <= 100000:
            if cost+1 < records[next_point]:
                visited[next_point] += visited[curr_point]
                records[next_point] = cost+1
                deq.append((next_point, cost+1))
            elif cost+1 == records[next_point]:
                visited[next_point] += visited[curr_point]

print(records[K])
print(visited[K])