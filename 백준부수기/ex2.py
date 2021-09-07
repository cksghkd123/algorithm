def candidate_key(relation, candidate):
    target = len(relation)
    temp = []
    for i in range(target):
        temp.append(tuple(map(lambda n:relation[i][n], candidate)))
    temp = set(temp)

    if len(temp) == target:
        global answer
        answer += 1
        global button
        button = True

def combination(relation, temp, k, target, result, buttons):
    if len(result) == target:
        candidate_key(relation, result)
        return

    if k == len(temp):
        return
    
    if buttons[temp[k]] == True:
        combination(relation, temp, k+1, target, result, buttons)
    else:
        combination(relation, temp, k+1, target, result + [temp[k]], buttons)
        combination(relation, temp, k+1, target, result, buttons)

answer = 0
button = False
def solution(relation):
    global button
    index_info = [i for i in range(len(relation[0]))]

    buttons = [False for _ in range(len(relation[0]))]

    for r in range(1,len(index_info)+1):
        for i in range(len(index_info)):
            button = False
            if buttons[i] == True:
                continue
            temp = index_info[i:]
            combination(relation, temp, 1, r, [temp[0]], buttons)
            if button == True:
                buttons[i] = True
            print(r, i, buttons)

    return answer





print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))