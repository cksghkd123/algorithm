import collections


def permutation(list, r, result):
    if len(result) == r:
        order.append(result + [end])
        return

    for i in range(len(list)):
        if visited[i] == False:
            visited[i] = True
            permutation(list, r, result + [list[i]])
            visited[i] = False


def search(start, things):
    result = 0
    here = start
    for t in things:
        result += bfs(here, t)
        here = t
    
    return result

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def bfs(start, end):
    visited = [[False]*n for _ in range(m)]
    deq = collections.deque()
    deq.append([0] + start)
    visited[start[0]][start[1]] = True

    while deq:
        count, row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < m and 0 <= nc < n:
                if visited[nr][nc] == False and house_map[nr][nc] != '#':
                    if [nr, nc] == end:
                        return count+1
                    else:
                        visited[nr][nc] = True
                        deq.append((count+1, nr, nc))

n, m = map(int,input().split())
house_map = []
things_index = []
for row in range(m):
    house_map.append(list(input()))
    for col in range(n):
        if house_map[row][col] == 'X':
            things_index.append([row,col])
        elif house_map[row][col] == 'S':
            start = [row, col]
        elif house_map[row][col] == 'E':
            end = [row, col]

answer = float('inf')
order = []
visited = [False]*(len(things_index))
permutation(things_index, len(things_index) , [])


for oo in order:
    result = search(start, oo)
    answer = min(answer, result)

print(answer)