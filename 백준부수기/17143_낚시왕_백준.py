def fishing(col):
    for i in range(r):
        if map_list[i][col] != 0:
            result = shq_list[map_list[i][col]][4]
            del shq_list[map_list[i][col]]
            map_list[i][col] = 0
            return result
    else:
        return 0

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
def shq_moving():
    eaten_list = []
    for shaq in shq_list:
        row, col, speed, direction, size = shq_list[shaq]
        if map_list[row][col] == shaq:
            map_list[row][col] = 0
        nr = row + dr[direction]*speed
        nc = col + dc[direction]*speed
        nr = nr % (2*r-2)
        nc = nc % (2*c-2)
        if nr > r-1:
            nr = (2*(r-1))-nr
            direction = 1-direction
        if nc > c-1:
            nc = (2*(c-1))-nc
            direction = 5-direction
        shq_list[shaq] = [nr, nc, speed, direction, size]
        if map_list[nr][nc] == 0 or map_list[nr][nc] > shaq:
            map_list[nr][nc] = shaq
        else:
            if shq_list[map_list[nr][nc]][4] < size:
                eaten_list.append(map_list[nr][nc])
                map_list[nr][nc] = shaq
            else:
                eaten_list.append(shaq)
    for i in eaten_list:
        del shq_list[i]

r, c, m = map(int,input().split())
shq_list = {}
map_list = [[0 for _ in range(c)] for _ in range(r)]
for i in range(m):
    row, col, speed, direction, size = map(int,input().split())
    shq_list[i+1] = [row-1,col-1,speed,direction-1,size]
    map_list[row-1][col-1] = i+1

score = 0
for col in range(c):
    score += fishing(col)
    shq_moving()
print(score)