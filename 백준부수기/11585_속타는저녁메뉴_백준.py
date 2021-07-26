def table_kmp(keyword):
    i = 1
    j = 0
    pattern = [0] * len(keyword)

    while i < len(keyword):
        if keyword[i] != keyword[j]:
            if j == 0:
                pattern[i] = j
                i += 1
            else:
                j = pattern[j-1]

        else:
            j += 1
            pattern[i] = j
            i += 1

    return pattern
    
def kmp(reference, keyword, pattern):
    ri = 0 
    ki = 0
    count = 0

    while ri < len(reference):
        if reference[ri] != keyword[ki]:
            if ki == 0:
                ri += 1
            else:
                ki = pattern[ki-1]

        else:
            ri += 1
            ki += 1
            if ki == len(keyword):
                count += 1
                ki = keyword[ki-1]

    return count

def reduced_fraction(numerator, denominator):
    a = factorization(numerator)
    b = factorization(denominator)
    result = [1, 1]

    i = 0
    while i < len(a):
        if a[i] in b:
            a.pop(i)
            b.pop(b.index(a[i]))

        i += 1
    
    for j in a:
        result[0] *= j
    
    for j in b:
        result[1] *= j
    
    return '{}/{}'.format(result[0],result[1])

def factorization(num):
    result = list()
    i = 2
    while i <= num:

        if num%i == 0:
            print(num, i)
            result.append(i)
            num = num//i
            continue

        i += 1

    return result
    
n = int(input())
meat = ''.join(input().split())
roulette = input().split()*2
roulette.pop()
roulette = ''.join(roulette)


pi = table_kmp(meat)
count = kmp(roulette, meat, pi)
result = reduced_fraction(count, n)
print(result)