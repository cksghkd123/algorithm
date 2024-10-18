import heapq


N = int(input())

left_heap = []
right_heap = []
answer = []
for _ in range(N):
    new_number = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -new_number)
    else:
        heapq.heappush(right_heap, new_number)

    if right_heap and right_heap[0] < -left_heap[0]:
        left_value = heapq.heappop(left_heap)
        right_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -right_value)
        heapq.heappush(right_heap, -left_value)

    answer.append(-left_heap[0])

for i in range(N):
    print(answer[i])
