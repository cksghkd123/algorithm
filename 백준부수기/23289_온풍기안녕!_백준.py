from collections import defaultdict, deque
from copy import deepcopy

axis_d = [(0,1),(0,-1),(-1,0),(1,0)]
vert_d = [(1,0),(1,0),(0,1),(0,1)]
def heating(d, h_r, h_c):

    a_d = axis_d[d-1]
    v_d = vert_d[d-1]
    spread_visited = [[False for _ in range(c)] for _ in range(r)]

    deq = deque()
    row = h_r+a_d[0]
    col = h_c+a_d[1]
    if 0 <= row < r and 0 <= col < c:
        deq.append((row, col , 4))
        add_temperature[row][col] += 5
    while deq:
        row, col, t = deq.popleft()
        if t == 0:
            continue
        n_r, n_c = row+a_d[0], col+a_d[1]
        if 0 <= n_r < r and 0 <= n_c < c:
            if not wall[(row, col, n_r, n_c)] and not spread_visited[n_r][n_c]:
                spread_visited[n_r][n_c] = True
                add_temperature[n_r][n_c] += t
                deq.append((n_r, n_c, t-1))
        for i in [1,-1]:
            s_r, s_c = row+v_d[0]*i, col+v_d[1]*i
            if 0 <= s_r < r and 0 <= s_c < c and 0 <= s_r+a_d[0] < r and 0 <= s_c+a_d[1] < c:
                if not wall[(row, col, s_r, s_c)] and not wall[(s_r, s_c, s_r+a_d[0], s_c+a_d[1])] and not spread_visited[s_r+a_d[0]][s_c+a_d[1]]:
                    spread_visited[s_r+a_d[0]][s_c+a_d[1]] = True
                    add_temperature[s_r+a_d[0]][s_c+a_d[1]] += t
                    deq.append((s_r+a_d[0], s_c+a_d[1], t-1))
    
       

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def control():
    pre_map = deepcopy(temperature_map)
    
    for s_r in range(r):
        for s_c in range(c):
            for i in range(4):
                nr = s_r + dr[i]
                nc = s_c + dc[i]
                if 0 <= nr < r and 0 <= nc < c:
                    if not wall[(s_r, s_c, nr, nc)]:
                        dif = (pre_map[s_r][s_c]-pre_map[nr][nc])
                        if dif < 0:
                            dif = (abs(dif)//4)*-1
                        else:
                            dif = dif//4
                        temperature_map[nr][nc] += dif


def cooling():
    for col in range(0, c):
        if temperature_map[0][col]:
            temperature_map[0][col] -= 1
        if temperature_map[r-1][col]:
            temperature_map[r-1][col] -= 1
    
    for row in range(1, r-1):
        if temperature_map[row][0]:
            temperature_map[row][0] -= 1
        if temperature_map[row][c-1]:
            temperature_map[row][c-1] -= 1


r, c, k = map(int,input().split())
check_room = []
heater_list = []
temperature_map = [[0 for _ in range(c)] for _ in range(r)]
add_temperature = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    row_list = list(map(int,input().split()))
    for j in range(c):
        if row_list[j] == 5:
            check_room.append((i,j))
        elif row_list[j] != 0:
            heater_list.append((row_list[j],i,j))

wall = defaultdict(bool)

w = int(input())
for _ in range(w):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall[(x,y,x-1,y)] = True
        wall[(x-1,y,x,y)] = True
    elif t == 1:
        wall[(x,y,x,y+1)] = True
        wall[(x,y+1,x,y)] = True

chocolate = 0
for direction, row, col in heater_list:
    heating(direction, row, col)

for _ in range(101):
    #온풍기
    for row in range(r):
        for col in range(c):
            temperature_map[row][col] += add_temperature[row][col]
            
    #온도가 조절됨
    control()
    
    # 온도가 1이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    cooling()

    #초콜렛을 하나 먹는다
    chocolate += 1

    #조사하는 모든 칸의 온도가 k 이상?
    for row, col in check_room:
        if temperature_map[row][col] < k:
            break
    else:
        break


print(chocolate)


