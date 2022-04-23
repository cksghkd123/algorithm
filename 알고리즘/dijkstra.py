# 입력 - 마지막은 시작정점
# 6 11
# 1 2 3
# 1 3 3
# 1 4 3
# 2 3 2
# 4 3 5
# 4 5 2
# 5 4 1
# 3 5 1
# 6 3 1
# 3 6 4
# 5 6 2
# 1
# 정점, 간선의 수
V, E = map(int, input().split())

# 인접 리스트 초기화
maplist = [[] for i in range(V+1)]

# 간선 정보를 인접리스트에 저장
for _ in range(E):
    s, e, l = map(int, input().split())
    maplist[s].append((e, l))

# 시작 정점 입력
start = int(input())

# distance 리스트 초기화
distance = [float('inf') for _ in range(V+1)]
distance[start] = 0
# 시작 정점의 distance 초기화
for i, j in maplist[start]:
    distance[i] = j

# selected 리스트 초기화
selected = [0 for i in range(V+1)]
# 0번 노드는 없어서
selected[0] = 1

# 아래 과정을 정점 수 만큼 반복
for _ in range(1, V+1):
    # 방문하지 않았으면서, 알려진 거리가 가장 짧은 노드를
    # min_node에 저장
    min_value = float('inf')
    min_node = 0
    for i in range(1, V+1):
        if distance[i] < min_value and not selected[i]:
            min_value = distance[i]
            min_node = i
    
    # min_node 방문표시
    selected[min_node] = 1
    
    # min_node 에서 갈 수 있는 각 정점들 중
    # 알려진 거리 (distance[next_node]) 와
    # 새로운 거리 (distance[min_node] + l) 중 작은 값으로 갱신
    for next_node, l in maplist[min_node]:
        distance[next_node] = min(distance[next_node], distance[min_node] + l)

# 거리정보 출력
print(distance)

############## heapq로 구현하는게 더 빠르다 ###############
############## 백준 1753 최단경로 문제 참고 ###############