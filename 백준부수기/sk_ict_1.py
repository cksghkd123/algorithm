def solution(money, costs):
    answer = 0

    coins = [1, 5, 10, 50, 100, 500]
    for i in range(5):
        for j in range(i+1,6):
            r = coins[j]//coins[i]
            if r*costs[i] < costs[j]:
                costs[j] = r*costs[i]
    
    for i in range(5, -1, -1):
        answer += costs[i]*(money//coins[i])
        money = money%coins[i]

    return answer

print(solution(4578, [1, 4, 99, 35, 50, 1000]))
print(solution(1999, [2, 11, 20, 100, 200, 600]))
# 4578	[1, 4, 99, 35, 50, 1000]	2308