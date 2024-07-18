def union(x, y):
    fx = find(x)
    fy = find(y)

    if fx != fy:
        parents[fx] = fy

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    
    return parents[x]


N = int(input())

planet_list = []
parents = [i for i in range(N)]
x_list = []
y_list = []
z_list = []

for i in range(N):
    x, y, z = map(int, input().split())
    planet_list.append((x, y, z))

    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

x_list.sort()
y_list.sort()
z_list.sort()

answer = 0
count = 0

total_list = []

for i in range(N-1):
    total_list.append((x_list[i+1][0]-x_list[i][0], x_list[i][1], x_list[i+1][1]))
    total_list.append((y_list[i+1][0]-y_list[i][0], y_list[i][1], y_list[i+1][1]))
    total_list.append((z_list[i+1][0]-z_list[i][0], z_list[i][1], z_list[i+1][1]))

total_list.sort()


for distance, a, b in total_list:

    if find(a) != find(b):
        union(a, b)
        answer += distance
        count += 1

    if count == N-1:
        break
    

print(answer)