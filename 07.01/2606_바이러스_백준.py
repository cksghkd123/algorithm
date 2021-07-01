import collections


def bfs(num):
    deq = collections.deque()
    deq.append(num)
    visited[num] = True
    count = 0

    while deq:
        num = deq.popleft()
        
        for nnum in network[num]:
            if visited[nnum] == False:
                deq.append(nnum)
                visited[nnum] = True
                count += 1

    return count

    
    

N = int(input())
M = int(input())

network = [[] for _ in range(N)]
for _ in range(M):
    i = list(map(int,input().split()))
    i = list(map(lambda x : x-1 ,i))
    network[i[0]].append(i[1])
    network[i[1]].append(i[0])
    

visited = [False for _ in range(N)]

num = 1-1

print(bfs(num))

