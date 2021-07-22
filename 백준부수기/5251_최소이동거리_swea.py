INF = float('inf')

def mini(list,visit):
    result = None
    for i in range(len(list)):
        if visit[i] == True:
            continue
        if result == None:
            result = i
            continue
        if result > list[i]:
            result = i
        
    return result

def dijkstra():
    long = 0
    visit = [False] * (N+1)
    d_list = {}
    for i in range(N+1):
        d_list[i] = INF
    d_list[0] = 0
    num = 0
    visit[num] = True

    while 1:
        for n, distance in road_list[num]:
            if d_list[n] > distance + long:
                d_list[n] = distance + long
        go = mini(d_list,visit)
        if go == None:
            break
        if visit[go] == False:
            visit[go] = True
            long = d_list[go]
            num = go
    
    return long

        

T = int(input())

for i in range(T):
    N, E = map(int,input().split())
    road_list = {i: [] for i in range(N+1)}
    for _ in range(E):
        n1, n2, m = list(map(int,input().split()))
        road_list[n1].append((n2, m))
        road_list[n2].append((n1, m))
    print('#{} {}'.format(i+1,dijkstra()))
