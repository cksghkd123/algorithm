def table(keyword):
    i = 1
    j = 0
    pattern = [0]*len(keyword)

    while i < len(keyword):
        if keyword[i] != keyword[j]:
            if j != 0:
                j = pattern[j-1]
            else:
                pattern[i] = 0
                i += 1
        
        else:
            j += 1
            pattern[i] = j
            i += 1

    return pattern


for _ in range(10):
    taken_keyword = input()
    if taken_keyword == '.':
        break
    pi = table(taken_keyword)
    temp = len(taken_keyword) - pi[-1]
    print(pi)

    if len(taken_keyword) % temp == 0:
        print(len(taken_keyword) // temp)
    else:
        print(1)