from collections import deque

w = ((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))

def bfs(start):
    deq = deque()
    day_pass = 0
    for flo, row, col in start:
        deq.append((day_pass,flo,row,col))


    while deq:
        day_pass, flo, row, col = deq.popleft()

        for dw in w:
            nf = flo + dw[0]
            nr = row + dw[1]
            nc = col + dw[2]

            if 0 <= nf < H and 0 <= nr < N and 0 <= nc < M:
                if box_list[nf][nr][nc] == 0:
                    box_list[nf][nr][nc] = 1
                    deq.append((day_pass+1, nf, nr, nc))
    
    return day_pass

def check():
    for flo in range(H):
        for row in range(N):
            for col in range(M):
                if box_list[flo][row][col] == 0:
                    return -1
    
    return result
    

M, N, H = map(int,input().split())
box_list = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
start = []

for flo in range(H):
    for row in range(N):
        for col in range(M):
            if box_list[flo][row][col] == 1:
                start.append((flo,row,col))

result = bfs(start)
result = check()

print(result)