def dikstra(start, list):
    INF = float('inf')
    distance = [INF for _ in range(n+1)]
    distance[start] = 0

    selected  = [False for _ in range(n+1)]
    selected[0] = True

    for _ in range(n):
        min_value = INF
        min_node = 0

        for i in range(1, n+1):
            if distance[i] < min_value and selected[i] == False:
                min_value = distance[i]
                min_node = i
        
        selected[min_node] = True

        for next_node, l in list[min_node]:
            distance[next_node] = min(distance[next_node], distance[min_node] + l)

    return distance


n, m, x = map(int,input().split())
go_list = [[] for _ in range(n+1)]
back_list = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, t = map(int,input().split())
    go_list[end].append((start, t))
    back_list[start].append((end,t))

go_distance = dikstra(x, go_list)
back_distance = dikstra(x, back_list)
result = max(map(lambda x,y: x+y, go_distance[1:], back_distance[1:]))

print(result)
