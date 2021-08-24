from pprint import pprint
## 기존 드래곤커브 문제에 꼭지점이아닌 이어진 변으로 사각형을 이룬 것들의 수를 계산한다고 가정
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
def dragon_curve(col, row, direction, generation):
    que = []
    que.append(direction)
    visited[row+dr[direction]][col+dc[direction]] = 1
    row = row + 2*dr[direction]
    col = col + 2*dc[direction]
    for _ in range(generation):
        for d in reversed(que):
            nd = (d+1)%4
            visited[row+dr[nd]][col+dc[nd]] = 1
            row = row + 2*dr[nd]
            col = col + 2*dc[nd]
            que.append(nd)

#점 사이의 변을 좌표를 visited로 찍음

visited = [[0 for _ in range(11)] for _ in range(11)]
n = int(input())
for _ in range(n):
    c, r, d, g = map(int,input().split())
    dragon_curve(2*c,2*r,d,g)
pprint(visited)
answer = 0
for row in range(1, 201, 2):
    for col in range(1, 201, 2):
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if visited[nr][nc] == False:
                break
        else:
            print(row,col)
            answer += 1

print(answer)

# [[&, 0, &, 0, &, 0, &, 0, &, 0, &],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [&, 0, &, 0, &, 0, &, 1, &, 0, &],
#  [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#  [&, 0, &, 0, &, 1, &, 1, &, 0, &],
#  [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
#  [&, 0, &, 0, &, 1, &, 1, &, 0, &],
#  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#  [&, 0, &, 0, &, 1, &, 0, &, 0, &],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [&, 0, &, 0, &, 0, &, 0, &, 0, &]]