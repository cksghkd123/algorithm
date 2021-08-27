from pprint import pprint


def spread():
    for row in range(r):
        for col in range(c):
            if a[row][col] >= 5:
                for w in range(4):
                    nr = row + dr[w]
                    nc = col + dc[w]
                    if 0 <= nr < r and 0 <= nc < c and a[nr][nc] != -1:
                        b[nr][nc] += a[row][col] // 5
                        b[row][col] -= a[row][col] // 5
    for row in range(r):
        for col in range(c):
            a[row][col] += b[row][col]

def air_cleaning(index):
    que = []
    que.append(conditioner[index])

    if index == 0:
        ll = 0
        rr = conditioner[index][0]
    elif index == 1:
        ll = conditioner[index][0]
        rr = r-1
    
    if index == 0:
        movew = 0
    elif index == 1:
        movew = 2
    while que:
        row, col = que.pop()
        nr = row + dr[movew]
        nc = col + dc[movew]
        if (row,col) == conditioner[index]:
            que.append((nr,nc))
        else:
            if ll <= nr <= rr and 0 <= nc < c:
                if (nr,nc) == conditioner[index]:
                    a[row][col] = 0
                    break
                a[row][col] = a[nr][nc]
                que.append((nr,nc))
            else:
                if index == 0:
                    movew += 1
                elif index == 1:
                    movew -= 1
                    movew %= 4
                que.append((row, col))
    
r, c, t = map(int,input().split())
a = []
conditioner = []
for i in range(r):
    a.append(list(map(int,input().split())))
    if -1 in a[i]:
        conditioner.append((i,0))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for _ in range(t):
    b = [[0 for _ in range(c)] for _ in range(r)]
    spread()
    air_cleaning(0)
    air_cleaning(1)


result = 0
for row in range(r):
    result += sum(a[row])

result += 2

print(result)