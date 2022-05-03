import math


def distance(x1, y1, x2, y2):
    result = math.sqrt( math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return result


def combination(k, r, x, y, l):
    if k == N:
        if l != r:
            return
        global answer
        new_answer = distance(x, y, 0, 0)
        answer = min(answer, new_answer)
        return
    if l < r:
        combination(k+1, r, x + points[k][0], y + points[k][1], l+1)
        combination(k+1, r, x - points[k][0], y - points[k][1], l)
    else:
        combination(k+1, r, x - points[k][0], y - points[k][1], l)



T = int(input())
for _ in range(T):
    N = int(input())
    points = []
    answer = float('inf')
    for _ in range(N):
        points.append(list(map(int,input().split())))
    
    combination(0, N//2, 0, 0, 0)
    print(answer)
