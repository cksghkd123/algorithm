from pprint import pprint


def sandstorm(row,col,direction,sandtotal):
    global outsand
    a = 0
    sand_storm = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if real_storm_list[direction][i][j] == 'a':
                ar = i
                ac = j
                continue
            sand_storm[i][j] = int(real_storm_list[direction][i][j] * sandtotal)
            a += sand_storm[i][j]

    a = sandtotal - a
    sand_storm[ar][ac] = a
    

    ro = row - 2
    co = col - 2
    sand_list[row][col] = 0
    for wr in range(5):
        for wc in range(5):
            nr = ro + wr
            nc = co + wc    
            if 0 <= nr < N and 0 <= nc < N:
                sand_list[nr][nc] += sand_storm[wr][wc]
            else:
                outsand += sand_storm[wr][wc]
    
    
    
    

N = int(input())
sand_list = [list(map(int,input().split())) for _ in range(N)]
outsand = 0

#storm list
real_storm_list = []
rstorm_list = []
ustorm_list = [[None]*5 for _ in range(5)]
dstorm_list = [[None]*5 for _ in range(5)]
lstorm_list = [
    [0,0,0.02,0,0],
    [0,0.1,0.07,0.01,0],
    [0.05,'a',0,0,0],
    [0,0.1,0.07,0.01,0],
    [0,0,0.02,0,0]]
for i in range(5):
    rstorm_list.append(list(reversed(lstorm_list[i])))
for i in range(5):
    for j in range(5):
        ustorm_list[i][j] = lstorm_list[j][i]
for i in range(5):
    for j in range(5):
        dstorm_list[i][j] = rstorm_list[j][i]
        
real_storm_list.append(lstorm_list)
real_storm_list.append(dstorm_list)
real_storm_list.append(rstorm_list)
real_storm_list.append(ustorm_list)



# 토네이도
wind_list = [[None]*N for _ in range(N)]
torlen = 1
tordir = [(0,-1),(1,0),(0,1),(-1,0)]
w = 0
row = int((N-1)/2)
col = int((N-1)/2)
while torlen < N+1:
    for _ in range(torlen):
        if row == 0 and col == 0:
            break
        wind_list[row][col] = tordir[w]
        row += tordir[w][0]
        col += tordir[w][1]
        sandstorm(row,col,w,sand_list[row][col])
    w += 1
    if w == 4:
        w -= 4
    if row == 0 and col == 0:
        break
    for _ in range(torlen):
        wind_list[row][col] = tordir[w]
        row += tordir[w][0]
        col += tordir[w][1]
        sandstorm(row,col,w,sand_list[row][col])
    w += 1
    if w == 4:
        w -= 4
    torlen += 1


print(outsand)


        
        