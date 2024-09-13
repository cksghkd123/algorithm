N, M = map(int, input().split())

dp = []

for _ in range(N):
    dp.append(list(map(int, input().split())))

for j in range(1, M):
    dp[0][j] += dp[0][j-1]

for i in range(1, N):
    left_to_right = dp[i][:]
    right_to_left = dp[i][:]

    for j in range(M):
        if (j == 0):
            left_to_right[j] += dp[i-1][j]
        else:
            left_to_right[j] += max(dp[i-1][j], left_to_right[j-1])

    for j in range(M-1, -1, -1):
        if (j == M-1):
            right_to_left[j] += dp[i-1][j]
        else:
            right_to_left[j] += max(dp[i-1][j], right_to_left[j+1])

    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])

print(dp[N-1][M-1])