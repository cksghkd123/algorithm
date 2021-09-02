table_size, many_shq, smell_count = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(table_size)]
smell_list = [[[0,0] for _ in range(table_size)] for _ in range(table_size)]

#1 위 #2 아래 #3 왼 #4 오른
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
sharks = {i+1: [] for i in range(many_shq)}

#sharks [0] = [row, col, direction] , sharks[1~4] = 방향에 따른 우선순위

for row in range(table_size):
    for col in range(table_size):
        if map_list[row][col] != 0:
            sharks[map_list[row][col]].append([row, col])

d = list(map(int,input().split()))
for i in range(many_shq):
    sharks[i+1][0].append(d[i])
for i in range(many_shq*4):
    sharks[i//4 + 1].append(list(map(int,input().split())))

time = 0

#시작
while len(sharks) > 1:

    #냄새 뿌림
    for shark_number in range(1, many_shq+1):
        if shark_number not in sharks:
            continue
        row, col, direction = sharks[shark_number][0]
        smell_list[row][col] = [shark_number, smell_count]

    #상어 이동
    for shark_number in range(1, many_shq+1):
        if shark_number not in sharks:
            continue
        row, col, direction = sharks[shark_number][0]
        if map_list[row][col] == shark_number:
            map_list[row][col] = 0
        for w in range(4):
            nd = sharks[shark_number][direction][w]
            nr = row + dr[nd]
            nc = col + dc[nd]
            if 0 <= nr < table_size and 0 <= nc < table_size:
                if smell_list[nr][nc][0] == 0:
                    if map_list[nr][nc] != 0 and shark_number > map_list[nr][nc]:
                        del sharks[shark_number]
                        break
                    else:
                        map_list[nr][nc] = shark_number
                        sharks[shark_number][0] = [nr, nc, nd]
                        break
        else:
            for w in range(4):
                nd = sharks[shark_number][direction][w]
                nr = row + dr[nd]
                nc = col + dc[nd]
                if 0 <= nr < table_size and 0 <= nc < table_size:
                    if smell_list[nr][nc][0] == shark_number:
                        map_list[nr][nc] = shark_number
                        sharks[shark_number][0] = [nr, nc, nd]
                        break

    #시간 경과
    for row in range(table_size):
        for col in range(table_size):
            if smell_list[row][col][0] != 0:
                smell_list[row][col][1] -= 1
                if smell_list[row][col][1] == 0:
                    smell_list[row][col][0] = 0

    if time > 1000:
        break
    time += 1


if time > 1000:
    result = -1
else:
    result = time

print(result)