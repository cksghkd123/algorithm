n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int,input().split())))
visited = [[0]*i for i in range(1,n+1)]

visited[0][0] = triangle[0][0]

for row in range(n-1):
    for col in range(len(triangle[row])):
        n_row = row+1
        for i in range(2):
            new_amount = visited[row][col]+triangle[n_row][col+i]
            if new_amount > visited[n_row][col+i]:
                visited[n_row][col+i] = new_amount

print(max(visited[n-1]))
