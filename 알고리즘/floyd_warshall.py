#모든 정점에서 모든정점으로의 최단 경로
#거쳐가는 정점을 기준으로

INF = float('inf')
#초기값 설정
v = 10
data = [[INF]*v for _ in range(v)]
#간선의 개수, v1, v2, cost
n = int(input())
for _ in range(n):
    v1, v2, cost = map(int,input().split())
    data[v1][v2] = cost

for k in range(v):
#자기자신은 0
    data[k][k] = 0
    # i : 출발지    
    for i in range(v):
        # j : 목적지
        for j in range(v):
            #X에서 Y로 가는 최소비용  VS  X에서 노드k로 가는 비용 + 노드k에서 Y로 가는 비용
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])
