import collections
from pprint import pprint


def bfs(row,col):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    deq = collections.deque()
    deq.append((row,col)) 
    house = 0
    visited[row][col] = True
    map_list[row][col] = count

    while deq:
        row, col = deq.popleft()
        house += 1

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
        
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == False and map_list[nr][nc] == 1:
                    deq.append((nr,nc))
                    visited[nr][nc] = True
                    map_list[row][col] = count
    
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
                count += 1
                bfs(row,col)
        
print(count)

howmanyhouse.sort()
for i in range(len(howmanyhouse)):
    if i == len(howmanyhouse) - 1:
        print(howmanyhouse[i], end="")
    else:
        print(howmanyhouse[i])
