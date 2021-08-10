import collections


def topology_sort():
    result = []
    deq = collections.deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            deq.append(i)

    while deq:
        node = deq.popleft()
        result.append(node)

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                deq.append(i)
    
    return result

n, m = map(int,input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

answer = topology_sort()

print(*answer)
