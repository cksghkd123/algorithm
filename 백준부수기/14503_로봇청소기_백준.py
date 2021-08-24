def clean(row, col):
    global count
    count += 1
    visited[row][col] = True

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
def find(row, col, direction):
    for w in range(4):
        nr = row + dr[(w-direction)%4]
        nc = col + dc[(w-direction)%4]
        if 0 <= nr < n and 0 <= nc < m and map_list[nr][nc] == 0 and visited[nr][nc] == False:
            clean(nr, nc)
            return find(nr, nc, (direction-1-w)%4)
    else:
        nr = row + dr[(-direction-1+2)%4]
        nc = col + dc[(-direction-1+2)%4]
        if 0 <= nr < n and 0 <= nc < m and map_list[nr][nc] == 0:
            return find(nr, nc, direction)
        else:
            return 


n, m = map(int,input().split())
r, c, d = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
count = 0
clean(r,c)
find(r, c, d)
print(count)

