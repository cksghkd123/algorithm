n = int(input())

line_list = [list(map(int, input().split())) for _ in range(n)]

dp = [1 for _ in range(n)]

line_list.sort()

for i in range(1, n):
    for j in range(0, i):
        if line_list[j][1] < line_list[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))