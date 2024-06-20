def find_zero(target, input_list):
    n = len(input_list)
    left = 0
    right = n-1
    answer = [0, 0]
    result = float('inf')

    while left < right:
        dif = abs(input_list[right] + input_list[left] + target)
        if dif < result:
            answer = [input_list[left], input_list[right]]
            result = dif
        
        if input_list[left] + input_list[right] + target < 0:
            left += 1
        else:
            right -= 1
        

        
    return result, *answer
            

n = int(input())

liquid_list = list(map(int, input().split()))

liquid_list.sort()

min_result = float('inf')
answer = [0, 0, 0]
for i in range(n):
    result, a, b = find_zero(liquid_list[i], liquid_list[:i]+liquid_list[i+1:])
    if min_result > result:
        min_result = result
        answer = sorted([liquid_list[i], a, b])

print(*answer)



