N, K = map(int,input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for capacity in range(1, K+1):
        weight, value = items[i-1]

        if capacity < weight:
            dp[i][capacity] = dp[i-1][capacity]
        else:
            dp[i][capacity] = max(dp[i-1][capacity - weight] + value, dp[i - 1][capacity])


answer = dp[N][K]

print(answer)

