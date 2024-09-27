import collections


N, D = map(int, input().split())

INF = float('inf')
roads = {}

for _ in range(N):
    a, b, d = map(int, input().split())
    if a not in roads:
        roads[a] = [(b, d)]
    else:
        roads[a].append((b, d))

dp = [INF for _ in range(10001)]
dp[0] = 0

for i in range(10000):
    if i in roads:
        for j, d in roads[i]:
            dp[j] = min(dp[j], dp[i]+d)
    
    dp[i+1] = min(dp[i+1], dp[i]+1)

answer = dp[D]


print(answer)