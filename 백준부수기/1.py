def solution(board, r, c):
    not_clear = [True for _ in range(7)]
    for row in range(4):
        for col in range(4):
            if board[row][col] != 0 and not_clear[board[row][col]] == True:
                not_clear[board[row][col]] = False
    
    print(not_clear)
    
    answer = 0
    return answer



a = [
    [1,0,0,3],
    [2,0,0,0],
    [0,0,0,2],
    [3,0,1,0]]
b = 1
c = 0
print(solution(a,b,c))