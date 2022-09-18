n, m = map(int,input().split())
activating_bytes = [0]+list(map(int,input().split()))
cost_list = [0]+list(map(int,input().split()))

ac_list = []
for i in range(n+1):
    ac_list.append([activating_bytes[i],cost_list[i]])

#maximum_bytes[recent_visited][cost] 조건 당 최대 바이트수
cost_sum = sum(cost_list)
maximum_bytes = [[0 for _ in range(cost_sum+1)] for _ in range(n+1)]
answer = cost_sum


if m == 0:
    answer = 0
else:
    #i(recent_visiteda) 앱사용가능 범위
    for i in range(1,n+1):
        #j(cost) 사용 가능한 cost
        for j in range(1,cost_sum+1):
            if ac_list[i][1] > j:
                maximum_bytes[i][j] = maximum_bytes[i-1][j]
            else:
                maximum_bytes[i][j] = max(ac_list[i][0] + maximum_bytes[i-1][j-ac_list[i][1]], maximum_bytes[i-1][j])

            if maximum_bytes[i][j] >= m:
                answer = min(answer, j)

print(answer)

