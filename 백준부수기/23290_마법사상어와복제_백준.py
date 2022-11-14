from collections import deque


m, s = map(int,input().split())
fishes_point = deque()
for _ in range(m):
    fishes_point.append(list(map(lambda x: int(x)-1,input().split())))

shark_point = list(map(lambda x: int(x)-1,input().split()))
fish_can_go = [[0 for _ in range(4)] for _ in range(4)]
fish_map_list = [[0 for _ in range(4)] for _ in range(4)]
for r,c,d in fishes_point:
    fish_map_list[r][c] += 1

fish_direction = ((0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1))
shark_direction = ((-1,0), (0,-1), (1,0), (0,1))

def go_shark(row, col, result, count):
    if len(result) == 3:
        global track, mcount
        if not track:
            track = result
        if mcount < count:
            mcount = count
            track = result
        return

    for i in range(4):
        nr = row+shark_direction[i][0]
        nc = col+shark_direction[i][1]
        if 0 <= nr < 4 and 0 <= nc < 4:
            if visited[nr][nc] == False:
                visited[nr][nc] = True
                go_shark(nr, nc, result+[(nr,nc)], count+fish_map_list[nr][nc])
                visited[nr][nc] = False
            elif visited[nr][nc] == True:
                go_shark(nr, nc, result+[(nr,nc)], count)

for _ in range(s):
    copied_fishes = []
    i = len(fishes_point)
    for _ in range(i):
        r, c, d = fishes_point.popleft()
        copied_fishes.append((r,c,d))
        fish_map_list[r][c] -= 1
        for dd in range(8):
            nd = (d-dd)%8
            nr = r+fish_direction[nd][0]
            nc = c+fish_direction[nd][1]
            if 0 <= nr < 4 and 0 <= nc < 4 :
                if nr == shark_point[0] and nc == shark_point[1] or fish_can_go[nr][nc]:
                    continue
                fishes_point.append((nr,nc,nd))
                fish_map_list[nr][nc] += 1
                break
        else:
            fishes_point.append((r,c,d))
            fish_map_list[r][c] += 1
    mcount = 0
    track = []
    visited = [[False for _ in range(4)] for _ in range(4)]
    
    go_shark(*shark_point, [], 0)
    for r,c in track:
        if fish_map_list[r][c]:
            fish_can_go[r][c] = 3
            fish_map_list[r][c] = 0
    shark_point[0] = r
    shark_point[1] = c
    
    i = len(fishes_point)
    for _ in range(i):
        r, c, d = fishes_point.popleft()
        if (r,c) in track:
            continue
        else:
            fishes_point.append((r,c,d))



    for i in range(4):
        for j in range(4):
            if fish_can_go[i][j]:
                fish_can_go[i][j] -= 1


    for c_fish in copied_fishes:
        fishes_point.append(c_fish)
        fish_map_list[c_fish[0]][c_fish[1]] += 1

    

print(len(fishes_point))