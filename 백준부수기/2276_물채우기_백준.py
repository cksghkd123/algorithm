dr = [0 ,0, 1, -1]
dc = [1, -1, 0, 0]
def pouring(row, col):

    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]
        
        

m, n = map(int,input().split())
bottle = [list(map(int,input().split())) for _ in range(m)]
water = [[0]*m for _ in range(n)]

# result = 0
# for row in range(1,m-1):
#     for col in range(1,n-1):
#         if visited[row][col] == False:
#             result += pouring(row, col)
for i in range(m):
    print(bottle[i])
