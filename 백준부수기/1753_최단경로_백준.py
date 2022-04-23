import collections
import heapq


INF = float('inf')

v, e = map(int,input().split())
k = int(input())
distance = [INF for _ in range(v+1)]
distance[k] = 0
graph = [collections.defaultdict(lambda:INF) for _ in range(v+1)]


for _ in range(e):
    n1, n2, w = map(int,input().split())
    if w < graph[n1][n2]:
        graph[n1][n2] = w
        if n1 == k:
            distance[n2] = w

for i in range(v+1):
    graph[i] = list(graph[i].items())

heap = []

for i,j in graph[k]:
    heapq.heappush(heap, (j,i))


selected = [0 for _ in range(v+1)]
selected[0] = 1

while heap:
    min_value, min_node = heapq.heappop(heap)
    if selected[min_node]:
        continue
    
    selected[min_node] = 1

    for next_node, weight in graph[min_node]:
        if distance[min_node]+weight < distance[next_node]:
            distance[next_node] = distance[min_node]+weight
            heapq.heappush(heap,(distance[next_node],next_node))


for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])