def combination(part, dist_range, r, target, result:set):
    global button
    if button == True:
        return

    if len(result) == target:
        button = True
        return
    
    if r == len(part):
        return
    
    for ranran in dist_range[part[r]]:
        combination(part, dist_range, r+1, target, result.union(ranran))

button = False
def solution(n, weak, dist):
    global button
    dist.sort(reverse=True)
    
    dist_range = {i:[] for i in dist}
    

    for ii in range(1, len(dist)+1, 1):
        part = dist[:ii]
        j = part[-1]
        for i in weak:
            temp = set()
            for w in weak:
                if i <= w <= i+j or i <= w+n <= i+j:
                    temp.add(w)
            if temp and temp not in dist_range[j]:
                dist_range[j].append(temp)

        combination(part, dist_range, 0, len(weak), set())
        if button == True:
            answer = ii
            break
    if button == False:
        answer = -1
    
    return answer
        
    
        


print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))