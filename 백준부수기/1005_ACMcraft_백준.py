import collections


t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    construction_time = [0] + list(map(int,input().split()))
    chain = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int,input().split())
        chain[y].append(x)
    w = int(input())

    visited = [0 for _ in range(n+1)]
    deq = collections.deque()
    deq.append((w, construction_time[w]))
    visited[w] = construction_time[w]
    answer = construction_time[w]

    while deq:
        node, time = deq.popleft()
        if visited[node] > time:
            continue
        for pre_node in chain[node]:
            new_time = time+construction_time[pre_node]
            if visited[pre_node] < new_time:
                visited[pre_node] = new_time
                deq.append((pre_node, new_time))
                answer = max(answer, new_time)
    
    print(answer)
        