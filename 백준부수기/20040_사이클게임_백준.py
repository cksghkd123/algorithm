def find(x, root):
    while root[x] != x:
        root[x] = root[root[x]]
        x = root[x]
    return x


def union(x, y, root):
    fx = find(x, root)
    fy = find(y, root)

    if fx != fy:
        root[fy] = fx
    
    
n, m = map(int, input().split())
root = [i for i in range(n)]

answer = 0

for i in range(m):
    a, b = map(int, input().split())
    if answer != 0:
        continue
    
    if find(a, root) == find(b, root):
        answer = i+1
    else:
        union(a, b, root)

print(answer)
