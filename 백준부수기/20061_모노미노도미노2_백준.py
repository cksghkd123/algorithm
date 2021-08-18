n = int(input())

green_block = [[0 for _ in range(4)] for _ in range(6)]
blue_block = [[0 for _ in range(4)] for _ in range(6)]
point = 0

for _ in range(n):
    t, r, c = map(int,input().split())

    if t == 1:
        for i in range(2,6):
            if green_block[i][c] != 0:
                green_block[i-1][c] = 1
                break
        else:
            green_block[5][c] = 1
        for i in range(2,6):
            if blue_block[i][r] != 0:
                blue_block[i-1][r] = 1
                break
        else:
            blue_block[5][r] = 1

    elif t == 2:
        for i in range(2,6):
            if green_block[i][c] != 0 or green_block[i][c+1] != 0:
                green_block[i-1][c] = 2
                green_block[i-1][c+1] = 2
                break
        else:
            green_block[5][c] = 2
            green_block[5][c+1] = 2
        for i in range(2,6):
            if blue_block[i][r] != 0:
                blue_block[i-1][r] = 1
                blue_block[i-2][r] = 1
                break
        else:
            blue_block[5][r] = 1
            blue_block[4][r] = 1

    elif t == 3:
        for i in range(2,6):
            if green_block[i][c] != 0:
                green_block[i-1][c] = 1
                green_block[i-2][c] = 1
                break
        else:
            green_block[5][c] = 1
            green_block[4][c] = 1
        for i in range(2,6):
            if blue_block[i][r] != 0 or blue_block[i][r+1] != 0:
                blue_block[i-1][r] = 2
                blue_block[i-1][r+1] = 2
                break
        else:
            blue_block[5][r] = 2
            blue_block[5][r+1] = 2
    
    combo_button = True
    while combo_button:
        pt = point
        for i in range(6):
            for j in range(4):
                if green_block[i][j] == 0:
                    break
            else:
                green_block = [[0, 0, 0, 0]] + green_block[:i] + green_block[i+1:]
                point += 1
            for j in range(4):
                if blue_block[i][j] == 0:
                    break
            else:
                blue_block = [[0, 0, 0, 0]] + blue_block[:i] + blue_block[i+1:]
                point += 1
        
        if pt == point:
            combo_button = False
                
    
    for row in range(2):
        if sum(green_block[row]) != 0:
            index = row
            green_block = [[0, 0, 0, 0] for _ in range(2)] + green_block[row:row+4]
            break
    
    for row in range(2):
        if sum(blue_block[row]) != 0:
            index = row
            blue_block = [[0, 0, 0, 0] for _ in range(2)] + blue_block[row:row+4]
            break
    

blocks = 0  
for row in range(6):
    for col in range(4):
        if green_block[row][col] != 0:
            blocks += 1

        if blue_block[row][col] != 0:
            blocks += 1

print(point)
print(blocks)