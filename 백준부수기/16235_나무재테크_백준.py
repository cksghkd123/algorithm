import collections

dr = [1, 1, 1, -1, -1, -1, 0, 0]
dc = [-1, 0, 1, -1, 0, 1, 1, -1]

n, m, k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
trees = [[collections.deque() for _ in range(n)] for _ in range(n)]

b = []
for _ in range(m):
    x, y, z = map(int,input().split())
    b.append((z, x-1, y-1))
b.sort()

for age, row, col in b:
    trees[row][col].append(age)

nutrients = [[5 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    dead_list = list()
    breeding_list = list()
    for row in range(n):
        for col in range(n):
            rrr = len(trees[row][col])
            for _ in range(rrr):
                age = trees[row][col].popleft()
                if age <= nutrients[row][col]:
                    nutrients[row][col] -= age
                    age += 1
                    if age % 5 == 0:
                        breeding_list.append((row, col))
                    trees[row][col].append(age)
                else:
                    dead_list.append((age, row, col))

    for age, row, col in dead_list:
        nutrients[row][col] += age//2

    for row, col in breeding_list:
        for w in range(8):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < n:
                trees[nr][nc].appendleft(1)

    for row in range(n):
        for col in range(n):
            nutrients[row][col] += a[row][col]

answer = 0
for row in range(n):
    for col in range(n):
        answer += len(trees[row][col])
print(answer)
