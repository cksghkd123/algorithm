while True:
    s = input()
    if s == 'end':
        break

    answer = 'invalid'

    count_X = 0
    count_O = 0

    for c in s:
        if c == 'X':
            count_X += 1
        elif c == 'O':
            count_O += 1
    

    ttt_count_X = 0
    ttt_count_O = 0

    # 가로
    for i in range(3):
        if s[i*3] == s[i*3+1] == s[i*3+2]:
            if s[i*3] == 'X':
                ttt_count_X += 1
            elif s[i*3] == 'O':
                ttt_count_O += 1
    
    # 세로
    for i in range(3):
        if s[i] == s[i+3] == s[i+6]:
            if s[i] == 'X':
                ttt_count_X += 1
            elif s[i] == 'O':
                ttt_count_O += 1

    # 대각선
    if s[0] == s[4] == s[8]:
        if s[0] == 'X':
            ttt_count_X += 1
        elif s[0] == 'O':
            ttt_count_O += 1

    if s[2] == s[4] == s[6]:
        if s[2] == 'X':
            ttt_count_X += 1
        elif s[2] == 'O':
            ttt_count_O += 1

    if count_X + count_O < 9:
        if count_X - count_O == 1:
            if ttt_count_X > 0 and ttt_count_O == 0:
                answer = 'valid'
        
        elif count_X - count_O == 0:
            if ttt_count_X == 0 and ttt_count_O > 0:
                answer = 'valid'
    else:
        if count_X - count_O == 1 and ttt_count_X >= 0 and ttt_count_O == 0:
            answer = 'valid'

    print(answer)