from pprint import pprint

def g_rain_it_one(row, col):
    green_block[row][col] = 0
    row += 1
    while row < 6:
        if green_block[row][col] != 0:
            green_block[row-1][col] = 1
            return
        row += 1
    
    green_block[5][col] = 1

def g_rain_it_two(row, col):
    green_block[row][col] = 0
    green_block[row][col+1] = 0
    row += 1
    while row < 6:
        if green_block[row][col] != 0 or green_block[row][col+1] != 0:
            green_block[row-1][col] = 2
            green_block[row-1][col+1] = 2
            return
        row += 1
    
    green_block[5][col] = 2
    green_block[5][col+1] = 2

def b_rain_it_one(row, col):
    blue_block[row][col] = 0
    row += 1
    while row < 6:
        if blue_block[row][col] != 0:
            blue_block[row-1][col] = 1
            return
        row += 1
    
    blue_block[5][col] = 1

def b_rain_it_two(row, col):
    blue_block[row][col] = 0
    blue_block[row][col+1] = 0
    row += 1
    while row < 6:
        if blue_block[row][col] != 0 or blue_block[row][col+1] != 0:
            blue_block[row-1][col] = 2
            blue_block[row-1][col+1] = 2
            return
        row += 1
    
    blue_block[5][col] = 2
    blue_block[5][col+1] = 2
    
        
n = int(input())

green_block = [[0 for _ in range(4)] for _ in range(6)]
blue_block = [[0 for _ in range(4)] for _ in range(6)]
point = 0

for _ in range(n):
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    t, r, c = map(int,input().split())

    #블럭 쌓기
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
    # print("쌓는다")
    # pprint(green_block)
    # pprint(blue_block)
    
    #채워진 행, 열 지우고 점수올리기
    combo_button = True
    while combo_button:
        pt = point
        for i in range(6):
            for j in range(4):
                if green_block[i][j] == 0:
                    break
            else:
                green_block[i] = [0, 0, 0, 0]
                point += 1
            for j in range(4):
                if blue_block[i][j] == 0:
                    break
            else:
                blue_block[i] = [0, 0, 0, 0]
                point += 1

        # print("블럭지우고점수올린다")
        # pprint(green_block)
        # pprint(blue_block)
        
        #내리기
        for row in range(5,-1,-1):
            col = 0
            while col < 4:
                if green_block[row][col] == 1:
                    g_rain_it_one(row, col)
                elif green_block[row][col] == 2:
                    g_rain_it_two(row, col)
                    col += 2
                    continue
                col += 1
            col = 0
            while col < 4:
                if blue_block[row][col] == 1:
                    b_rain_it_one(row, col)
                elif blue_block[row][col] == 2:
                    b_rain_it_two(row, col)
                    col += 2
                    continue
                col += 1
        
        if pt == point:
            combo_button = False
                
        # print("블럭떨어진다")
        # pprint(green_block)
        # pprint(blue_block)
    
    
    #연한박스 부분처리
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
    # print("블럭마무리한다")
    # pprint(green_block)
    # pprint(blue_block)
    

blocks = 0  
for row in range(6):
    for col in range(4):
        if green_block[row][col] != 0:
            blocks += 1

        if blue_block[row][col] != 0:
            blocks += 1

print(point)
print(blocks)