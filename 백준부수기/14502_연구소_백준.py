from pprint import pprint
from collections import deque
import copy


def combination(list, k, r, result, comset):
    if len(result) == r:
        comset.append(result)
        return
    if k >= len(list):
        return
    else:
        combination(list, k+1, r, result + [list[k]], com_room)
        combination(list, k+1, r, result, com_room)

def build_walls(new_wall):
    new_map_list = copy.deepcopy(map_list)
    for row, col in new_wall:
        new_map_list[row][col] = 1
    return new_map_list
    

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def bfs():
    no_viruszone = len(room) - 3

    deq = deque()
    for v in virus:
        visited[v[0]][v[1]] = True
        deq.append(v)

    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == False and new_map_list[nr][nc] == 0:
                    visited[nr][nc] = True
                    no_viruszone -= 1
                    deq.append((nr, nc))
    
    return no_viruszone



n, m = map(int,input().split())
virus = []
room = []
map_list = [list(map(int,input().split())) for _ in range(n)]
for row in range(n):
    for col in range(m):
        if map_list[row][col] == 2:
            virus.append((row, col))
        elif map_list[row][col] == 0:
            room.append((row, col))

com_room = []
combination(room, 0, 3, [], com_room)
maxresult = -1

for new_wall in com_room:

    new_map_list = build_walls(new_wall)
    visited = [[False]*m for _ in range(n)]
    result = bfs()
    maxresult = max(result, maxresult)

print(maxresult)
