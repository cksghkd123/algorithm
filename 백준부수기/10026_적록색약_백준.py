import collections


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def bfs(row, col, collor):
    deq = collections.deque()
    deq.append((row, col))

    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False:
                if map_list[nr][nc] == collor:
                    visited[nr][nc] = True
                    deq.append((nr,nc))

def bfs_rg(row, col, collor):
    deq = collections.deque()
    deq.append((row, col))

    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False:
                if collor == 'R' or collor == 'G':
                    if map_list[nr][nc] == 'R' or map_list[nr][nc] == 'G':
                        visited[nr][nc] = True
                        deq.append((nr,nc))
                else:
                    if map_list[nr][nc] == collor:
                        visited[nr][nc] = True
                        deq.append((nr,nc))


n = int(input())
map_list = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
result1 = 0
result2 = 0
for row in range(n):
    for col in range(n):
        if visited[row][col] == False:
            visited[row][col] = True
            bfs(row, col, map_list[row][col])
            result1 += 1
visited = [[False for _ in range(n)] for _ in range(n)]
for row in range(n):
    for col in range(n):
        if visited[row][col] == False:
            bfs_rg(row, col, map_list[row][col])
            result2 += 1

print(result1, result2)