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
