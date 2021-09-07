import collections

dr = [2, -2, 0, 0]
dc = [0, 0, 2, -2]
ddr = [1, -1, 1, -1]
ddc = [-1, -1, 1, 1]
def solution(board):
    n = 2*len(board)-1
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][1] = True
    deq = collections.deque()
    deq.append((0,1,0))
    while deq:
        row, col, count = deq.popleft()

        #도착했는지
        if row == n-1 and col == n-2:
            return count
        if row == n-2 and col == n-1:
            return count

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < n:
                if row%2 == 0:
                    if visited[nr][nc] == False and board[nr//2][(nc+1)//2] == 0 and board[nr//2][(nc-1)//2] == 0:
                        visited[nr][nc] = True
                        deq.append((nr, nc, count+1))
                elif col%2 == 0:
                    if visited[nr][nc] == False and board[(nr+1)//2][nc//2] == 0 and board[(nr-1)//2][nc//2] == 0:
                        visited[nr][nc] = True
                        deq.append((nr, nc, count+1))
        
        for w in range(4):
            nr = row + ddr[w]
            nc = col + ddc[w]
            if 0 <= nr < n and 0 <= nc < n:
                if row%2 == 0:
                    if visited[nr][nc] == False and board[(nr+ddr[w])//2][nc//2] == 0 and board[(nr+ddr[w])//2][(col-ddc[w])//2] == 0:
                        visited[nr][nc] = True
                        deq.append((nr, nc, count+1))
                if col%2 == 0:
                    if visited[nr][nc] == False and board[nr//2][(nc+ddc[w])//2] == 0 and board[(row-ddr[w])//2][(nc+ddc[w])//2] == 0:
                        visited[nr][nc] = True
                        deq.append((nr, nc, count+1))
    


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))