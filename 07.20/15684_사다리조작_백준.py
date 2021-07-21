def draw_lines(add_lines, ladder_init):
    for a, b in add_lines:
        ladder_init[a][b] = (1, 1)
        ladder_init[a][b+1] = (1, -1)

def check_ii(number, ladder_info):
    point = (0, number)
    for i in range(h):
        go = ladder_info[point[0]][point[1]]
        point = tuple(map(lambda x, y: x+y , go, point))
    return point[1]

def ladder_check():
    for i in range(n):
        ii = check_ii(i, ladder_info)
        if i != ii:
            return False
    return True

def combination(row, col, k):
    global button
    
    if button == True:
        return
    
    if k == plus_line:
        if ladder_check():
            button = True
        return

    if row >= h:
        return

    nc = col + 1
    nr = row
    
    if nc > n-2:
        nc = nc % (n-1)
        nr = row + 1

    if ladder_info[row][col] == (1,0) and ladder_info[row][col+1] == (1,0): 
        ladder_info[row][col] = (1,1)
        ladder_info[row][col+1] = (1,-1)
        combination(nr, nc, k+1)
        ladder_info[row][col] = (1,0)
        ladder_info[row][col+1] = (1,0)
        combination(nr, nc, k)
   
    else:
        combination(nr, nc, k)

    


n, m, h = map(int,input().split())
lines = []
for i in range(m):
    x, y = map(int,input().split())
    lines.append((x-1, y-1))
ladder_info = [[(1, 0) for _ in range(n)] for _ in range(h)]
ladder_info.append([i for i in range(n)])

draw_lines(lines, ladder_info)

if h%2 == 0:
    rangeend = (n-1)*h//2 - len(lines) + 1
else:
    rangeend = (n-1)*h//2 + 1 - len(lines) + 1

for plus_line in range(rangeend):
    button = False
    combination(0, 0, 0)
    if button:
        print(plus_line)
        break
    
    if plus_line == (rangeend - 1):
        print('-1')