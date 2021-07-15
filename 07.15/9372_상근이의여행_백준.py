def find(x):
    if parent[x] != x:
        return find(parent[x])

    return x

def union(n1,n2):
    if find(n1) != find(n2):
        parent[find(n2)] = n1

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    fairway = [list(map(int,input().split())) for _ in range(M)]
    parent = [i for i in range(N+1)]
    air_time = 0
    for n1, n2 in fairway:
        if find(n1) != find(n2):
            union(n1,n2)
            air_time += 1
    print(air_time)