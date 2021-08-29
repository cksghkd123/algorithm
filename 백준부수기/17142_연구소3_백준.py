import collections


def combination(r,k,result):
    if len(result) == r:
        global answer
        answer = min(answer,bfs(result))
        return

    if k == len(virus_list):
        return

    combination(r, k+1, result + [virus_list[k]])
    combination(r, k+1, result)


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def bfs(activate_list):
    visited = [[False for _ in range(n)] for _ in range(n)]
    deq = collections.deque()
    mx_count = 0

    for i in activate_list:
        deq.append((*i,0))
        visited[i[0]][i[1]] = True
    while deq:
        row, col, count = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < n:
                if map_list[nr][nc] == 0 and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    deq.append((nr,nc,count+1))
                    mx_count = count+1
                elif map_list[nr][nc] == 2 and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    deq.append((nr,nc,count+1))

    for row in range(n):
        for col in range(n):
            if map_list[row][col] == 1:
                continue
            if visited[row][col] == False:
                return float('inf')

    return mx_count

    
n, m = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(n)]
virus_list = []
for row in range(n):
    for col in range(n):
        if map_list[row][col] == 2:
            virus_list.append((row,col))
answer = float('inf')
combination(m,0,[])
if answer == float('inf'):
    answer = -1
print(answer)