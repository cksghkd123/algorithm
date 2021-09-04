def solution(s):
    answer = len(s)

    for i in range(1,len(s)//2+1):
        result = 0
        pivot = s[0:i]
        count = 1
        for j in range(i, len(s), len(pivot)):
            print(j,pivot)
            print(result)
            if j+i <= len(s):
                if s[j:j+i] == pivot:
                    count += 1
                else:
                    if count == 1:
                        result += len(pivot)
                    else:
                        result += len(pivot) + 1
                    pivot = s[j:j+i]
                    count = 1
            else:
                if count == 1:
                    result += len(pivot)
                else:
                    result += len(pivot) + 1
                pivot = s[j:j+i]
                count = 1
        if count == 1:
            result += len(pivot)
        else:
            result += len(pivot) + 1
        print(result)
        answer = min(answer, result)
        
    return answer

print(solution("abcabcdede"))