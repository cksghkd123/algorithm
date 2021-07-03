import collections



def bfs(row,col):
    dr = [0,0,1,-1,1,1,-1,-1]
    dc = [1,-1,0,0,1,-1,1,-1]
    deq = collections.deque() 
    deq.append((row,col))

    while deq:
        row, col = deq.popleft()

        for i in range(8):
            nr = row + dr[i]
            nc = col + dc[i]
            
            if 0 <= nr < h and 0 <= nc < w:
                if visited[nr][nc] == False and map_list[nr][nc] == 1:
                    visited[nr][nc] = True
                    deq.append((nr,nc))


while 1:
    w, h = map(int, input().split())
    map_list = []
    if w == 0 and h == 0:
        break
    for _ in range(h):
        map_list.append(list(map(int,input().split())))
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    count = 0

    for row in range(h):
        for col in range(w):
            if visited[row][col] == False and map_list[row][col] == 1:
                bfs(row,col)
                count += 1
    
    print(count)