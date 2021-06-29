import collections
from pprint import pprint


def bfs(row,col):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    deq = collections.deque()
    deq.append((row,col))
    global count 
    count += 1
    house = 0

    while deq:
        visited[row][col] = True
        row, col = deq.popleft()
        map_list[row][col] = count
        house += 1

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
        
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == False and map_list[nr][nc] == 1:
                    deq.append((nr,nc))
                    visited[nr][nc] = True
    
    howmanyhouse.append(house)

    

N = int(input())

map_list = []
for _ in range(N):
    map_list.append(list(map(int,input())))

visited = [[False for _ in range(N)] for _ in range(N)]

count = 0
howmanyhouse = []


for row in range(N):
    for col in range(N):    
        if map_list[row][col] == 1:
            if visited[row][col] == False:
                bfs(row,col)
        
print(count)

howmanyhouse.sort()
for i in howmanyhouse:
    if i == howmanyhouse[len(howmanyhouse)-1]:
        print(i,end='')
    else:
        print(i)
