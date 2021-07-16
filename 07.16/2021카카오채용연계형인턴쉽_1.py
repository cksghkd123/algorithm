def solution(s):
    s = list(s)
    answer = []
    i = 0
    while i < len(s):
        try:
            s[i] = int(s[i])
            answer.append(str(s[i]))
            i += 1
        except:
            if s[i] == 'z':
                answer.append('0')
                i += 4
            elif s[i] == 'o':
                answer.append('1')
                i += 3
            elif s[i] == 't':
                i += 1
                if s[i] == 'w':
                    answer.append('2')
                    i += 2
                else:
                    answer.append('3')
                    i += 4
            elif s[i] == 'f':
                i += 1
                if s[i] == 'o':
                    answer.append('4')
                    i += 3
                else:
                    answer.append('5')
                    i += 3
            elif s[i] == 's':
                i += 1
                if s[i] == 'i':
                    answer.append('6')
                    i += 2
                else:
                    answer.append('7')
                    i += 4
            elif s[i] == 'e':
                answer.append('8')
                i += 5
            elif s[i] == 'n':
                answer.append('9')
                i +=4

    answer = ''.join(answer)
    answer = int(answer)
    
    return answer