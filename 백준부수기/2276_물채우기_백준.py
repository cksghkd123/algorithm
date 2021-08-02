def find(row, col):
    if root[row][col] = (row, col)


dr = [0 ,0, 1, -1]
dc = [1, -1, 0, 0]
def pouring(row, col):
    temp = 0
    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]
        if 0 <= nr < m and 0 <= nc < n:
            if bottle[row][col] > bottle[nr][nc]:
                

        else:
            
        
        

m, n = map(int,input().split())
bottle = [list(map(int,input().split())) for _ in range(m)]
water = [[0 for i in range(n)] for _ in range(m)]

result = 0
for row in range(m):
    for col in range(n):
        pouring(row, col)

