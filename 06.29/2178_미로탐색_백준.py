import collections
from pprint import pprint


dr = [0,0,1,-1]
dc = [1,-1,0,0]
deq = collections.deque()
end = []

def Miro():
    row = 0
    col = 0
    deq.append((row,col))
    visited[row][col] = '시작'

    while deq:
        row, col = deq.popleft()
        direction = 0

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]


            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == False and Map_list[nr][nc] == '1':
                    if (nr,nc) in deq:
                        continue
                    else:
                        deq.append((nr,nc))
                        direction += 1
                    #w = 0 1 2 3 우 좌 하 상
                        if w == 0:
                            visited[nr][nc] = '우'
                        elif w == 1:
                            visited[nr][nc] = '좌'
                        elif w == 2:
                            visited[nr][nc] = '하'
                        elif w == 3:
                            visited[nr][nc] = '상'


        if row == N-1 and col == M-1:
            end.append((row,col))
        elif direction == 0 :
            end.append((row,col))

    count = 0

    for i in end:
        if i == (N-1,M-1):
            row = N-1
            col = M-1
            count = 0
            while 1 :
                count += 1
                if visited[row][col] == '우':
                    col -= 1
                elif visited[row][col] == '좌':
                    col += 1
                elif visited[row][col] == '하':
                    row -= 1
                elif visited[row][col] == '상':
                    row += 1
                elif visited[row][col] == '시작':
                    break
    
    return count

N, M = map(int,input().split())
Map_list = []

for _ in range(N):
    Map_list.append(list(input()))

visited = [[False for _ in range(M)] for _ in range(N)]

print(Miro())
