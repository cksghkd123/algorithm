from pprint import pprint

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def tetromino(row, col, count, score):
    result = 0
    if count == 4:
        return score

    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]
        if 0 <= nr < n and 0 <= nc < m:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                result = max(result, tetromino(nr,nc,count+1,score+map_list[nr][nc]))
                visited[nr][nc] = 0
    
    return result
    
def temp(row, col):
    result = 0
    for i in range(4):
        score = map_list[row][col]
        for w in range(4):
            if w == i:
                continue
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < m:
                score += map_list[nr][nc]
            else:
                break
        else:
            result = max(result, score)


    return result

n, m = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
total = 0
for row in range(n):
    for col in range(m):
        if visited[row][col] == 0:
            visited[row][col] = -1
            total = max(total, tetromino(row, col, 1, map_list[row][col]), temp(row, col))
            visited[row][col] = 0

print(total)