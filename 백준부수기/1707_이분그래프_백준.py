import collections


def is_binary_graph(start):
    visited[start] = 1
    deq = collections.deque()
    deq.append(start)

    while deq:
        node = deq.popleft()
        for j in connected[node]:
            if visited[j] == 0:
                visited[j] = visited[node]*-1
                deq.append(j)
            elif visited[j] == visited[node]:
                return 'NO'

    return 'YES'


k = int(input())
for _ in range(k):
    v, e = map(int,input().split())
    connected = collections.defaultdict(list)
    visited = [0 for _ in range(v)]
    for _ in range(e):
        n1, n2 = map(int,input().split())
        connected[n1-1].append(n2-1)
        connected[n2-1].append(n1-1)
    
    for i in range(v):
        if visited[i] == False:
            result = is_binary_graph(i)
            if result == 'NO':
                break
    print(result)
            

