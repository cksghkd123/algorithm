def solution(v):
    line_index = [(0,1,2), (0,2,1), (1,2,0)]
    line = []
    for n1, n2, n3 in line_index:
        if v[n1][0] - v[n2][0] == 0:
            if v[n3][1] == v[n2][1]:
                return [v[n3][0], v[n3][1] + (v[n1][1] - v[n2][1])]
            else:
                return [v[n3][0], v[n3][1] - (v[n1][1] - v[n2][1])]



print(solution([[1, 1], [2, 2], [1, 2]]))