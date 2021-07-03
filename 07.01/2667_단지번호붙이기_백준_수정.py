import collections
from pprint import pprint

#map_list[row][col] == 1 이면 아직 조사하지 않은집
#조사한 집은 1부터가 아닌 2부터 번호가 메겨짐
#이때문에 조건문에서 visited가 필요없어짐

def bfs(row,col):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    deq = collections.deque()
    deq.append((row,col)) 
    house = 0
    map_list[row][col] = len(howmanyhouse)+2

    while deq:
        row, col = deq.popleft()
        house += 1

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
        
            if 0 <= nr < N and 0 <= nc < N:
                if map_list[nr][nc] == 1:
                    deq.append((nr,nc))
                    map_list[nr][nc] = len(howmanyhouse) + 2
    
    howmanyhouse.append(house)

    

N = int(input())

map_list = []
for _ in range(N):
    map_list.append(list(map(int,input())))

howmanyhouse = []


for row in range(N):
    for col in range(N):    
        if map_list[row][col] == 1:
                bfs(row,col)
        
print(len(howmanyhouse))

howmanyhouse.sort()
for i in range(len(howmanyhouse)):
    if i == len(howmanyhouse) - 1:
        print(howmanyhouse[i], end="")
    else:
        print(howmanyhouse[i])