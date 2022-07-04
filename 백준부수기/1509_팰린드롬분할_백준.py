line = list(input())
n = len(line)

result = [float('inf')] * (n+1)
result[-1] = 0
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n): # 길이 1짜리
    dp[i][i] = 1
 
for i in range(n-1): # 길이 2짜리
    if line[i] == line[i+1]:
        dp[i][i+1] = 1

for l in range(3, n+1): # 길이 3~n짜리
    for s in range(n-l+1):
        e = s + l - 1
        if line[s] == line[e] and dp[s+1][e-1] == 1:
            dp[s][e] = 1

for end in range(n):
    for start in range(end + 1):
        if dp[start][end]:
            result[end] = min(result[end], result[start - 1] + 1)
        else:
            result[end] = min(result[end], result[end - 1] + 1)

print(result[n - 1])
