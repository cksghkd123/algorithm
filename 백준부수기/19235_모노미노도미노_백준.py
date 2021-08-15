n = int(input())

green_block = [[0 for _ in range(4)] for _ in range(6)]
blue_block = [[0 for _ in range(4)] for _ in range(6)]
point = 0

for _ in range(n):
    t, r, c = map(int,input().split())

    #블럭 쌓기
    if t == 1:
        for i in range(2,6):
            if green_block[i][c] != 0:
                green_block[i-1][c] = 1
                break
        for i in range(2,6):
            if blue_block[i][r] != 0:
                blue_block[i-1][r] = 1
                break

    elif t == 2:
        for i in range(2,6):
            if green_block[i][c] != 0 or green_block[i][c+1] != 0:
                green_block[i-1][c] = 1
                green_block[i-1][c+1] = 1
                break
        for i in range(2,6):
            if blue_block[i][r] != 0:
                blue_block[i-1][r] = 1
                blue_block[i-2][r] = 1
                break

    elif t == 3:
        for i in range(2,6):
            if green_block[i][c] != 0:
                green_block[i-1][c] = 1
                green_block[i-2][c] = 1
                break
        for i in range(2,6):
            if blue_block[i][r] != 0 or blue_block[i][r+1] != 0:
                blue_block[i-1][r] = 1
                blue_block[i-1][r+1] = 1
                break
    
    #채워진 행, 열 지우고 점수올리기
    for i in range(6):
        if sum(green_block[i]) == 4:
            green_block[i] = [0, 0, 0, 0]
            point += 1
        if sum(blue_block[i]) == 4:
            blue_block[i] = [0, 0, 0, 0]
            point += 1

    #내리기
    
        
    