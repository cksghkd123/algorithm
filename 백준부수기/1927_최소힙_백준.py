import heapq
import sys

n = int(input())
array = []

for _ in range(n):
    number = int(sys.stdin.readline())
    if number == 0:
        if array:
            print(heapq.heappop(array))
        else:
            print(0)
    else:
        heapq.heappush(array, number)
