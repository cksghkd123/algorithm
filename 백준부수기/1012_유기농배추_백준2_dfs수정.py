from pprint import pprint

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dfs(fr,fc):
    visited[fc][fr] = 1
    col = fc
    row = fr
    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]
        if 0 <= nr < M and 0 <= nc < N:
                if map_list[nc][nr] == 1:
                    if visited[nc][nr] == 0:
                        dfs(nr,nc)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    map_list = [[0 for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        row, col = map(int,input().split())
        map_list[col][row] = 1

    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    warm = 0

    for row in range(M):
        for col in range(N):
            if map_list[col][row] == 1 and visited[col][row] == 0:
                dfs(row,col)
                warm += 1
    
    print(warm)
