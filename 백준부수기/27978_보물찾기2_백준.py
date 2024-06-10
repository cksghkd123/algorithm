import heapq
import pprint


h, w = map(int, input().split())

map_list = [list(input()) for _ in range(h)]

# . 바다 # 암초 * 보물 K 배

# 12시부터 시계방향
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

ship_point = (0,0)

visited = [[False for _ in range(w)] for _ in range(h)]

for row in range(h):
    for col in range(w):
        if map_list[row][col] == 'K':
            ship_point = (row, col)
            visited[row][col] = True

heap = [(0,*ship_point)]
answer = -1

while heap:
    fuel, cr, cc = heapq.heappop(heap)
    if map_list[cr][cc] == '*':
        answer = fuel
        break

    for i in range(8):
        nr = cr + dr[i]
        nc = cc + dc[i]

        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
            if map_list[nr][nc] == '#':
                continue
            elif map_list[nr][nc] == '.' or map_list[nr][nc] == '*':
                if 1 <= i <= 3:
                    heapq.heappush(heap, (fuel, nr, nc))
                else:
                    heapq.heappush(heap, (fuel+1, nr, nc))
                visited[nr][nc] = True
    
print(answer)