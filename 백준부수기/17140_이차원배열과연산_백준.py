import collections


def row_calculate(leng_r, leng_c):
    result = [[] for _ in range(leng_r)]
    max_leng = 0
    for row in range(leng_r):
        count_dict = collections.defaultdict(int)
        for col in range(leng_c):
            if 1 <= array[row][col] <= 100:
                count_dict[array[row][col]] += 1
        count_list = [[v, k] for k, v in count_dict.items()]
        count_list.sort()
        max_leng = max(max_leng, len(count_list))
        for i in count_list:
            if len(result) > 100:
                continue
            j, k = i
            result[row].append(k)
            result[row].append(j)
    
    for row in range(leng_r):
        if len(result[row]) < 2*max_leng:
            zero_count = 2*max_leng-len(result[row])
            for _ in range(zero_count):
                result[row].append(0)
    
    return result

def col_calculate(leng_r,leng_c):
    result = [[] for _ in range(leng_c)]
    max_leng = 0
    for col in range(leng_c):
        count_dict = collections.defaultdict(int)
        for row in range(leng_r):
            if 1 <= array[row][col] < 100:
                count_dict[array[row][col]] += 1
        count_list = [[v, k] for k, v in count_dict.items()]
        count_list.sort()
        max_leng = max(max_leng, len(count_list))
        for i in count_list:
            if len(result) > 100:
                continue
            j, k = i
            result[col].append(k)
            result[col].append(j)

    for col in range(leng_c):
        if len(result[col]) < 2*max_leng:
            zero_count = 2*max_leng-len(result[col])
            for _ in range(zero_count):
                result[col].append(0)

    result2 = [[] for _ in range(2*max_leng)]
    for row in range(leng_c):
        for col in range(2*max_leng):
            result2[col].append(result[row][col])
    
    return result2


r, c, k = map(int,input().split())
r -= 1
c -= 1
array = [list(map(int,input().split())) for _ in range(3)]
time = 0
while True:
    leng_r = len(array)
    leng_c = len(array[0])
    if r < leng_r and c < leng_c:
        if array[r][c] == k:
            break
    if leng_r >= leng_c:
        array = row_calculate(leng_r, leng_c)
    else:
        array = col_calculate(leng_r, leng_c)
    time += 1

if time == 100:
    time = -1
print(time)