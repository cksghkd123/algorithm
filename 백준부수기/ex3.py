import collections


def solution(food_times, k):
    food_times = collections.deque(enumerate(food_times))
    for i in range(k):
        print(i, food_times)
        number, leftover = food_times.popleft()
        leftover -= 1
        if leftover > 0:
            food_times.append((number, leftover))
        
        if food_times == False:
            answer = -1
            break
    
    print(food_times)
    if food_times != -1:
        number, leftover = food_times.popleft()
        answer = number + 1

    return answer



print(solution([3, 1, 2],5))