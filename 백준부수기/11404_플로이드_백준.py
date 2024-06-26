n = int(input())
m = int(input())

INF = float('inf')
data = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a-1][b-1] = min(data[a-1][b-1], c)

for k in range(n):
    data[k][k] = 0
    for i in range(n):
        for j in range(n):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

for row in data:
    for d in row:
        if d == INF:
            print(0, end=' ')
        else:
            print(d, end=' ')
    print()
