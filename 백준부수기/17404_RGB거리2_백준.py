INF = float('inf')

def do_dp(star_i):
    result = INF

    dp = [[INF for _ in range(3)] for _ in range(N)]
    dp[0][star_i] = rgb_list[0][star_i]

    for i in range(1, N-1):
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + rgb_list[i][j])
    
    for i in range(3):
        for j in range(3):
            if i != j and i != star_i:
                dp[N-1][i] = min(dp[N-1][i], dp[N-2][j] + rgb_list[N-1][i])
                result = min(result, dp[N-1][i])
    
    return result

N = int(input())

rgb_list = [list(map(int, input().split())) for _ in range(N)]

answer_list = [do_dp(i) for i in range(3)]

answer = min(answer_list)

print(answer)