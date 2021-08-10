import collections


def topology_sort():
    result = []
    deq = collections.deque()

    for i in range(1, n+1):
        for j in range(n):
            if last_year[j] == i:
                break
            graph[last_year[j]].append(i)
            indegree[i] += 1

    for _ in range(m):
        a, b = map(int,input().split())
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
        else:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            deq.append(i)

    while deq:
        if len(deq) > 1:
            return '?'
        node = deq.popleft()
        result.append(node)

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                deq.append(i)
                
    
    if len(result) == n:
        return result
    else:
        return 'IMPOSSIBLE'


t = int(input())
for _ in range(t):
    n = int(input())
    last_year = list(map(int,input().split()))
    m = int(input())

    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    
    result = topology_sort()
    if type(result) == str:
        print(result)
    else:
        print(*result)

