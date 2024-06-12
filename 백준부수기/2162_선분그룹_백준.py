def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)

    # 선분이 일직선상에 있을 때, 범위가 겹치는지 확인
    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return True
        return False
    
    return ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0

def find_root(i):
    if parents_line[i] == i:
        return i
    
    parents_line[i] = find_root(parents_line[i])
    return parents_line[i]

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

        # 두 선분이 만나면 parents 변경
        if is_intersect(ix1, iy1, ix2, iy2, jx1, jy1, jx2, jy2):
            root_i = find_root(i)
            root_j = find_root(j)
            if root_i != root_j:
                parents_line[root_j] = root_i

# 부모 갱신
for i in range(n):
    parents_line[i] = find_root(i)

max_count = 0
group_count = {}

for i in range(n):
    root = parents_line[i]
    if root not in group_count:
        group_count[root] = 1
    else:
        group_count[root] += 1
    
    max_count = max(max_count, group_count[root])

print(len(group_count))
print(max_count)
