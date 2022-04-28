n = int(input())
m = int(input())
bus_info = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int,input().split())
    bus_info[s].append((e, c))

start_node, end_node = map(int,input().split())
INF = float('inf')

visited = [False for _ in range(n+1)]
visited[start_node] = True

result = [INF for _ in range(n+1)]
result[start_node] = 0
for e, c in bus_info[start_node]:
    result[e] = min(result[e],c)

for _ in range(n-1):
    min_value = float('inf')
    min_node = 0
    for i in range(1,n+1):
        if result[i] < min_value and not visited[i]:
            min_value = result[i]
            min_node = i
    
    visited[min_node] = True

    for e, c in bus_info[min_node]:
        result[e] = min(result[e], result[min_node]+c)

print(result[end_node])
