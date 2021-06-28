import collections

def dfs(spot):
    dvisited[spot-1] = True
    dtrace.append(spot)

    for w in connect[spot]:
        if dvisited[w-1] == False:
            dfs(w)


def bfs(spot):
    bvisited[spot-1] = True
    btrace.append(spot)

    deq = collections.deque()
    deq.append(spot)
    
    while deq:
        dw = deq.popleft()
        for w in connect[dw]:
            if bvisited[w-1] == False:
                bvisited[w-1] = True
                btrace.append(w)
                deq.append(w)

N, M, V = map(int,input().split())

connect = {}

for spot in range(1,N+1):
    connect[spot] = []

for _ in range(M):
    branch = list(map(int,input().split()))
    connect[branch[0]].append(branch[1])
    connect[branch[1]].append(branch[0])

for k in range(1,N+1):
    connect[k].sort()

dvisited = [False for _ in range(N)]
bvisited = [False for _ in range(N)]

dtrace = []
btrace = []

dfs(V)
bfs(V)

for t in dtrace:
    print(t,end = ' ')
print('')
for t in btrace:
    print(t,end = ' ')