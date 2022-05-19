import heapq


n = int(input())
conference_info = []
for _ in range(n):
    s, e = map(int,input().split())
    conference_info.append((s,e))
conference_info.sort()

heap = []
heap.append((0, 0, 0))
visited = [-1 for _ in range(n)]
answer = 0
while heap:
    i, count, current_time = heapq.heappop(heap)
    print(i,count,current_time)
    if i == n:
        answer = max(answer, count)
        continue
    if conference_info[i][0] < current_time:
        heapq.heappush(heap,(i+1, count, current_time))
    else:
        if visited[i] < count:
            visited[i] = count
            heapq.heappush(heap, (i+1, count+1, conference_info[i][1]))
            heapq.heappush(heap,(i+1, count, current_time))


    
print(answer)
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14