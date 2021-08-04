import collections


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def island_naming(row, col, number):
    map_list[row][col] = number
    deq = collections.deque()
    deq.append((row, col))

    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < n and 0 <= nc < m:
                if map_list[nr][nc] == 1:
                    map_list[nr][nc] = number
                    deq.append((nr,nc))
    
def make_bridge_list():
    result = set()

    for row in range(n):
        i1 = None
        i2 = None
        count = 0
        for col in range(m):
            if 0 <= count < 2:
                if map_list[row][col] != 0:
                    i1 = map_list[row][col]
                    count = 0
                else:
                    if i1 != None:
                        count += 1
            else:
                if map_list[row][col] == 0:
                    count += 1
                elif map_list[row][col] == i1:
                    count = 0
                else:
                    i2 = map_list[row][col]
                    result.add((count, i1, i2))
                    count = 0
                    i1 = map_list[row][col]
                    i2 = None
                    
    for col in range(m):
        i1 = None
        i2 = None
        count = 0
        for row in range(n):
            if 0 <= count < 2:
                if map_list[row][col] != 0:
                    i1 = map_list[row][col]
                    count = 0
                else:
                    if i1 != None:
                        count += 1
            else:
                if map_list[row][col] == 0:
                    count += 1
                elif map_list[row][col] == i1:
                    count = 0
                else:
                    i2 = map_list[row][col]
                    result.add((count, i1, i2))
                    count = 0
                    i1 = map_list[row][col]
                    i2 = None
    
    return list(result)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(x1, x2):
    if find(x1) != find(x2):
        parent[find(x2)] = find(x1)

    
n, m = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(n)]

nn = 2
for i in range(n):
    for j in range(m):
        if map_list[i][j] == 1:
            island_naming(i, j, nn)
            nn += 1

bridge_list = make_bridge_list()


bridge_list.sort()

parent = [i for i in range(nn)]

result = 0
for i in range(len(bridge_list)):
    cost, n1, n2 = bridge_list[i]
    if find(n1) != find(n2):
        union(n1, n2)
        result += cost


for i in range(2, nn):
    if i == 2:
        k = find(i)
    else:
        if find(i) != k:
            print(-1)
            break
else:
    print(result)


