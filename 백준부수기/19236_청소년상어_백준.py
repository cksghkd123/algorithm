dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
def moving_fishes():
    movin_list = []
    for number, info in fishes.items():
        if number == 17:
            continue
        fish_row, fish_col, direction = info
        for w in range(8):
            nr = fish_row + dr[(direction+w)%8]
            nc = fish_col + dc[(direction+w)%8]
            if 0 <= nr < 4 and 0 <= nc < 4:
                nd = (direction+w)%8
                next_fish = map_list[nr][nc]
                if next_fish == 0:
                    fishes[number] = [nr, nc, nd]
                    map_list[fish_row][fish_col] = 0
                    map_list[nr][nc] = number
                    movin_list.append((number, fish_row, fish_col, direction))
                elif next_fish == 17:
                    continue
                else:
                    fishes[number] = [nr, nc, nd]
                    fishes[next_fish][0] = fish_row
                    fishes[next_fish][1] = fish_col
                    map_list[fish_row][fish_col], map_list[nr][nc] = map_list[nr][nc], map_list[fish_row][fish_col]
                    movin_list.append((number, fish_row, fish_col, direction))
                break
                    
    return movin_list



def moving_shq(map_list, fishes, shq_row, shq_col, direction, score):
    init_row = shq_row
    init_col = shq_col
    go_home = False
    shq_row += dr[direction]
    shq_col += dc[direction]
    while 0 <= shq_row < 4 and 0 <= shq_col < 4:
        if map_list[shq_row][shq_col] != 0:
            go_home = True
            map_list[init_row][init_col] = 0
            eaten = map_list[shq_row][shq_col]
            fishes[17] = fishes[eaten][2]
            del fishes[eaten]
            map_list[shq_row][shq_col] = 17
            print("전")
            print(map_list)
            moves = moving_fishes()
            print("후")
            print(map_list)
            moving_shq(map_list, fishes, shq_row, shq_col, fishes[17], score+eaten)
            map_list[shq_row][shq_col] = eaten
            map_list[init_row][init_col] = 17
            fishes[eaten] = [shq_row,shq_col,fishes[17]]
            fishes[17] = direction
            for n, r, c, d in reversed(moves):
                map_list[fishes[n][0]][fishes[n][1]], map_list[r][c] = map_list[r][c], map_list[fishes[n][0]][fishes[n][1]]
                fishes[n][2] = d

        shq_row += dr[direction]
        shq_col += dc[direction]

    if go_home == False:
        global result
        print(map_list, score)
        result = max(result, score)


map_list = [[] for _ in range(4)]
fishes = {i:0 for i in range(1,17)}
for i in range(4):
    line_list = list(map(int,input().split()))
    for j in range(4):
        map_list[i].append(line_list[j*2])
        fishes[line_list[j*2]] = [i, j, line_list[j*2+1]-1]

result = 0
first_eaten = map_list[0][0]
#shq >> fishes[17]
fishes[17] = fishes[first_eaten][2]
del fishes[first_eaten]
map_list[0][0] = 17
moving_fishes()
print(map_list)
moving_shq(map_list,fishes,0,0,fishes[17],first_eaten)

print(result)