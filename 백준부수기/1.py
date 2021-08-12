import collections


dr = [0, 0, 1, -1]
dc = [1, -1, 0 ,0]
def solution(board, r, c):
    card_left = [True for _ in range(7)]
    clear_condition = 0
    for row in range(4):
        for col in range(4):
            if board[row][col] != 0 and card_left[board[row][col]] == True:
                card_left[board[row][col]] == False
                clear_condition += 1

    deq = collections.deque()
    deq.append((r, c, card_left, 0, False, 0))

    while deq:
        row, col, card_left, count, matching, clear_count = deq.popleft()
        if matching == False:
            if card_left[board[row][col]] == False:
                for w in range(4):
                    nr = row + dr[w]
                    nc = col + dc[w]
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        deq.append((nr, nc, card_left, count+1, matching, clear_count))
                        if board[nr][nc] == 0:
                            while board[nr][nc] == 0:
                                nr = row + dr[w]
                                nc = col + dc[w]
                            deq.append((nr, nc, card_left, count+1, matching, clear_count))
                
                deq.append((row, col, card_left, count+1, board[row][col], clear_count))
            
            else:
                for w in range(4):
                    nr = row + dr[w]
                    nc = col + dc[w]
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        deq.append((nr, nc, card_left, count+1, matching, clear_count))
                        if board[nr][nc] == 0:
                            while board[nr][nc] == 0:
                                nr = row + dr[w]
                                nc = col + dc[w]
                            deq.append((nr, nc, card_left, count+1, board[row][col], clear_count))

        else:
            if board[row][col] != matching:
                for w in range(4):
                    nr = row + dr[w]
                    nc = col + dc[w]
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        deq.append((nr, nc, card_left, count+1))
                        if board[nr][nc] == 0:
                            while board[nr][nc] == 0:
                                nr = row + dr[w]
                                nc = col + dc[w]
                            deq.append((nr, nc, card_left, count+1))
                
                deq.append((row, col, card_left, count+1, board[row][col]))
            
            else:
                card_left[board[row][col]] = True
                deq.append((row, col ,card_left, count+1, False, clear_count+1))
                if clear_count+1 == clear_condition:
                    return clear_count+1

a = [
    [1,0,0,3],
    [2,0,0,0],
    [0,0,0,2],
    [3,0,1,0]]
b = 1
c = 0
print(solution(a,b,c))