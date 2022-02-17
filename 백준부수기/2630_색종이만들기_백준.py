n = int(input())
map_list = []
for _ in range(n):
    map_list.append(list(map(int,input().split())))

answer = {0:0, 1:0}

def counting_paper(First_row, First_col, length):
    number = map_list[First_row][First_col]
    Bbutton = False

    for dr in range(length):
        for dc in range(length):
            if map_list[First_row + dr][First_col + dc] != number:
                Bbutton = True
                for i in range(First_row, First_row+length, length//2):
                    for j in range(First_col, First_col+length, length//2):
                        counting_paper(i, j, length//2)
                break
        
        if Bbutton == True:
            break
    
        if dr == length-1 and dc == length-1:
            answer[number] += 1

counting_paper(0, 0, n)

for a in answer.values():
    print(a)
