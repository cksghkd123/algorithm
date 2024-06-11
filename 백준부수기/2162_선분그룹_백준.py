n = int(input())

parents_line = [i for i in range(n)]
lines = []

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append((x1, y1, x2, y2))

for i in range(n):
    for j in range(i):
        ix1, iy1, ix2, iy2 = lines[i]
        jx1, jy1, jx2, jy2 = lines[j]

                
    
