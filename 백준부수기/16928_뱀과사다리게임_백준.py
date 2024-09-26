N, M = map(int, input().split())

ladders = [i for i in range(101)]

for _ in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    ladders[a] = b

dp = [float('inf') for _ in range(101)]
dp[1] = 0

stack = [1]

while stack:
    i = stack.pop()
    for d in range(1, 7):
        if i+d <= 100:
            j = ladders[i+d]
            if dp[i]+1 < dp[j]:
                dp[j] = dp[i]+1
                stack.append(j)

print(dp[100])