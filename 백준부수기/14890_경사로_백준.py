def slope_check(array, index, length):
    gap = array[index] - array[index+1]
    if abs(gap) > 1:
        return -1

    if gap > 0: 
        for i in range(1, length+1):
            if index+i >= n or array[index+i] != array[index+1]:
                return -1
            sloped[index+i] = True
        else:
            return length

    elif gap < 0:
        for i in range(0, length):
            if index-i < 0 or array[index-i] != array[index] or sloped[index-i] == True:
                return -1
            sloped[index-i] = True
        else:
            return 1


n, l = map(int,input().split())
path_list = [[] for _ in range(2*n)]
for i in range(n):
    path_list[i] = list(map(int,input().split()))
    for j in range(n):
        path_list[n+j].append(path_list[i][j])

result = 0   
for path in path_list:
    sloped = [False for _ in range(n)]
    step = 0
    while step < n:
        if step == n-1:
            result += 1
            break
        if path[step+1] == path[step]:
            step += 1
            continue
        else:
            next_level = slope_check(path, step, l)
            if next_level < 0:
                break
            else:
                step += next_level

print(result)
