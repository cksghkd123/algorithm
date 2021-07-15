root = {}
rank = {}

def vertex(n):
    root[n] = n
    rank[n] = 0

def find_root(n):
    if root[n] != n:
        root[n] = find_root(root[n])

    return root[n]

def union(n1,n2):
    root1 = find_root(n1)
    root2 = find_root(n2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            root[root2] = root1
        else:
            root[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1
    
T = int(input())
k = 1

for _ in range(T):
    V, E = map(int,input().split())
    tree = 0
    lines = [tuple(reversed(tuple(map(int,input().split())))) for _ in range(E)]
    lines.sort()
    
    for i in range(V+1):
        vertex(i)
    
    
    for n in lines:
        if root[n[1]] != root[n[2]]:
            union(n[1],n[2])
            tree += n[0]

    print('#{} {}'.format(k,tree))
    k += 1




