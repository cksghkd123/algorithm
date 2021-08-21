def dice_move(bottom ,row, col):
    if map_list[row][col] == 0:
        map_list[row][col] = dice[bottom]
    else:
        dice[bottom] = map_list[row][col]
        map_list[row][col] = 0

n, m, x, y, k = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(n)]
dice = [0 for _ in range(7)]
bottom = 1
dice_info = [3, 4, 2, 5]

mo = list(map(int,input().split()))
for move in mo:
    if move == 1:
        if y+1 < m:
            y += 1
            s = bottom
            bottom = dice_info[0]
            dice_info = [7-s, s, dice_info[2], dice_info[3]]
        else:
            continue
    elif move == 2:
        if 0 <= y-1:
            y -= 1
            s = bottom
            bottom = dice_info[1]
            dice_info = [s, 7-s, dice_info[2], dice_info[3]]
        else:
            continue
    elif move == 3:
        if 0 <= x-1:
            x -= 1
            s = bottom
            bottom = dice_info[2]
            dice_info = [dice_info[0], dice_info[1], 7-s, s]
        else:
            continue
    elif move == 4:
        if x+1 < n:
            x += 1
            s = bottom
            bottom = dice_info[3]
            dice_info = [dice_info[0], dice_info[1], s, 7-s]
        else:
            continue
    dice_move(bottom, x, y)
    top = 7-bottom
    print(dice[top])

    
