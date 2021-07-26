def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
n, m = map(int,input().split())

def combination(k, r, result):
    if len(result) == r:
        cc.append(result)
        return
    if k >= len(bhc_to_house):
        return
    else:
        combination(k+1, r, result + [k])
        combination(k+1, r, result)


city_map = []
house = []
bhc = []
center = [0,0]
for row in range(n):
    city_map.append(list(map(int,input().split())))
    for col in range(n):
        if city_map[row][col] == 1:
            house.append((row,col))
        elif city_map[row][col] == 2:
            bhc.append((row,col))

bhc_to_house = [[0]*len(house) for _ in range(len(bhc))]
for i in range(len(bhc)):
    for j in range(len(house)):
        bhc_to_house[i][j] = distance(bhc[i], house[j])

cc = []
combination(0, m, [])
INF = float('inf')

gg = INF

for k in cc:
    result = [INF]*len(house)
    for i in range(len(house)):
        for j in k:
            result[i] = min(result[i], bhc_to_house[j][i])

    kk = 0
    for t in result:
        kk += t
    gg = min(gg, kk) 

print(gg)
