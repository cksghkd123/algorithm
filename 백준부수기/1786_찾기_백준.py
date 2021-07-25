def make_table(keyword):
    pattern = [0]*len(keyword)

    i = 1
    j = 0

    while i < len(keyword):
        if keyword[i] == keyword[j]:
            j += 1
            pattern[i] = j
            i += 1

        else:
            if j != 0:
                j = pattern[j-1]
            
            else:
                pattern[i] = 0
                i += 1

    return pattern


def kmp(reference, keyword, pattern):
    ri = 0
    ki = 0
    index_list = []

    while ri < len(reference):
        if reference[ri] != keyword[ki]:
            if ki == 0:
                ri += 1
            else:
                ri += ki - pattern[ki - 1]
                ki = pattern[ki - 1]
        
        else:
            ki += 1
            ri += 1
            if ki == len(keyword):
                index_list.append(ri - len(keyword) + 1)
                ki = pattern[ki - 1]
    
    return index_list


t = input()
p = input()

pi = make_table(p)

where = kmp(t, p, pi)

print(len(where))
# asterisk 1개 >> unpack list 공백으로 구분해서 띄어서 출력
print(*where) 
