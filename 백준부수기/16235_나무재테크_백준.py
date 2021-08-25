import collections


def spring():
    dead_list = []
    breeding_list = []
    for row, col in trees:
        for q in range(len(trees[(row,col)])-1, -1, -1):
            if trees[(row, col)][q] <= nutrients[row][col]:
                nutrients[row][col] -= trees[(row,col)][q]
                trees[(row,col)][q] +=1
                if trees[(row,col)][q]%5 == 0:
                    breeding_list.append((row, col))
            else:
                dead_list.append((row, col, trees[(row,col)][q]))
    return dead_list, breeding_list

def summer(list):
    for row, col, x in list:
        nutrients[row][col] += x//2
        trees[(row,col)].remove(x)

dr = [1, 1, 1, -1, -1, -1, 0, 0]
dc = [-1, 0, 1, -1, 0, 1, 1, -1]
def authumn(list):
    for row, col in list:
        for w in range(8):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < n:
                trees[(nr,nc)].append(1)

def winter():
    for row in range(n):
        for col in range(n):
            nutrients[row][col] += a[row][col]

def count():
    result = 0
    for i in trees:
        result += len(trees[i])
    return result


n, m, k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
trees = collections.defaultdict(list)

for _ in range(m):
    x, y, z = map(int,input().split())
    trees[(x-1,y-1)].append(z)
for i in trees:
    trees[i].sort()
    trees[i].reverse()
nutrients = [[5 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    d_list, b_list = spring()
    summer(d_list)
    authumn(b_list)
    winter()
answer = count()
print(answer)
