import collections
import copy


dr = [0,0,1,-1]
dc = [1,-1,0,0]
deq = collections.deque()

def bfs(row,col):
    deq.append((row,col))
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < M:
                if mapcase[nr][nc] == 0:
                    mapcase[nr][nc] = 2
                    deq.append((nr,nc))


N, M = map(int,input().split())
map_list = []
virusspot = []
blank = []

for i in range(N):
    map_list.append(list((map(int,input().split()))))

for row in range(N):
    for col in range(M):
        if map_list[row][col] == 0:
            blank.append((row,col))
        elif map_list[row][col] == 2:
            virusspot.append((row,col))

count = 0
# 벽이 세워지는 경우의 수에 따른 출력값 조사

for a in range(0,len(blank)-3):
    for b in range(a+1,len(blank)-2):
        for c in range(b+1,len(blank)-1):
            mapcase = copy.deepcopy(map_list)
            wall = [blank[a],blank[b],blank[c]]
            for row,col in wall:
                mapcase[row][col] = 1
            for row,col in virusspot:
                bfs(row,col)

            ncount = 0
            for row in range(N):
                for col in range(M):
                    if mapcase[row][col] == 0:
                        ncount += 1
            
            if count < ncount :
                count = ncount

print(count)