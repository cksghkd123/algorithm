from pprint import pprint
import collections


def bfs():
    deq = collections.deque()
    oneday = collections.deque()
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    daypassed = 0


    for row in range(N):
        for col in range(M):
            if box[row][col] == 1:
                deq.append((row,col))
    while deq:
        while deq:
            oneday.append(deq.popleft())
    
        while oneday:
            row, col = oneday.popleft()
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]
                if 0 <= nr < N and 0 <= nc < M:
                    if box[nr][nc] == 0:
                        box[nr][nc] = 1
                        deq.append((nr,nc))
        
        daypassed += 1
    
    for i in range(N):
        if 0 in box[i]:
            return -1
    return daypassed - 1
    

M, N = map(int,input().split())

box = []
for _ in range(N):
    box.append(list(map(int,input().split())))

print(bfs())

