n, k = map(int,input().split())
bowls = list(map(int,input().split()))

def first_shuffle():
    side = 1
    count = 1

    while count+side+side+1 <= n:
        count += side+side+1
        side += 1

    rotate_count = 2*(side-1)

    if n-count >= side:
        rotate_count += 1


    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    d = rotate_count%4

    map_list = [[0 for _ in range(side)] for _ in range(side)]

    row, col = side//2, side//2

    if side%2 == 0:
        if d == 0:
            col -= 1
        elif d == 1:
            row -= 1
            col -= 1
        elif d == 2:
            row -= 1
    map_list[row][col] = 0
    x2 = 0
    x1 = 1
    button = 0

    for number in range(1,count):
        row += direction[d][0]
        col += direction[d][1]
        
        map_list[row][col] = number

        x2 += 1
        if x2 == x1:
            button += 1
            x2 = 0
            d -= 1
            d %= 4
        if button == 2:
            x1 += 1
            button = 0

    if n-count >= side:
        map_list.append([i for i in range(count,n)])
    else:
        map_list[-1].extend([i for i in range(count,n)])

    return map_list

def second_shuffle():
    map_list = [[0 for _ in range(n//4)] for _ in range(4)]
    direction = [3*n//4-1, n//4, n//4-1, 3*n//4,0]
    count = 0
    d = 0
    i = direction[d]
    button = -1
    for row in range(4):
        for col in range(n//4):
            map_list[row][col] = i
            count += 1
            if count == n//4:
                d += 1
                i = direction[d]
                button *= -1
                count = 0
            else:
                i += button
    
    return map_list

def common_shuffle(map_list):
    new_map_list = []
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for col in range(len(map_list[-1])):
        for row in range(len(map_list)-1,-1,-1):
            try:
                map_list[row][col]
            except:
                continue
            
            new_map_list.append(map_list[row][col])
            for d in range(4):
                nr = row + dr[d]
                nc = col + dc[d]
                if 0 <= nr < len(map_list) and 0 <= nc <len(map_list[nr]):
                    if map_list[row][col] > map_list[nr][nc]:
                        new_map_list[-1] -= abs(map_list[row][col]-map_list[nr][nc])//5
                    else:
                        new_map_list[-1] += abs(map_list[row][col]-map_list[nr][nc])//5
    return new_map_list


count = 0

after_first = first_shuffle()
after_second = second_shuffle()
while True:
    if max(bowls) - min(bowls) <= k:
        break
    m = min(bowls)
    for i in range(n):
        if bowls[i] == m:
            bowls[i] += 1
    count += 1
    bowl_list = []
    for row in range(len(after_first)):
        bowl_list.append([])
        for col in range(len(after_first[row])):
            bowl_list[-1].append(bowls[after_first[row][col]])
    bowls = common_shuffle(bowl_list)
    bowl_list = []
    for row in range(len(after_second)):
        bowl_list.append([])
        for col in range(len(after_second[row])):
            bowl_list[-1].append(bowls[after_second[row][col]])
    bowls = common_shuffle(bowl_list)


print(count)


