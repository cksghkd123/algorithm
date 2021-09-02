import collections


def bfs(row, col):
    deq = collections.deque()
    deq.append((row, col))
    count = 1
    
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < 2**n and 0 <= nc < 2**n:
                if visited[nr][nc] == False and map_list[nr][nc][button] != 0:
                    visited[nr][nc] = True
                    deq.append((nr, nc))
                    count += 1
    
    return count

n, q = map(int,input().split())
map_list = [list(map(lambda x: [int(x), 0],input().split())) for _ in range(2**n)]
steps = list(map(int,input().split()))
button = 0
new_button = 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for step in steps:
    for i in range(0, 2**n, 2**step):
        for j in range(0, 2**n, 2**step):
            row = i
            col = j
            if step == 0:
                map_list[row][col][new_button] = map_list[row][col][button]
                continue
            for k in range(2**(step-1)):
                for w in range(4):
                    for t in range(2**step-1-(2*k)):
                        map_list[row+dr[w]*(2**step-1-(2*k))+t*dr[(w+1)%4]][col+dc[w]*(2**step-1-(2*k))+t*dc[(w+1)%4]][new_button] = map_list[row+t*dr[w]][col+t*dc[w]][button]
                    row += dr[w]*(2**step-1-(2*k))
                    col += dc[w]*(2**step-1-(2*k))
                row += 1
                col += 1
    
    button, new_button = new_button, button
    for row in range(2**n):
        for col in range(2**n):
            if map_list[row][col][button] == 0:
                map_list[row][col][new_button] = map_list[row][col][button]
                continue
            count = 0
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]
                if 0 <= nr < 2**n and 0 <= nc < 2**n:
                    if map_list[nr][nc][button] != 0:
                        count += 1
            if count < 3:
                map_list[row][col][new_button] = map_list[row][col][button] - 1
            else:
                map_list[row][col][new_button] = map_list[row][col][button]

    button, new_button = new_button, button

answer1 = 0
answer2 = 0
visited = [[False for _ in range(2**n)] for _ in range(2**n)]
for row in range(2**n):
    for col in range(2**n):
        answer1 += map_list[row][col][button]
        if map_list[row][col][button] != 0 and visited[row][col] == False:
            visited[row][col] = True
            result = bfs(row, col)
            answer2 = max(answer2, result)

print(answer1)
print(answer2)
