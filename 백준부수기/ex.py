def combination(part, dist_range, r, target, result:set):
    if len(result) == target:
        global button
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
    for i in range(n):
        for j in dist:
            temp = set()
            for w in weak:
                if i <= w <= i+j or i <= w+n <= i+j:
                    temp.add(w)
            if temp and temp not in dist_range[j]:
                dist_range[j].append(temp)

    for i in range(1, len(dist)+1, 1):
        part = dist[:i]
        combination(part, dist_range, 0, len(weak), set())
        if button == True:
            answer = i
            break
    if button == False:
        answer = -1
    
    return answer
        
    
        


print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))