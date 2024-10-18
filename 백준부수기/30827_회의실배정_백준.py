import heapq


N, K = map(int, input().split())
meeting_list = [list(map(int, input().split())) for _ in range(N)]

heap = []

for a, b in meeting_list:
    heapq.heappush(heap, (b, a))

room_list = [[] for _ in range(K)]
answer= 0

while heap:
    end, start = heapq.heappop(heap)

    for room in room_list:
        if not room:
            room.append(end)
            answer += 1
            break
        else:
            if room[-1] < start:
                room.append(end)
                answer += 1
                break

print(answer)
print(room_list)
