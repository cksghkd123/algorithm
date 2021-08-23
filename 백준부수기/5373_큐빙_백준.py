rotation_list = [[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]]
def cubing(moves):
    for move in moves:
        if move[0] == 'L':
            line1 = [cube[3+dr][dc] for dr,dc in rotation_list]
            line2 = [cube[i][3] for i in range(12)]
            if move[1] == '-':
                for i in range(8):
                    cube[3+rotation_list[i][0]][rotation_list[i][1]] = line1[(i+2)%8]
                for i in range(12):
                    cube[i][3] = line2[(i+3)%12]
            elif move[1] == '+':
                for i in range(8):
                    cube[3+rotation_list[i][0]][rotation_list[i][1]] = line1[(i-2)%8]
                for i in range(12):
                    cube[i][3] = line2[(i-3)%12]

        elif move[0] == 'R':
            line1 = [cube[3+dr][6+dc] for dr,dc in rotation_list]
            line2 = [cube[i][5] for i in range(12)]
            if move[1] == '-':
                for i in range(8):
                    cube[3+rotation_list[i][0]][6+rotation_list[i][1]] = line1[(i+2)%8]
                for i in range(12):
                    cube[i][5] = line2[(i-3)%12]
            elif move[1] == '+':
                for i in range(8):
                    cube[3+rotation_list[i][0]][6+rotation_list[i][1]] = line1[(i-2)%8]
                for i in range(12):
                    cube[i][5] = line2[(i+3)%12]
        
        elif move[0] == 'F':
            line1 = [cube[3+dr][3+dc] for dr,dc in rotation_list]
            line2 = [cube[2][3+i] for i in range(3)] + [cube[3+i][6] for i in range(3)] + [cube[6][5-i] for i in range(3)] + [cube[5-i][2] for i in range(3)]
            if move[1] == '-':
                for i in range(8):
                    cube[3+rotation_list[i][0]][3+rotation_list[i][1]] = line1[(i+2)%8]
                for i in range(3):
                    cube[2][3+i] = line2[(i+3)%12]
                for i in range(3):
                    cube[3+i][6] = line2[((i+3)+3)%12]
                for i in range(3):
                    cube[6][5-i] = line2[((i+6)+3)%12]
                for i in range(3):
                    cube[5-i][2] = line2[((i+9)+3)%12]
            elif move[1] == '+':
                for i in range(8):
                    cube[3+rotation_list[i][0]][3+rotation_list[i][1]] = line1[(i-2)%8]
                for i in range(3):
                    cube[2][3+i] = line2[(i-3)%12]
                for i in range(3):
                    cube[3+i][6] = line2[((i+3)-3)%12]
                for i in range(3):
                    cube[6][5-i] = line2[((i+6)-3)%12]
                for i in range(3):
                    cube[5-i][2] = line2[((i+9)-3)%12]

        elif move[0] == 'B':
            line1 = [cube[9+dr][3+dc] for dr,dc in rotation_list]
            line2 = [cube[0][5-i] for i in range(3)] + [cube[3+i][0] for i in range(3)] + [cube[8][3+i] for i in range(3)] + [cube[5-i][8] for i in range(3)]
            if move[1] == '-':
                for i in range(8):
                    cube[9+rotation_list[i][0]][3+rotation_list[i][1]] = line1[(i+2)%8]
                for i in range(3):
                    cube[0][5-i] = line2[(i+3)%12]
                for i in range(3):
                    cube[3+i][0] = line2[((i+3)+3)%12]
                for i in range(3):
                    cube[8][3+i] = line2[((i+6)+3)%12]
                for i in range(3):
                    cube[5-i][8] = line2[((i+9)+3)%12]
            elif move[1] == '+':
                for i in range(8):
                    cube[9+rotation_list[i][0]][3+rotation_list[i][1]] = line1[(i-2)%8]
                for i in range(3):
                    cube[0][5-i] = line2[(i-3)%12]
                for i in range(3):
                    cube[3+i][0] = line2[((i+3)-3)%12]
                for i in range(3):
                    cube[8][3+i] = line2[((i+6)-3)%12]
                for i in range(3):
                    cube[5-i][8] = line2[((i+9)-3)%12]
        
        elif move[0] == 'U':
            line1 = [cube[dr][3+dc] for dr,dc in rotation_list]
            line2 = [cube[3][i] for i in range(9)] + [cube[11][5-i] for i in range(3)]
            if move[1] == '-':
                for i in range(8):
                    cube[rotation_list[i][0]][3+rotation_list[i][1]] = line1[(i+2)%8]
                for i in range(9):
                    cube[3][i] = line2[(i-3)%12]
                for i in range(3):
                    cube[11][5-i] = line2[((i+9)-3)%12]
            elif move[1] == '+':
                for i in range(8):
                    cube[rotation_list[i][0]][3+rotation_list[i][1]] = line1[(i-2)%8]
                for i in range(9):
                    cube[3][i] = line2[(i+3)%12]
                for i in range(3):
                    cube[11][5-i] = line2[((i+9)+3)%12]
        
        elif move[0] == 'D':
            line1 = [cube[6+dr][3+dc] for dr,dc in rotation_list]
            line2 = [cube[5][i] for i in range(9)] + [cube[9][5-i] for i in range(3)]
            if move[1] == '-':
                for i in range(8):
                    cube[6+rotation_list[i][0]][3+rotation_list[i][1]] = line1[(i+2)%8]
                for i in range(9):
                    cube[5][i] = line2[(i+3)%12]
                for i in range(3):
                    cube[9][5-i] = line2[((i+9)+3)%12]
            elif move[1] == '+':
                for i in range(8):
                    cube[6+rotation_list[i][0]][3+rotation_list[i][1]] = line1[(i-2)%8]
                for i in range(9):
                    cube[5][i] = line2[(i-3)%12]
                for i in range(3):
                    cube[9][5-i] = line2[((i+9)-3)%12]

t = int(input())
for _ in range(t):
    cube = [
    '   www   ',
    '   www   ',
    '   www   ',
    'gggrrrbbb',
    'gggrrrbbb',
    'gggrrrbbb',
    '   yyy   ',
    '   yyy   ',
    '   yyy   ',
    '   ooo   ',
    '   ooo   ',
    '   ooo   ']
    for row in range(12):
        cube[row] = list(cube[row])

    n = int(input())
    seq = input().split(' ')
    cubing(seq)
    for row in range(3):
        for col in range(3,6):
            print(cube[row][col],end='')
        print('')