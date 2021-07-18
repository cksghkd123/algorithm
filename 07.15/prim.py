import heapq


#정점의 개수
V = 8  

#(정점, 정점, 가중치) 
Elist = [(1, 2, 3), (1, 4, 6), (2, 4, 5), (2, 5, 4), (4, 5, 2), (3, 4, 2), (5, 8, 4), (5, 7, 2), (4, 7, 1), (3, 6, 3), (6, 7, 4), (7, 8, 6)]

#간선의 비용을 오름차순으로 정렬한다.
lines = {i:[] for i in range(1,V+1)}
for n1, n2, wei in Elist:
    lines[n1].append((n2,wei))
    lines[n2].append((n1,wei))


#visit 배열과 distance 배열
INF = float('inf')
visit = [False]*(V+1)
distance = [INF]*(V+1)

#1에서 시작
visit[1] = True
distance[1] = 0

edges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (15, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]
from collections import defaultdict
from heapq import *

def prim(first_node, edges):
    mst = []
    # 해당 노드에 해당 간선을 추가
    adjacent_edges = defaultdict(list)
    for weight, node1, node2 in edges:
        adjacent_edges[node1].append((weight, node1, node2))
        adjacent_edges[node2].append((weight, node2, node1))

    # 처음 선택한 노드를 연결된 노드 집합에 삽입
    connected = set(first_node)
    # 선탠된 노드에 연결된 간선을 간선 리스트에 삽입
    candidated_edge = adjacent_edges[first_node]
    # 오름 차순으로 정렬
    heapify(candidated_edge)

    while candidated_edge:
        weight, node1, node2 = heappop(candidated_edge)
        # 사이클 있는지 확인 후 연결
        if node2 not in connected:
            connected.add(node2)
            mst.append((weight, node1, node2))

            for edge in adjacent_edges[node2]:
                if edge[2] not in connected:
                    heappush(candidated_edge, edge)

    return mst
prim('A', edges)