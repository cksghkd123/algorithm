import heapq


a = [1,3,5,7,9]
heapq.heapify(a)
heapq.heappush(a,8)

print(a)
print(heapq.heappop(a))

print(heapq.heappop(a))

print(heapq.heappop(a))

print(heapq.heappop(a))

print(heapq.heappop(a))

print(a)

