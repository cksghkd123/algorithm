
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

row = 2
col = 2
direction = [0, 1, 2, 3]
#북 동 남 서
for i in direction:
    nr = row + dr[(-i-1+2)%4]
    nc = col + dc[(-i-1+2)%4]
    print(nr,nc)