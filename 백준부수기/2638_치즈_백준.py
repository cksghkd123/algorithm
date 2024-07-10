import collections
from pprint import pprint


N, M = map(int, input().split())
map_list = [[0 for _ in range(M + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0 for _ in range(M + 2)]]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
visited = [[0 for _ in range(M+2)] for _ in range(N+2)]

answer = -1

air_list = collections.deque([(0, 0)])
visited[0][0] = 1

def time_pass(array: collections.deque):
    next_array = collections.deque()
    while array:
        cr, cc = array.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            if 0 <= nr < N+2 and 0 <= nc < M+2:
                if map_list[nr][nc] == 0:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        array.append((nr, nc))
                else:
                    if visited[nr][nc] == 1:
                        next_array.append((nr, nc))
                    visited[nr][nc] += 1
    
    return next_array

while air_list:
    air_list = time_pass(air_list)
    answer += 1

print(answer)