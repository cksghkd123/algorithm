import sys
sys.setrecursionlimit(10**5)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dd = ['D', 'U', 'R', 'L']

def dfs(r, c):
    if 0 <= r < N and 0 <= c < M and not visited[r][c]:
        visited[r][c] = 1
        if map_list[r][c] == 'U':
            dfs(r-1, c)
        elif map_list[r][c] == 'D':
            dfs(r+1, c)
        elif map_list[r][c] == 'L':
            dfs(r, c-1)
        elif map_list[r][c] == 'R':
            dfs(r, c+1)
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if map_list[nr][nc] == dd[i]:
                dfs(nr, nc)

N, M = map(int, input().split())

map_list = [list(input()) for _ in range(N)]

answer = 0

visited = [[0 for _ in range(M)] for _ in range(N)]

for row in range(N):
    for col in range(M):
        if not visited[row][col]:
            dfs(row, col)
            answer += 1
print(answer)