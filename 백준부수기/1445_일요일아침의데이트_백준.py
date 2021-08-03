import collections
from pprint import pprint


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def near_garbage(row, col, count):
    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]

        if 0 <= nr < n and 0 <= nc < m:
            if forest[nr][nc] == 'g':
                count += 1
    return count

def bfs(start, finish, garbage_limit):
    deq = collections.deque()
    deq.append((*start, 0, 0))
    minimum_garbage[start[0]][start[1]][0], minimum_garbage[start[0]][start[1]][1] = 0, 0
    
    while deq:
        row, col, g, near_g = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < n and 0 <= nc < m and g <= garbage_limit:
                n_near_g = near_garbage(nr, nc, near_g)
                if forest[nr][nc] == 'g':
                    if g+1 < minimum_garbage[nr][nc][0]:
                        minimum_garbage[nr][nc][0] = g+1
                        minimum_garbage[nr][nc][1] = near_g
                        deq.append((nr, nc, g+1, n_near_g))
                    elif g+1 == minimum_garbage[nr][nc][0] and near_g < minimum_garbage[nr][nc][1]:
                        minimum_garbage[nr][nc][1] = near_g
                        deq.append((nr, nc, g+1, n_near_g))

                elif forest[nr][nc] == 'F':
                    if g < minimum_garbage[nr][nc][0]:
                        minimum_garbage[nr][nc][0] = g
                        minimum_garbage[nr][nc][1] = near_g
                    elif g == minimum_garbage[nr][nc][0] and near_g < minimum_garbage[nr][nc][1]:
                        minimum_garbage[nr][nc][1] = near_g

                elif forest[nr][nc] == '.':
                    if g < minimum_garbage[nr][nc][0]:
                        minimum_garbage[nr][nc][0] = g
                        minimum_garbage[nr][nc][1] = n_near_g
                        deq.append((nr, nc, g, n_near_g))
                    elif g == minimum_garbage[nr][nc][0] and n_near_g < minimum_garbage[nr][nc][1]:
                        minimum_garbage[nr][nc][1] = n_near_g
                        deq.append((nr, nc, g, n_near_g))

        
    result = minimum_garbage[finish[0]][finish[1]]

    return result    


n, m = map(int,input().split())
forest = [list(input()) for _ in range(n)]
info = collections.defaultdict(list)
for row in range(n):
    for col in range(m):
        if forest[row][col] != '.':
            info[forest[row][col]].append((row, col))

INF = float('inf')
minimum_garbage = [[[INF, INF] for _ in range(m) ] for _ in range(n) ]
result = bfs(info['S'][0], info['F'][0], len(info['g']))

print(*result)
pprint(minimum_garbage)



