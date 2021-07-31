import collections


dr = [0, 0, 1, -1]
dc = [1, -1, 0 ,0]
def bfs():
    deq = collections.deque()
    deq.append((1,0,0,0))
    if n-1 == 0 and m-1 == 0:
        return 1  


    while deq:
        count, row, col, wall_break = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < n and 0 <= nc < m:
                if nr == n-1 and nc == m-1:
                    return count+1

                if map_list[nr][nc] == 0:
                    if wall_break == 0:
                        if visited[nr][nc] == 0 or visited[nr][nc] == 1:
                            visited[nr][nc] = 2
                            deq.append((count+1, nr, nc, wall_break))

                    elif wall_break == 1:
                        if visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            deq.append((count+1, nr, nc, wall_break))

                elif map_list[nr][nc] == 1 and wall_break == 0:
                    visited[nr][nc] = 2
                    deq.append((count+1, nr, nc, wall_break+1))

                

               
    return -1
    

n, m = map(int,input().split())
map_list = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
result = bfs()

print(result)