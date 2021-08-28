import collections


def calculate(leng_r):
    result = []
    max_leng = 0
    for row in range(leng_r):
        numbers = collections.Counter(array[row])
        del numbers[0]
        numbers = list(numbers.items())
        numbers.sort(key = lambda x: (x[1],x[0]))
        if len(numbers) > 50: numbers = numbers[:50]
        line = []
        for i in range(len(numbers)):
            j, k = numbers[i]
            line += [j,k]
        max_leng = max(max_leng, len(numbers))
        result.append(line)

    for row in range(leng_r):
        if len(result[row]) < 2*max_leng:
            zero_count = 2*max_leng-len(result[row])
            for _ in range(zero_count):
                result[row].append(0)
    
    return result

r, c, k = map(int,input().split())
r -= 1
c -= 1
array = [list(map(int,input().split())) for _ in range(3)]
time = 0
while time <= 100:
    leng_r = len(array)
    leng_c = len(array[0])
    if r < leng_r and c < leng_c:
        if array[r][c] == k:
            break
    if leng_r >= leng_c:
        array = calculate(leng_r)
    else:
        array = list(map(list, zip(*array)))
        array = calculate(leng_c)
        array = list(map(list, zip(*array)))
    time += 1

if time == 100:
    time = -1
print(time)