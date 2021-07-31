import collections

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def bfs(row, col):
    deq = collections.deque()
    deq.append((0,row,col,0))
    visited[row][col][0] = 1

    while deq:
        count, row, col, index = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < n and 0 <= nc < m:
                if maze_list[nr][nc] != '#' and visited[nr][nc][index] == 0:
                    if maze_list[nr][nc].isupper():
                        if index & (1 << (ord(maze_list[nr][nc]) - ord('A'))):
                            visited[nr][nc][index] = 1
                            deq.append((count+1, nr, nc, index))

                    elif maze_list[nr][nc].islower():     
                        new_index = index | (1 << (ord(maze_list[nr][nc])- ord('a')))
                        if visited[nr][nc][new_index] == 0:
                            visited[nr][nc][new_index] = 1
                            deq.append((count+1, nr, nc, new_index))

                    elif maze_list[nr][nc] == '1':
                        return count+1

                    else:
                        visited[nr][nc][index] = 1
                        deq.append((count+1, nr, nc, index))
    
    return -1

n, m = map(int,input().split())
maze_list = []
for row in range(n):
    maze_list.append(list(input()))
    for col in range(m):
        if maze_list[row][col] == '0':
            start = (row, col)

visited = [[[0]*64 for _ in range(m)] for _ in range(n)]
sr, sc = start
result = bfs(sr, sc)

print(result)
