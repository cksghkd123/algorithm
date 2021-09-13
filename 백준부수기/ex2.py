def solution(board, skill):
    answer = 0
    temp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board))]

    for i in range(len(skill)):
        t, r1, c1, r2, c2, degree = skill[i]

        if t == 1:
            degree = -degree

        for r in range(r1, r2+1):
            temp[r][c1] += degree
        for r in range(r1, r2+1):
            temp[r][c2+1] += (-degree)
    
    answer = 0

    for row in range(len(board)):
        weigh = 0
        for col in range(len(board[0])):
            weigh += temp[row][col]
            if board[row][col] + weigh > 0:
                answer += 1
        
    return answer



print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))