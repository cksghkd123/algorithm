import collections


def bfs(x):
    deq = collections.deque()
    deq.append(x)
    visited[x] = True
    
    while deq:
        x = deq.popleft()
        for w in web[x]:
            if visited[w] == False:
                visited[w] = True
                deq.append(w)


N, M = map(int,input().split())
web = [[] for _ in range(N)]

for _ in range(M):
    l = list(map(int,input().split()))
    u, v = map(lambda x: x-1, l)

    web[u].append(v)
    web[v].append(u)

visited = [False for _ in range(N)]
count = 0

for x in range(N):
    if visited[x] == False:
        count += 1
        bfs(x)
    
print(count)