def dfs(limit_day, day, payment):
    global result
    if day >= limit_day:
        result = max(result, payment)
        return

    add_day, add_pay = time_pay[day]
    
    dfs(limit_day, day+1, payment)

    if day+add_day-1 < limit_day:
        dfs(limit_day, day+add_day, payment+add_pay)
    else:
        result = max(result, payment)

def another_slove(limit_day):
    dp = [0]*(limit_day+1)
    for i in range(n-1, -1, -1):
        if time_pay[i][0] + i > n:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[ i+1 ], time_pay[i][1] + dp[ time_pay[i][0] + i ])
    
    return dp[0]

n = int(input())
time_pay = [tuple(map(int,input().split())) for _ in range(n)]

result = 0
dfs(n, 0, 0)
print(result)
result = another_slove(n)
print(result)