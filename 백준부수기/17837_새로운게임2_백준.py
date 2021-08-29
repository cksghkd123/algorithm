import collections
from pprint import pprint

def white(number, nr, nc, row, col):
    move = []
    while True:
        next_number = union_info[row][col].pop()
        move.append(next_number)
        if next_number == number:
            break
    while move:
        next_number = move.pop()
        union_info[nr][nc].append(next_number)
        chess_info[next_number][0] = nr
        chess_info[next_number][1] = nc

    if len(union_info[nr][nc]) >= 4:
        return True

    return False

def red(number, nr, nc, row, col):
    while True:
        next_number = union_info[row][col].pop()
        chess_info[next_number][0] = nr
        chess_info[next_number][1] = nc
        union_info[nr][nc].append(next_number)
        if next_number == number:
            break
    if len(union_info[nr][nc]) >= 4:
        return True

    return False

def blue(number, row, col, direction):
    if direction < 2:
        direction = 1-direction
    else:
        direction = 5-direction
    chess_info[number][2] = direction
    nr = row + dr[direction]
    nc = col + dc[direction]
    if 0 <= nr < n and 0 <= nc < n:
        color = map_list[nr][nc]
        if color == 0:
            return white(number, nr, nc, row, col)
        elif color == 1:
            return red(number, nr, nc, row, col)

    return False

n, k = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(n)]
chess_info = [list(map(lambda x : int(x)-1,input().split())) for _ in range(k)]
union_info = [[collections.deque() for _ in range(n)] for _ in range(n)]
for i in range(len(chess_info)):
    union_info[chess_info[i][0]][chess_info[i][1]].append(i)
#0 흰 1 빨 2 파
dr = [0, 0, -1, 1]
dc = [1, -1, 0 ,0]

t = 0
button = False
while t < 1001:
    t += 1
    for i in range(len(chess_info)):
        number = i
        row, col, direction = chess_info[number]
        nr = row + dr[direction]
        nc = col + dc[direction]
        if 0 <= nr < n and 0 <= nc < n:
            color = map_list[nr][nc]
            if color == 0:
                button = white(number, nr, nc, row, col)
            elif color == 1:
                button = red(number, nr, nc, row, col)
            elif color == 2:
                button = blue(number, row, col, direction)
        else:
            button = blue(number, row, col, direction)

        if button == True:
            break

    if button == True:
        break

if t > 1000:
    t = -1

print(t)
