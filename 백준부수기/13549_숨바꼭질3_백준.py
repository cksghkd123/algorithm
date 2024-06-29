import heapq


N, K = map(int, input().split())

INF = float('inf')
records = [INF for _ in range(100001)]

heap = []
heapq.heappush(heap, (0, N))

not_found = True
answer = 0

while not_found:
    count, curr_point = heapq.heappop(heap)
    
    if count > records[curr_point]:
        continue

    if curr_point == K:
        answer = count
        not_found = False
        continue

    candidates = [curr_point+1, curr_point-1, curr_point*2]

    for i in range(3):
        next_point = candidates[i]

        if 0 <= next_point <= 100000:
            if i == 2:
                if count < records[next_point]:
                    records[next_point] = count
                    heapq.heappush(heap, (count, next_point))
            else:
                if count + 1 < records[next_point]:
                    records[next_point] = count + 1
                    heapq.heappush(heap, (count + 1, next_point))

print(answer)