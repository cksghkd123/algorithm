def solution1(s, n, C):
    result = 0
    trigger = False
    for i in range(n-1, -1, -1):
        if s[i] != C:
            trigger = True
        
        if trigger == False:
            continue

        if s[i] == C:
            result += 1
    
    
    return result

def solution2(s, n, C):
    result = 0
    trigger = False
    for i in range(n):
        if s[i] != C:
            trigger = True
        
        if trigger == False:
            continue

        if s[i] == C:
            result += 1
    
    
    return result

N = int(input())

S = input()


answer = min(solution1(S, N, 'R'), solution2(S, N, 'R'), solution1(S, N, 'B'), solution2(S, N, 'B'))

print(answer)