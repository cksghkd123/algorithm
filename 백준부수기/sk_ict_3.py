from math import comb

def solution(width, height, diagonals):
    answer = 0
    for x, y in diagonals:
        route1 = comb(x+y-1,x) * comb(width-(x-1)+height-(y), width-(x-1))
        route2 = comb(x-1+y,y) * comb(width-(x)+height-(y-1), width-(x))
        answer += route1 + route2


    return answer

print(solution(4,5,[[1,1],[2,4]]))