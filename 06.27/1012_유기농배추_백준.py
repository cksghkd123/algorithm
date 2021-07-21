from pprint import pprint
import collections


def bfs(x,y):
    deq = collections.deque()
    deq.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    visited[y][x] = True

    while deq:
        px, py = deq.popleft()
        for w in range(4):
            nx = px + dx[w]
            ny = py + dy[w]
            if 0 <= nx < M and 0 <= ny < N:
                if map_list[ny][nx] == 1:
                    if visited[ny][nx] == False:
                        visited[ny][nx] = True
                        deq.append((nx,ny))
                    
                        

T = int(input())
for _ in range(T):

    M,N,K = map(int, input().split())
    map_list = [[0 for _ in range(M)] for _ in range(N)]
    #pprint(map_list)    

    for _ in range(K):
        x, y = map(int, input().split())
        map_list[y][x] = 1
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    warm = 0

    for x in range(M):
        for y in range(N):
            if map_list[y][x] == 1 and visited[y][x] == False:
                bfs(x,y)
                warm += 1
    
    print(warm)