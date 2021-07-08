import collections
from pprint import pprint

def bfs(row,col):
    deq = collections.deque()
    deq.append((row,col))
    visit[row][col] = True
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    while deq:
        row, col = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if region[nr][nc] > rain and visit[nr][nc] == False:
                        deq.append((nr,nc))
                        visit[nr][nc] = True



N = int(input())
region = [list(map(int,input().split())) for _ in range(N)]
maxrain = max(map(max,region))


safe_region = 1

for rain in range(1,maxrain):
    visit = [[False for _ in range(N)] for _ in range(N)]
    safe_region2 = 0
    for row in range(N):
        for col in range(N):
            if visit[row][col] == False and region[row][col] > rain:
                safe_region2 += 1
                bfs(row,col)
    safe_region = max(safe_region,safe_region2)

print(safe_region)