import collections

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def make_united(row, col, left, right):
    visited[row][col] = True
    total = world_list[row][col]
    nations = [(row, col)]
    deq = collections.deque()
    deq.append((row, col))

    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < n:
                population_difference = abs(world_list[row][col] - world_list[nr][nc])
                if left <= population_difference <= right and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    deq.append((nr, nc))
                    total += world_list[nr][nc]
                    nations.append((nr, nc))
    
    p = total//len(nations)
    for row, col in nations:
        world_list[row][col] = p 
    
    if len(nations) > 1:
        return True
    else:
        return False
                


n, l, r = map(int,input().split())
world_list = [list(map(int,input().split())) for _ in range(n)]

finish_button = True
count = -1
while finish_button:
    finish_button = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if visited[row][col] == False:
                f = make_united(row, col, l, r)
                if finish_button == False:
                    finish_button = f
    count += 1

print(count)
