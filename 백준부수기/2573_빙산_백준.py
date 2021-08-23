import collections

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def one_year_passed(key):
    for row in range(n):
        for col in range(m):
            if map_list[row][col][key] == 0:
                map_list[row][col][1-key] = 0
            else:
                ice_melt = 0
                for w in range(4):
                    nr = row + dr[w]
                    nc = col + dc[w]
                    if 0 <= nr < n and 0 <= nc < m and map_list[nr][nc][key] == 0:
                        ice_melt += 1
                map_list[row][col][1-key] = map_list[row][col][key] - ice_melt
                if map_list[row][col][1-key] < 0:
                    map_list[row][col][1-key] = 0

def ice_mountain_check(row, col, key):
    visited[row][col] = True
    deq = collections.deque()
    deq.append((row, col))

    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == False and map_list[nr][nc][key] != 0:
                    visited[nr][nc] = True
                    deq.append((nr,nc))

n, m = map(int,input().split())
map_list = [list(map(lambda x : [int(x), 0],input().split())) for _ in range(n)]

k = 0
passed_time = 0
while True:
    mountain_count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if visited[row][col] == False and map_list[row][col][k] != 0:
                ice_mountain_check(row,col,k)
                mountain_count += 1
    
    if mountain_count >= 2:
        break
    elif mountain_count == 0:
        passed_time = 0
        break
    
    one_year_passed(k)
    passed_time += 1
    k = 1-k

print(passed_time)
