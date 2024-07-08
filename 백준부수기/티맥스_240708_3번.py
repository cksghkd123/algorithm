def solution(foods):
    answer = 0
    
    n = len(foods)
    if n < 3:
        return 0


    accumulate_list = [0 for _ in range(n)]

    for i in range(n):
        if i == 0:
            accumulate_list[i] = foods[i]
        else:
            accumulate_list[i] = accumulate_list[i-1] + foods[i]
    
    target = accumulate_list[-1]
    if target%3 != 0:
        return 0

    x_number = target//3
    y_number = target//3*2

    x_count = 0

    for i in range(n):
        number = accumulate_list[i]
        if number == x_number:
            x_count += 1
        elif number == y_number:
            answer += x_count
    

    return answer

solution([1,2,3,0,3])

# [1,2,3,0,3]
# 1 3 6 6 9
# [4,1]