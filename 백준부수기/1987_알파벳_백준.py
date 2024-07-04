R, C = map(int, input().split())

board_list = [list(input()) for _ in range(R)]
visited = set()
answer = 0

def dfs(cr, cc, count):
    global answer
    answer = max(answer, count)
    visited.add(board_list[cr][cc])


    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr = cr + dr
        nc = cc + dc

        if 0 <= nr < R and 0 <= nc < C and board_list[nr][nc] not in visited:
            dfs(nr, nc, count+1)
    
    visited.remove(board_list[cr][cc])

dfs(0, 0, 1)

print(answer)