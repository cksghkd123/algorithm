def combination(left_arrow, index, info, result):
    global max_score
    global win_list

    if index == len(info):
        score = 0

        for i in range(11):
            if i in result:
                score += (10-i)
            elif info[i] != 0:
                score -= (10-i)
        if score > 0:
            print(score)
        if max_score > score:
            return
        else:
            max_score = score
            win_list = result
            return
    
    if left_arrow == 0:
        score = 0
        for i in range(11):
            if i in result:
                score += (10-i)
            elif info[i] != 0:
                score -= (10-i)
        if score >0:
            print(score)
        if max_score > score:
            return
        else:
            max_score = score
            win_list = result
            return
    
    if info[index] < left_arrow:
        combination(left_arrow - info[index]-1, index+1, info, result+[index])
        combination(left_arrow, index+1, info, result)
    else:
        combination(left_arrow, index+1, info, result)

max_score = 0
win_list = []

def solution(n, info):
    combination(n, 0, info, [])

    if max_score <= 0:
        return [-1]

    answer = [0 for _ in range(11)]
    left_arrow = n

    for index in win_list:
        answer[index] += info[index]+1
        left_arrow -= (info[index] + 1)
        print(left_arrow)

    if left_arrow > 0:
        answer[10] += left_arrow
        
    print(max_score)
    print(win_list)
    return answer

print(solution(2,[1,0,0,0,0,0,0,0,0,0,0]))