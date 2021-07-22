def find(n):
    if parent[n] == n:
        return n

    return find(parent[n])

def union(n1, n2):
    parent[find(n2)] = find(n1)

V, E = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(E)]
graph.sort(key = lambda x: x[2])
parent = [i for i in range(V+1)]
cost = 0

for s1, s2, a in graph:
    if find(s1) != find(s2):
        union(s1, s2)
        cost += a
    
print(cost)
