from pprint import pprint

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
def dragon_curve(col, row, direction, generation):
    que = []
    que.append(direction)
    visited[row][col] = 1
    row = row + dr[direction]
    col = col + dc[direction]
    visited[row][col] = 1
    for _ in range(generation):
        for d in reversed(que):
            nd = (d+1)%4
            row = row + dr[nd]
            col = col + dc[nd]
            visited[row][col] = 1
            que.append(nd)

#점 사이의 변을 좌표를 visited로 찍음

visited = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
for _ in range(n):
    c, r, d, g = map(int,input().split())
    dragon_curve(c,r,d,g)

answer = 0
for row in range(1,101):
    for col in range(100):
        nr = row
        nc = col
        for w in range(4):
            nr = nr + dr[w]
            nc = nc + dc[w]
            if visited[nr][nc] == 0:
                break
        else:
            answer += 1

print(answer)