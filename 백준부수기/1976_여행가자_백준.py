def union(x, y):
    fx = find(x)
    fy = find(y)

    if fx != fy:
        root[fy] = fx

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    
    return root[x]

N = int(input())
M = int(input())

connections = [list(map(int, input().split())) for _ in range(N)]

plans = list(map(lambda x: int(x)-1, input().split()))

root = [i for i in range(N)]

for i in range(N):
    for j in range(N):
        if connections[i][j] and find(i) != find(j):
            union(i, j)

result = find(plans[0])
answer = 'YES'

for plan in plans:
    if result != find(plan):
        answer = 'NO'
        break

print(answer)