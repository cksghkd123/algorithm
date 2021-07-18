#{정점1} {정점2} {비용}
Elist = [(1, 2, 3), (1, 4, 6), (2, 4, 5), (2, 5, 4), (4, 5, 2), (3, 4, 2), (5, 8, 4), (5, 7, 2), (4, 7, 1), (3, 6, 3), (6, 7, 4), (7, 8, 6)]

#간선의 비용을 오름차순으로 정렬한다.
Elist.sort(key=lambda x:x[2])

#union & find 를 정의한다.
#정점의 개수
V = 8
parent = [i for i in range(V+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parent[fy] = fx
    
#이제 정렬된 간선을 하나씩 검사한다. 만약 해당 차례의 간선이 이미 만들어진 MST에 속해있다면 
#(find(v1) == find(v2) 인 경우) 아무것도 하지 않고, 속해있지 않다면 union을 통해 병합한다.

total_cost = 0
mst_info = []
for i in range(len(Elist)):
    v1, v2, cost = Elist[i]
    if find(v1) != find(v2):
        union(v1, v2)
        mst_info.append(f"[{v1}-{v2}]")
        total_cost += cost

print(total_cost)
for info in mst_info:
    print(info)

#시간복잡도는 정렬 알고리즘에 따라 달라지는데, O(nlogn)의 정렬 알고리즘을 사용하면 
#최종 시간복잡도는 O(nlogn + n) = O(nlogn)이 된다.