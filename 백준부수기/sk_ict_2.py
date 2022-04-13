from pprint import pprint

def solution(n, clockwise):
    if clockwise:
        dr = (0, 1, 0, -1)
        dc = (1, 0, -1, 0)
        spots = [[0,0], [0,n-1], [n-1,n-1], [n-1,0]]
    else:
        dr = (1, 0, -1, 0)
        dc = (0, 1, 0, -1)
        spots = [[0,0], [n-1,0], [n-1,n-1], [0,n-1]]


    for i in range(4):
        spots[i][0] -= dr[i]
        spots[i][1] -= dc[i]

    number = 1
    answer = [[0 for _ in range(n)] for _ in range(n)]

    length = n-1
    index = 0
    for _ in range(n-3):
        for _ in range(length):
            for i in range(4):
                spots[i][0] += dr[index]
                spots[i][1] += dc[index]
                answer[spots[i][0]][spots[i][1]] = number
                index += 1
                index %= 4 
            number += 1
        index += 1
        index %= 4
        length -= 2
    
    if n%2:
        answer[n//2][n//2] = number

    return answer

solution(5, True)
solution(6, False)
solution(9, True)