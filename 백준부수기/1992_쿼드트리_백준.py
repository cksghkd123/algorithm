answer = ''
def QTree(row:int, col:int, length:int):
    global answer
    standard = map_list[row][col]
    button = False

    for i in range(row, row+length):
        for j in range(col, col+length):
            if map_list[i][j] != standard:
                answer += '('
                for cr, cc in confidence:
                    nr = row+int(length*cr)
                    nc = col+int(length*cc)
                    QTree(nr, nc, length//2)
                answer += ')'
                button = True
                break
        if button == True:
                break

    if button == False and i == row+length-1 and j == col+length-1:
        answer += str(standard)



n = int(input())
map_list = []
for _ in range(n):
    map_list.append(list(map(int,list(input()))))

confidence = [(0,0), (0,0.5), (0.5,0), (0.5,0.5)]
QTree(0,0,n)


print(answer)